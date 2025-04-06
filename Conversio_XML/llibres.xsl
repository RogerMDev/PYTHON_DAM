<!-- llibres.xsl -->
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="/">
    <html>
      <head>
        <title>Llistat de Llibres</title>
        <link rel="stylesheet" type="text/css" href="estils.css"/>
      </head>
      <body>
        <h1>Llistat de Llibres disponibles</h1>
        <ul>
          <xsl:for-each select="llibres/llibre">
            <li>
              <a href="https://www.todostuslibros.com/busquedas?keyword={titol}">
                <strong><xsl:value-of select="titol"/></strong>
              </a>
              — <xsl:value-of select="autor"/> - <strong><xsl:value-of select="pagines"/> pàgines</strong>
            </li>
          </xsl:for-each>
        </ul>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
