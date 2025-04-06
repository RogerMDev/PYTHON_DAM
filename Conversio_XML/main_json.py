import xml.etree.ElementTree as ET
import json

# 1. Carregar l'arbre XML des del fitxer
arbre = ET.parse('llibres.xml')
arrel = arbre.getroot()

# 2. Crear una llista per emmagatzemar els llibres
llista_llibres = []

# 3. Iterar per cada element <llibre> dins <llibres>
for llibre in arrel.findall('llibre'):
    titol = llibre.find('titol').text
    autor = llibre.find('autor').text
    pagines = llibre.find('pagines').text

    # 4. Crear un diccionari amb la informació del llibre
    llibre_dict = {
        "titol": titol,
        "autor": autor,
        "pagines": pagines
    }

    # 5. Afegir-lo a la llista
    llista_llibres.append(llibre_dict)

# 6. Escriure la llista en format JSON en un fitxer
with open('llibres.json', 'w', encoding='utf-8') as f:
    json.dump(llista_llibres, f, indent=4, ensure_ascii=False)
