<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:template match="/">
    <html>
      <head>
        <title>Llistat de Llibres</title>
        <style>
          table { border-collapse: collapse; width: 100%; }
          th, td { border: 1px solid black; padding: 8px; text-align: center; }  <!-- Centrado -->
          th { background-color: #f2f2f2; }
          .red-bold { color: red; font-weight: bold; }  <!-- Estilo para páginas > 200 -->
        </style>
      </head>
      <body>
        <h1>Llibres disponibles</h1>

        <table>
          <tr>
            <th>Títol</th>
            <th>Autor</th>
            <th>Número de pàgines</th>
          </tr>
          <xsl:for-each select="llibres/llibre">
            <tr>
              <td><xsl:value-of select="titol"/></td>
              <td><xsl:value-of select="autor"/></td>
              <!-- Condición para páginas mayores a 200 -->
              <xsl:choose>
                <xsl:when test="pagines > 200">
                  <td class="red-bold"><xsl:value-of select="pagines"/></td>
                </xsl:when>
                <xsl:otherwise>
                  <td><xsl:value-of select="pagines"/></td>
                </xsl:otherwise>
              </xsl:choose>
            </tr>
          </xsl:for-each>
        </table>

      </body>
    </html>
  </xsl:template>

</xsl:stylesheet>

