import xmltodict
import json

def convert_xml_to_json(xml_file, json_file):
    try:
        # Leer el archivo XML
        with open(xml_file, "r", encoding="utf-8") as file:
            xml_content = file.read()

        # Convertir XML a diccionario
        dict_data = xmltodict.parse(xml_content)

        # Convertir diccionario a JSON
        json_data = json.dumps(dict_data, indent=4,ensure_ascii=False)

        # Guardar JSON en un archivo
        with open(json_file, "w", encoding="utf-8") as file:
            file.write(json_data)

        print(f"✅ Conversión completada: {json_file}")

    except Exception as e:
        print(f"❌ Error: {e}")

# Ejemplo de uso
xml_file = "pruebaxml.xml"  # Nombre del archivo XML de entrada
json_file = "pruebajson.json"  # Nombre del archivo JSON de salida

convert_xml_to_json(xml_file, json_file)



