
def contar_palabras(fichero, palabra):
    try:
        with open(fichero, "r", encoding="utf-8") as quijote:
            contenido = quijote.read()
            conteado = contenido.count(palabra)
            print(f"La palabra {palabra} aparece {conteado} veces.")
            return conteado
    except:
        print("Ha habido un error")
        return -1

#contar_palabras("quijote.txt","la")

def cambiar_texto(fichero, cadenaAreemplazar, nueva_cadena):

    try :
        with open(fichero, "r+", encoding="utf-8") as texto:
            textoleido = texto.read()
            textoreemplazado = textoleido.replace(cadenaAreemplazar, nueva_cadena)
            texto.write(textoreemplazado)
            print(f"Se han reemplazado todas las palabras {cadenaAreemplazar} por {nueva_cadena}")
    except:
        print("Ha habido un error")
        return -1


cambiar_texto("quijote.txt","Quijote", "Pepe")