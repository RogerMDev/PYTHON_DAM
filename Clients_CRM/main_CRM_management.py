import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error, IntegrityError

# =========================
# Connexió a la BD
# =========================
def get_conn():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            database='hipoaposta',
            user='root',
            password='admin'
        )
        return conn
    except Error as e:
        messagebox.showerror("Error MySQL", f"No s'ha pogut connectar:\n{e}")
        raise


# =========================
# Funcions CRUD
# =========================
def fetch_clients(filtre_nom=None):
    """
    Retorna:
      (id, dni_nie, nom, cognoms, email, telefon, saldo_actual, tipus_client, estat)
    """
    conn = None
    try:
        conn = get_conn()
        cur = conn.cursor()
        if filtre_nom:
            cur.execute(
                """
                SELECT id, dni_nie, nom, cognoms, email, telefon,
                       saldo_actual, tipus_client, estat
                FROM clients
                WHERE nom LIKE %s
                ORDER BY id;
                """,
                (f"%{filtre_nom}%",)
            )
        else:
            cur.execute(
                """
                SELECT id, dni_nie, nom, cognoms, email, telefon,
                       saldo_actual, tipus_client, estat
                FROM clients
                ORDER BY id;
                """
            )
        return cur.fetchall()
    finally:
        if conn:
            conn.close()


def insert_client(dni_nie, nom, cognoms, email, telefon, saldo_actual, tipus_client, estat):
    """
    Insereix un nou client.
    - data_registre NO es demana: s'assigna automàticament amb CURDATE() a la BD.
    """
    dni_nie = (dni_nie or "").strip() or None
    nom = (nom or "").strip()
    cognoms = (cognoms or "").strip()
    email = (email or "").strip()
    telefon = (telefon or "").strip()
    tipus_client = (tipus_client or "").strip() or None
    estat = (estat or "").strip() or None

    if not nom or not cognoms or not email or not telefon:
        raise ValueError("Nom, cognoms, email i telèfon són obligatoris.")

    if "@" not in email:
        raise ValueError("L'email ha de contenir un '@'.")

    if saldo_actual in (None, ""):
        saldo_float = 0.0
    else:
        try:
            saldo_float = float(saldo_actual)
        except ValueError:
            raise ValueError("El saldo actual ha de ser un número vàlid.")
        if saldo_float < 0:
            raise ValueError("El saldo actual no pot ser negatiu.")

    valors_tipus = {"regular", "vip", "premium"}
    valors_estat = {"actiu", "suspès", "inactiu"}

    if tipus_client and tipus_client not in valors_tipus:
        raise ValueError("Tipus de client invàlid. Usa: regular, vip o premium.")
    if estat and estat not in valors_estat:
        raise ValueError("Estat invàlid. Usa: actiu, suspès o inactiu.")

    conn = None
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO clients (
                dni_nie, nom, cognoms, email, telefon,
                saldo_actual, tipus_client, estat, data_registre
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, CURDATE())
            """,
            (dni_nie, nom, cognoms, email, telefon,
             saldo_float, tipus_client, estat),
        )
        conn.commit()
    except IntegrityError as e:
        msg = str(e)
        if "Duplicate entry" in msg and "dni_nie" in msg:
            raise ValueError("Ja existeix un client amb aquest DNI/NIE.")
        if "Duplicate entry" in msg and "email" in msg:
            raise ValueError("Ja existeix un client amb aquest email.")
        raise
    finally:
        if conn:
            conn.close()


def update_client(client_id, dni_nie, nom, cognoms, email, telefon,
                  saldo_actual, tipus_client, estat):
    """
    Actualitza un client existent.
    Mateixa validació que insert_client.
    """
    dni_nie = (dni_nie or "").strip() or None
    nom = (nom or "").strip()
    cognoms = (cognoms or "").strip()
    email = (email or "").strip()
    telefon = (telefon or "").strip()
    tipus_client = (tipus_client or "").strip() or None
    estat = (estat or "").strip() or None

    if not nom or not cognoms or not email or not telefon:
        raise ValueError("Nom, cognoms, email i telèfon són obligatoris.")

    if "@" not in email:
        raise ValueError("L'email ha de contenir un '@'.")

    if saldo_actual in (None, ""):
        saldo_float = 0.0
    else:
        try:
            saldo_float = float(saldo_actual)
        except ValueError:
            raise ValueError("El saldo actual ha de ser un número vàlid.")
        if saldo_float < 0:
            raise ValueError("El saldo actual no pot ser negatiu.")

    valors_tipus = {"regular", "vip", "premium"}
    valors_estat = {"actiu", "suspès", "inactiu"}

    if tipus_client and tipus_client not in valors_tipus:
        raise ValueError("Tipus de client invàlid. Usa: regular, vip o premium.")
    if estat and estat not in valors_estat:
        raise ValueError("Estat invàlid. Usa: actiu, suspès o inactiu.")

    conn = None
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            """
            UPDATE clients
            SET dni_nie = %s,
                nom = %s,
                cognoms = %s,
                email = %s,
                telefon = %s,
                saldo_actual = %s,
                tipus_client = %s,
                estat = %s
            WHERE id = %s
            """,
            (dni_nie, nom, cognoms, email, telefon,
             saldo_float, tipus_client, estat, client_id),
        )
        if cur.rowcount == 0:
            raise ValueError("No s'ha trobat cap client amb aquest ID.")
        conn.commit()
    except IntegrityError as e:
        msg = str(e)
        if "Duplicate entry" in msg and "dni_nie" in msg:
            raise ValueError("Ja existeix un client amb aquest DNI/NIE.")
        if "Duplicate entry" in msg and "email" in msg:
            raise ValueError("Ja existeix un client amb aquest email.")
        raise
    finally:
        if conn:
            conn.close()


def delete_client_db(client_id):
    conn = None
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("DELETE FROM clients WHERE id=%s", (client_id,))
        conn.commit()
    finally:
        if conn:
            conn.close()


# =========================
# Interfície Tkinter
# =========================
def refresh_tree(tree, filtre_nom=None):
    tree.delete(*tree.get_children())
    try:
        rows = fetch_clients(filtre_nom)
        for row in rows:
            tree.insert("", tk.END, values=row)
    except Exception as e:
        messagebox.showerror("Càrrega de dades", str(e))


def open_client_form(tree, client_data=None):
    """
    Formulari Afegir / Editar client.
    client_data = tupla (fila del tree) o None.
    """
    win = tk.Toplevel()
    win.title("Editar client" if client_data else "Afegir client")
    win.geometry("460x380")
    win.resizable(False, False)
    win.transient(tree.winfo_toplevel())
    win.grab_set()

    frame = ttk.Frame(win, padding=15)
    frame.pack(fill="both", expand=True)

    camps = [
        ("DNI/NIE", "dni_nie"),
        ("Nom", "nom"),
        ("Cognoms", "cognoms"),
        ("Email", "email"),
        ("Telèfon", "telefon"),
        ("Saldo actual", "saldo_actual"),
        ("Tipus client", "tipus_client"),          # desplegable
        ("Estat", "estat"),                        # desplegable
    ]

    entries = {}

    # Map de columnes segons SELECT a fetch_clients:
    # 0:id, 1:dni_nie, 2:nom, 3:cognoms, 4:email, 5:telefon, 6:saldo_actual, 7:tipus_client, 8:estat
    index_map = {
        "dni_nie": 1,
        "nom": 2,
        "cognoms": 3,
        "email": 4,
        "telefon": 5,
        "saldo_actual": 6,
        "tipus_client": 7,
        "estat": 8,
    }

    for i, (label_text, field_key) in enumerate(camps):
        ttk.Label(frame, text=label_text + ":").grid(row=i, column=0, sticky="w", pady=3)

        # Para tipus_client y estat usamos Combobox con opciones fijas
        if field_key == "tipus_client":
            widget = ttk.Combobox(
                frame,
                values=("regular", "vip", "premium"),
                state="readonly",
                width=32,
            )
        elif field_key == "estat":
            widget = ttk.Combobox(
                frame,
                values=("actiu", "suspès", "inactiu"),
                state="readonly",
                width=32,
            )
        else:
            widget = ttk.Entry(frame, width=35)

        widget.grid(row=i, column=1, sticky="ew", pady=3)

        # Rellenar datos si estamos editando
        if client_data:
            idx = index_map[field_key]
            value = client_data[idx]
            if value is None:
                value = ""
            if isinstance(widget, ttk.Combobox):
                widget.set(str(value))
            else:
                widget.insert(0, str(value))

        entries[field_key] = widget

    client_id = client_data[0] if client_data else None

    def on_save():
        try:
            dni_nie = entries["dni_nie"].get()
            nom = entries["nom"].get()
            cognoms = entries["cognoms"].get()
            email = entries["email"].get()
            telefon = entries["telefon"].get()
            saldo_actual = entries["saldo_actual"].get()
            tipus_client = entries["tipus_client"].get()
            estat = entries["estat"].get()

            if client_id is None:
                insert_client(dni_nie, nom, cognoms, email, telefon,
                              saldo_actual, tipus_client, estat)
                messagebox.showinfo("Èxit", "Client afegit correctament.", parent=win)
            else:
                update_client(client_id, dni_nie, nom, cognoms, email, telefon,
                              saldo_actual, tipus_client, estat)
                messagebox.showinfo("Èxit", "Client actualitzat correctament.", parent=win)

            win.destroy()
            refresh_tree(tree)
        except ValueError as ve:
            messagebox.showwarning("Validació", str(ve), parent=win)
        except Exception as e:
            messagebox.showerror("Error BD", str(e), parent=win)

    ttk.Button(frame, text="Guardar", command=on_save).grid(
        row=len(camps), column=0, columnspan=2, pady=10
    )


def delete_selected(tree):
    sel = tree.selection()
    if not sel:
        messagebox.showwarning("Selecciona", "Tria un client.", parent=tree.winfo_toplevel())
        return

    values = tree.item(sel[0], "values")
    client_id = values[0]

    if not messagebox.askyesno("Confirmar", "Vols eliminar el client seleccionat?",
                               parent=tree.winfo_toplevel()):
        return

    try:
        delete_client_db(client_id)
        messagebox.showinfo("Èxit", "Client eliminat.", parent=tree.winfo_toplevel())
        refresh_tree(tree)
    except Exception as e:
        messagebox.showerror("Error BD", str(e), parent=tree.winfo_toplevel())


def main():
    root = tk.Tk()
    root.title("Gestió de Clients — HipoAposta (MySQL)")
    root.geometry("1050x500")

    # ====== BARRA SUPERIOR: filtre + botons ======
    top_bar = ttk.Frame(root, padding=8)
    top_bar.pack(fill="x")

    ttk.Label(top_bar, text="Filtre nom:").pack(side="left")
    entry_filter = ttk.Entry(top_bar, width=30)
    entry_filter.pack(side="left", padx=5)

    # ====== FRAME PRINCIPAL AMB LA TAULA ======
    main_frame = ttk.Frame(root, padding=12)
    main_frame.pack(fill="both", expand=True)

    cols = ("ID", "DNI/NIE", "Nom", "Cognoms", "Email",
            "Telèfon", "Saldo", "Tipus", "Estat")
    tree = ttk.Treeview(main_frame, columns=cols, show="headings", selectmode="browse")

    for c in cols:
        tree.heading(c, text=c)
        if c in ("Email", "Cognoms"):
            tree.column(c, width=220, anchor="w")
        elif c == "Saldo":
            tree.column(c, width=90, anchor="e")
        else:
            tree.column(c, width=110, anchor="w")

    tree.grid(row=0, column=0, sticky="nsew")
    vsb = ttk.Scrollbar(main_frame, orient="vertical", command=tree.yview)
    vsb.grid(row=0, column=1, sticky="ns")
    tree.configure(yscrollcommand=vsb.set)

    main_frame.rowconfigure(0, weight=1)
    main_frame.columnconfigure(0, weight=1)

    # ====== Funcions de filtre ======
    def do_search():
        filtre = entry_filter.get().strip()
        refresh_tree(tree, filtre)

    def reset_filter():
        entry_filter.delete(0, tk.END)
        refresh_tree(tree)

    # ====== Botons barra superior ======
    btn_cercar = ttk.Button(top_bar, text="Cercar", command=do_search)
    btn_cercar.pack(side="left", padx=3)

    btn_reiniciar = ttk.Button(top_bar, text="Reiniciar", command=reset_filter)
    btn_reiniciar.pack(side="left", padx=3)

    btn_afegir = ttk.Button(top_bar, text="Afegir",
                            command=lambda: open_client_form(tree))
    btn_afegir.pack(side="left", padx=8)

    btn_editar = ttk.Button(
        top_bar,
        text="Editar",
        state="disabled",
        command=lambda: open_client_form(
            tree,
            tree.item(tree.selection()[0], "values")
        )
    )
    btn_editar.pack(side="left", padx=3)

    btn_eliminar = ttk.Button(
        top_bar,
        text="Eliminar",
        state="disabled",
        command=lambda: delete_selected(tree)
    )
    btn_eliminar.pack(side="left", padx=3)

    # ====== Habilitar / deshabilitar Editar / Eliminar segons selecció ======
    def on_select(_event):
        enabled = bool(tree.selection())
        btn_editar.config(state="normal" if enabled else "disabled")
        btn_eliminar.config(state="normal" if enabled else "disabled")

    tree.bind("<<TreeviewSelect>>", on_select)

    # Càrrega inicial sense filtre
    refresh_tree(tree)

    root.mainloop()


if __name__ == "__main__":
    main()
