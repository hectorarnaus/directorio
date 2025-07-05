import os
import openpyxl 
#from autowordpress import *

def crea_provincia(home,provincia,texto,imagen):

    res=('<!-- wp:html -->\n'
        '\t<div class="migas">\n'
        f'\t\t<p><a href="{home}">Inicio</a> &gt; {provincia}</p>\n'
        '\t</div>\n'
        '<!-- /wp:html -->\n'
        '<!-- wp:media-text {"mediaPosition":"right","mediaId":178,"mediaLink":"https://calculadora-porcentajes-colombia.top/localidad/ciudad/#main","mediaType":"image"} -->\n'
        '<div class="wp-block-media-text has-media-on-the-right is-stacked-on-mobile"><div class="wp-block-media-text__content"><!-- wp:paragraph {"placeholder":"Contenido…"} -->\n'
        f'\t\t<p>{texto}</p>\n'
        f'\t\t<!-- /wp:paragraph -->\n'
        '\t</div>\n'
        f'<figure class="wp-block-media-text__media"><img src="{imagen}" alt="" class="wp-image-178 size-full"/></figure></div>\n'
        '<!-- /wp:media-text -->\n'
        '<!-- wp:group {"layout":{"type":"constrained"}} -->\n'
        '\t<div class="wp-block-group">\n'
        '\t\t<!-- wp:heading {"textAlign":"center"} -->\n'
        f'\t\t\t<h2 class="wp-block-heading has-text-align-center">Todas las creperias de {provincia}</h2>\n'
        '\t\t<!-- /wp:heading -->\n'
        f'\t\t<!-- wp:dpt/display-post-types {{"taxonomy":"category","terms":["{provincia}"],"number":100,"styleSup":["title"],"showPgnation":true}} /-->\n'
        '\t</div>\n'
        '\t<!-- /wp:group -->\n')
    return res



#wc=WpConnection("https://calculadora-porcentajes-colombia.top//xmlrpc.php",'hector.arnaus@gmail.com','bolo3o,Eresgay')
#wc.connect()

etiquetas=['crepería','crepes']
ciudades=[]
provincias=[]
#print(crea_provincia("http://www.creperias.com","Valencia","Este es un texto de prueba de la provincia",'https://calculadora-porcentajes-colombia.top/wp-content/uploads/2025/06/valencia.jpg'))
print(obten_lista_municipios("castilla_leon_1.xlsx"))

'''creperias=openpyxl.load_workbook('creperias.xlsx')
hoja_activa = creperias.active
fila=1
while fila<hoja_activa.max_row:
    print(hoja_activa.cell(row=fila,column=1).value)
    fila+=1'''