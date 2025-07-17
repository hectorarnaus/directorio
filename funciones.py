import random, re

def sluguiza(texto):
    texto=texto.strip()
    texto=texto.lower()
    texto=texto.replace("ñ","n")
    texto=texto.replace("á","a")
    texto=texto.replace("é","e")
    texto=texto.replace("í","i")
    texto=texto.replace("ó","o")
    texto=texto.replace("ú","u")
    texto=texto.replace("ü","u")
    texto=texto.replace("de","")
    texto=texto.replace("el","")
    texto=texto.replace("la","")
    texto=texto.replace("los","")
    texto=texto.replace("las","")
    texto=texto.replace(" ","-")
    while texto.find("--")!=-1:
        texto=texto.replace("--","-")
    
    return texto

def spinner(s):
     
    while True:
        s, n = re.subn('{([^{}]*)}',
                    lambda m: random.choice(m.group(1).split("|")),
                    s)
        if n == 0: break
    return s.strip()

def crea_provincia(home,provincia,texto,imagen):
    res=('<!-- wp:html -->\n'
        '\t<div class="migas">\n'
        f'\t\t<p><a href="{home}">Inicio</a> &gt; {provincia}</p>\n'
        '\t</div>\n'
        '<!-- /wp:html -->\n'
        f'<!-- wp:media-text {{"mediaPosition":"right","mediaId":{imagen.get_id()},"mediaLink":"https://calculadora-porcentajes-colombia.top/localidad/ciudad/#main","mediaType":"image"}} -->\n'
        '<div class="wp-block-media-text has-media-on-the-right is-stacked-on-mobile"><div class="wp-block-media-text__content"><!-- wp:paragraph {"placeholder":"Contenido…"} -->\n'
        f'\t\t<p>{texto}</p>\n'
        f'\t\t<!-- /wp:paragraph -->\n'
        '\t</div>\n'
        f'<figure class="wp-block-media-text__media"><img src="{imagen.get_url()}" alt="" class="wp-image-178 size-full"/></figure></div>\n'
        '<!-- /wp:media-text -->\n'
        '<!-- wp:group {"layout":{"type":"constrained"}} -->\n'
        '\t<div class="wp-block-group">\n'
        '\t\t<!-- wp:heading {"textAlign":"center"} -->\n'
        f'\t\t\t<h2 class="wp-block-heading has-text-align-center">Todas las creperias de {provincia} ordenadas por nombre de municipio</h2>\n'
        '\t\t<!-- /wp:heading -->\n'
        f'\t\t<!-- wp:dpt/display-post-types {{"taxonomy":"category","terms":["{provincia}"],"number":100,"styleSup":["title"],"showPgnation":true}} /-->\n'
        '\t</div>\n'
        '\t<!-- /wp:group -->\n')
    return res

def crea_municipio(home,municipio,provincia,texto,imagen):
    res=('<!-- wp:html -->\n'
        '\t<div class="migas">\n'
        f'\t\t<p><a href="{home}">Inicio</a> &gt; <a href="{home}/{provincia}">{provincia}</a> &gt; {municipio}</p>'
        '\t</div>\n'
        '<!-- /wp:html -->'
        f'<!-- wp:media-text {{"mediaPosition":"right","mediaId":{imagen.get_id()},"mediaLink":"https://calculadora-porcentajes-colombia.top/localidad/ciudad/#main","mediaType":"image"}} -->\n'
        '<div class="wp-block-media-text has-media-on-the-right is-stacked-on-mobile"><div class="wp-block-media-text__content"><!-- wp:paragraph {"placeholder":"Contenido…"} -->\n'
        f'\t\t<p>{texto}</p>\n'
        f'<!-- /wp:paragraph --></div><figure class="wp-block-media-text__media"><img src="{imagen.get_url()}" alt="" class="wp-image-{imagen.get_id()} size-full"/></figure></div>\n'
        '<!-- /wp:media-text -->\n'
        '<!-- wp:group {"layout":{"type":"constrained"}} -->\n'
        '\t<div class="wp-block-group">\n'
        '\t\t<!-- wp:heading {"textAlign":"center"} -->\n'
        f'\t\t\t<h2 class="wp-block-heading has-text-align-center">Todas las creperias de {municipio}</h2>\n'
        '\t\t<!-- /wp:heading -->\n'
        '\t<!-- wp:dpt/display-post-types {"taxonomy":"category","terms":["blog"],"number":100,"styleSup":["title"],"showPgnation":true} /--></div>\n'
        '<!-- /wp:group -->')
    return res

def obten_nombre_provincia(imagen):
   return imagen.split(".")[0]

def obten_nombre_municipio(imagen):
   return imagen.split("_")[0]

def obten_nombre_provincia_municipio(imagen):
    aux=imagen.split("_")[1]
    return aux.split(".")[0]

def obten_texto_provincia(provincia):
    with open('provincia.txt', 'r') as file :
        texto_base = file.read()
        texto=spinner(texto_base)
        texto=texto.replace("*Provincia*",provincia)
        return texto
    
def obten_texto_municipio(municipio):
    with open('municipio.txt', 'r') as file :
        texto_base = file.read()
        texto=spinner(texto_base)
        texto=texto.replace("*Municipio*",municipio)
        return texto