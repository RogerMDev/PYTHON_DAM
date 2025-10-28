import tkinter as tk
from tkinter import ttk, messagebox

import psycopg
from psycopg import OperationalError, IntegrityError

# =========================
# Configuración de conexión
# =========================
DB_CONFIG = {
    "host": "127.0.0.1",   # o 'localhost'
    "port": 5432,          # config per PGADMIN
    "user": "crm_user",
    "password": "TuPassFuerte_123!",
    "dbname": "erp_demo",
}

# =========================
# Acceso a la base de datos
# =========================
def get_conn():
    try:
        return psycopg.connect(connect_timeout=5, **DB_CONFIG)
    except OperationalError as e:
        messagebox.showerror("PostgreSQL", f"No se pudo conectar a la BD:\n{e}")
        raise

def fetch_clients():
    conn = None
    try:
        conn = get_conn()
        with conn.cursor() as cur:
            cur.execute("SET search_path TO public;")
            cur.execute("SELECT id, nom, email, telefon, ciutat FROM client ORDER BY id;")
            return cur.fetchall()
    finally:
        if conn:
            conn.close()

def insert_client(nom, email, telefon, ciutat):
    conn = None
    try:
        conn = get_conn()
        with conn.cursor() as cur:
            cur.execute("SET search_path TO public;")
            cur.execute(
                "INSERT INTO client (nom, email, telefon, ciutat) VALUES (%s, %s, %s, %s)",
                (nom, email, telefon, ciutat),
            )
        conn.commit()
    except IntegrityError as e:
        if conn: conn.rollback()
        if getattr(e, "pgcode", None) == errorcodes.UNIQUE_VIOLATION:
            raise ValueError(f"El email '{email}' ya existe.")
        raise
    except Exception:
        if conn: conn.rollback()
        raise
    finally:
        if conn:
            conn.close()

def update_client(client_id, nom, email, telefon, ciutat):
    conn = None
    try:
        conn = get_conn()
        with conn.cursor() as cur:
            cur.execute("SET search_path TO public;")
            cur.execute(
                "UPDATE client SET nom=%s, email=%s, telefon=%s, ciutat=%s WHERE id=%s",
                (nom, email, telefon, ciutat, client_id),
            )
        conn.commit()
    except IntegrityError as e:
        if conn: conn.rollback()
        if getattr(e, "pgcode", None) == errorcodes.UNIQUE_VIOLATION:
            raise ValueError(f"El email '{email}' ya existe.")
        raise
    except Exception:
        if conn: conn.rollback()
        raise
    finally:
        if conn:
            conn.close()

def delete_client_db(client_id):
    conn = None
    try:
        conn = get_conn()
        with conn.cursor() as cur:
            cur.execute("SET search_path TO public;")
            cur.execute("DELETE FROM client WHERE id=%s", (client_id,))
        conn.commit()
    except Exception:
        if conn: conn.rollback()
        raise
    finally:
        if conn:
            conn.close()

# =========================
# Interfaz Tkinter
# =========================
def refresh_tree(tree: ttk.Treeview):
    for item in tree.get_children():
        tree.delete(item)
    try:
        for row in fetch_clients():
            tree.insert("", tk.END, values=row)
    except Exception as e:
        messagebox.showerror("Cargar datos", str(e))

def open_client_form(tree: ttk.Treeview, client_data=None):
    win = tk.Toplevel()
    win.title("Modificar cliente" if client_data else "Nuevo cliente")
    win.geometry("420x260")
    win.resizable(False, False)
    win.transient(tree.winfo_toplevel())
    win.grab_set()

    frame = ttk.Frame(win, padding=15)
    frame.pack(fill="both", expand=True)

    labels = [("Nombre", "nom"), ("Email", "email"), ("Teléfono", "telefon"), ("Ciudad", "ciutat")]
    entries = {}
    for i, (text, key) in enumerate(labels):
        ttk.Label(frame, text=text + ":").grid(row=i, column=0, sticky="w", pady=5, padx=5)
        ent = ttk.Entry(frame, width=36)
        ent.grid(row=i, column=1, sticky="ew", pady=5, padx=5)
        if client_data:
            idx = {"nom": 1, "email": 2, "telefon": 3, "ciutat": 4}[key]
            ent.insert(0, client_data[idx] or "")
        entries[key] = ent

    client_id = int(client_data[0]) if client_data else None

    def save():
        nom = entries["nom"].get().strip()
        email = entries["email"].get().strip()
        telefon = entries["telefon"].get().strip()
        ciutat = entries["ciutat"].get().strip()

        if not nom or not email:
            messagebox.showwarning("Validación", "Nombre y email son obligatorios.", parent=win)
            return
        if "@" not in email or "." not in email.split("@")[-1]:
            if not messagebox.askyesno("¿Email correcto?",
                                       "El email no parece válido. ¿Guardar igualmente?",
                                       parent=win):
                return
        try:
            if client_id is None:
                insert_client(nom, email, telefon, ciutat)
                messagebox.showinfo("Éxito", "Cliente añadido.", parent=win)
            else:
                update_client(client_id, nom, email, telefon, ciutat)
                messagebox.showinfo("Éxito", "Cliente actualizado.", parent=win)
            win.destroy()
            refresh_tree(tree)
        except ValueError as ve:
            messagebox.showerror("Datos duplicados", str(ve), parent=win)
        except Exception as e:
            messagebox.showerror("BD", f"Ocurrió un error:\n{e}", parent=win)

    btn = ttk.Button(frame, text="Guardar", command=save)
    btn.grid(row=len(labels), column=0, columnspan=2, pady=16)
    entries["nom"].focus_set()

def delete_selected(tree: ttk.Treeview):
    sel = tree.selection()
    if not sel:
        messagebox.showwarning("Selecciona", "Elige un cliente a eliminar.")
        return
    if not messagebox.askyesno("Confirmar", "¿Eliminar el cliente seleccionado?"):
        return
    values = tree.item(sel[0], "values")
    try:
        delete_client_db(int(values[0]))
        messagebox.showinfo("Éxito", "Cliente eliminado.")
        refresh_tree(tree)
    except Exception as e:
        messagebox.showerror("BD", f"No se pudo eliminar:\n{e}")

def main():
    root = tk.Tk()
    root.title("Gestión de Clientes — PostgreSQL")
    root.geometry("860x480")

    main_frame = ttk.Frame(root, padding=12)
    main_frame.pack(fill="both", expand=True)

    cols = ("ID", "Nombre", "Email", "Teléfono", "Ciudad")
    tree = ttk.Treeview(main_frame, columns=cols, show="headings", selectmode="browse")
    for c in cols:
        tree.heading(c, text=c)
        tree.column(c, width=120 if c != "Email" else 240, anchor="w")

    vsb = ttk.Scrollbar(main_frame, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(main_frame, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(row=0, column=0, sticky="nsew")
    vsb.grid(row=0, column=1, sticky="ns")
    hsb.grid(row=1, column=0, sticky="ew")
    main_frame.rowconfigure(0, weight=1)
    main_frame.columnconfigure(0, weight=1)

    btns = ttk.Frame(root, padding=(12, 0, 12, 12))
    btns.pack(fill="x")

    ttk.Button(btns, text="Nuevo", command=lambda: open_client_form(tree)).pack(side="left")
    edit_btn = ttk.Button(btns, text="Modificar", state="disabled",
                          command=lambda: open_client_form(tree, tree.item(tree.selection()[0], "values")))
    edit_btn.pack(side="left", padx=6)
    del_btn = ttk.Button(btns, text="Eliminar", state="disabled", command=lambda: delete_selected(tree))
    del_btn.pack(side="left")

    ttk.Button(btns, text="Refrescar", command=lambda: refresh_tree(tree)).pack(side="right")
    ttk.Button(btns, text="Salir", command=root.destroy).pack(side="right", padx=6)

    def on_select(_):
        has = bool(tree.selection())
        edit_btn.config(state="normal" if has else "disabled")
        del_btn.config(state="normal" if has else "disabled")

    tree.bind("<<TreeviewSelect>>", on_select)

    refresh_tree(tree)
    root.mainloop()

if __name__ == "__main__":
    main()
