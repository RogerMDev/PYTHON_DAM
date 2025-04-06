from lxml import etree

# Llegir els fitxers XML i XSL
xml_doc = etree.parse("llibres.xml")
xsl_doc = etree.parse("llibres.xsl")

# Crear l'objecte transformador
transformador = etree.XSLT(xsl_doc)

# Aplicar la transformació
html_resultat = transformador(xml_doc)

# Guardar el resultat com a fitxer HTML
with open("resultat.html", "w", encoding="utf-8") as f:
    f.write(str(html_resultat))
