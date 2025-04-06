def ejercicio1():
    with open("frase.txt", "r",encoding="utf-8") as fitxer:
        contador = 1
        for frase in fitxer:
            print(f"{contador}: {frase.strip()}")
            contador+= 1

def ejercicio2():
    frase = input("Digues quina frase vols afegir")
    with open("frase.txt", "a",encoding="utf-8") as fitxer:
        fitxer.write(f"\n{frase}")

def ejercicio3():
    try:
        frase = input("Digues quina frase vols afegir")
        with open("frases.txt", "r",encoding="utf-8") as fitxer:
            fitxer.write(f"\n{frase}")
    except FileNotFoundError:
        print("No s'ha trobat el fitxer")

ejercicio3()

