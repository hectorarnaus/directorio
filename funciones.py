import random, re

def sluguiza(texto):
    texto=texto.strip()
    texto=texto.lower()
    texto=texto.replace("ñ","n")
    texto=texto.replace("á","a")
    texto=texto.replace("ä","a")
    texto=texto.replace("à","a")
    texto=texto.replace("â","a")
    texto=texto.replace("é","e")
    texto=texto.replace("ê","e")
    texto=texto.replace("ë","e")
    texto=texto.replace("è","e")
    texto=texto.replace("í","i")
    texto=texto.replace("ï","i")
    texto=texto.replace("ì","i")
    texto=texto.replace("ó","o")
    texto=texto.replace("ö","o")
    texto=texto.replace("ò","o")
    texto=texto.replace("ú","u")
    texto=texto.replace("ü","u")
    texto=texto.replace("ù","u")
    '''
    texto=texto.replace(" de las ","-")
    texto=texto.replace(" de los ","-")
    texto=texto.replace(" de ","-")
    texto=texto.replace(" del ","-")
    texto=texto.replace(" el ","-")
    texto=texto.replace(" la ","-")
    texto=texto.replace(" los ","-")
    texto=texto.replace(" las ","-")'''
    texto=texto.replace(" ","-")
    texto=texto.replace("&quot;","'")
    texto=texto.replace("&amp;","&")
    texto=texto.replace("&apos;","'")
    texto=texto.replace("|","")
    texto=texto.replace(".","")
    texto=texto.replace(",","")
    texto=texto.replace("*","")
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

def obten_id_categoria_provincia(provincia,lista_categorias):
    for categoria in lista_categorias:
        if categoria.get('Nombre')==provincia:
            print("encontrada")
            return categoria['Id']
    return 0

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
        f'\t\t<!-- wp:dpt/display-post-types {{"taxonomy":"category","terms":["Provincia de {provincia}"],"number":100,"styleSup":["title"],"showPgnation":true}} /-->\n'
        '\t</div>\n'
        '\t<!-- /wp:group -->\n')
    return res

def crea_municipio(home,municipio,provincia,texto,imagen):
    res=('<!-- wp:html -->\n'
        '\t<div class="migas">\n'
        f'\t\t<p><a href="{home}">Inicio</a> &gt; <a href="{home}/{sluguiza("Provincia de "+provincia)}">{provincia}</a> &gt; {municipio}</p>'
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
        f'\t<!-- wp:dpt/display-post-types {{"taxonomy":"category","terms":["{municipio}"],"number":100,"styleSup":["title"],"showPgnation":true}} /--></div>\n'

        '<!-- /wp:group -->')
    '''
    {
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Mejores creperías en Valladolid",
  "description": "Directorio de creperías recomendadas en Valladolid",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "item": {
        "@type": "Restaurant",
        "@id": "https://midominio.com/valladolid/creperia-la-dulce/",
        "url": "https://midominio.com/valladolid/creperia-la-dulce/",
        "name": "Crepería La Dulce",
        "image": "https://midominio.com/wp-content/uploads/creperia-la-dulce.jpg",
        "servesCuisine": "Creperie",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "Calle Mayor 12",
          "addressLocality": "Valladolid",
          "addressRegion": "Valladolid",
          "postalCode": "47001",
          "addressCountry": "ES"
        },
        "telephone": "+34 912 345 678",
        "priceRange": "$$",
        "aggregateRating": {
          "@type": "AggregateRating",
          "ratingValue": "4.5",
          "reviewCount": "127"
        }
      }
    },
    {
      "@type": "ListItem",
      "position": 2,
      "item": {
        "@type": "Restaurant",
        "@id": "https://midominio.com/valladolid/creperia-el-sabor/",
        "url": "https://midominio.com/valladolid/creperia-el-sabor/",
        "name": "Crepería El Sabor",
        "image": "https://midominio.com/wp-content/uploads/creperia-el-sabor.jpg",
        "servesCuisine": "Creperie",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "Avenida Central 45",
          "addressLocality": "Valladolid",
          "addressRegion": "Valladolid",
          "postalCode": "47002",
          "addressCountry": "ES"
        },
        "telephone": "+34 987 654 321",
        "priceRange": "$$",
        "aggregateRating": {
          "@type": "AggregateRating",
          "ratingValue": "4.3",
          "reviewCount": "98"
        }
      }
    }
  ]
}
'''
    return res

def crea_negocio(home,negocio):

    res=('<!-- wp:html -->\n'
        '\t<div class="migas">\n'
        f'\t\t<p><a href="{home}">Inicio</a> &gt; <a href="{home}/{sluguiza("Provincia de "+negocio.provincia)}">{negocio.provincia}</a> &gt; <a href="{home}/{sluguiza(negocio.municipio)}">{negocio.municipio}</a> &gt; {negocio.nombre}</p>'
        '\t</div>\n'
        '<!-- /wp:html -->\n'

        '<!-- wp:columns -->\n'
        '<div class="wp-block-columns"><!-- wp:column {"className":"contenedor"} -->\n'
        '\t<div class="wp-block-column contenedor"><!-- wp:heading {"textAlign":"center"} -->\n'
        '\t\t<h2 class="wp-block-heading has-text-align-center">Datos de contacto</h2>\n'
        '\t<!-- /wp:heading -->\n'

        '\t<!-- wp:paragraph -->'
        f'\t\t<p><strong>Dirección postal:</strong> {negocio.direccion}</p>\n'
        '\t<!-- /wp:paragraph -->\n'

        '\t<!-- wp:paragraph -->\n'
        f'\t\t<p><strong>Teléfono:</strong> {negocio.telefono}</p>\n'
        '\t<!-- /wp:paragraph -->\n'

        '\t<!-- wp:paragraph -->\n'
        f'\t\t<p><strong>Sitio web:</strong> {negocio.web}</p>\n'
        '\t<!-- /wp:paragraph -->\n'

        '\t<!-- wp:shortcode -->\n'
        '\t\t[adinserter name="anuncio_manual"]\n'
        '\t<!-- /wp:shortcode -->\n'

        '\t<!-- wp:buttons -->\n'
        '\t<div class="wp-block-buttons"><!-- wp:button {"width":100,"className":"is-style-fill","style":{"border":{"radius":"15px"}},"fontSize":"medium"} -->\n'
        f'\t\t<div class="wp-block-button has-custom-width wp-block-button__width-100 is-style-fill"><a class="wp-block-button__link has-medium-font-size has-custom-font-size wp-element-button" href="tel:{negocio.telefono}" style="border-radius:15px">Llamar ahora</a></div>\n'
        '\t<!-- /wp:button -->\n'

        '\t<!-- wp:button {"width":100,"className":"is-style-fill","style":{"border":{"radius":"15px"}},"fontSize":"medium"} -->\n'
        f'\t\t<div class="wp-block-button has-custom-width wp-block-button__width-100 is-style-fill"><a class="wp-block-button__link has-medium-font-size has-custom-font-size wp-element-button" href="{negocio.web}" style="border-radius:15px" rel="">Visitar sitio web</a></div>\n'
        '\t<!-- /wp:button --></div>\n'
        '\t<!-- /wp:buttons -->\n'

        '\t<!-- wp:paragraph -->\n'
        f'\t\t<p>{negocio.texto}</p>\n'
        '\t<!-- /wp:paragraph -->\n'

        '\t<!-- wp:heading {"textAlign":"center"} -->\n'
        '\t\t<h2 class="wp-block-heading has-text-align-center">Horario</h2>\n'
        '\t\t<!-- /wp:heading -->\n'

        '\t<!-- wp:html -->\n'
        f'\t\t[su_list icon="icon: clock-o" icon_color="#7B2C2C" indent="15" class="lista-bloque"]\n{negocio.horario}\n'
		'\t\t[/su_list]\n'
        '\t<!-- /wp:html --></div>\n'
        '\t<!-- /wp:column -->\n'

        '\t<!-- wp:column {"className":"contenedor"} -->\n'
        '\t\t<div class="wp-block-column contenedor"><!-- wp:heading {"textAlign":"center"} -->\n'
        '\t\t\t<h2 class="wp-block-heading has-text-align-center">Localización</h2>\n'
        '\t\t<!-- /wp:heading -->\n'

        '\t<!-- wp:html -->\n'
        f'\t\t<iframe src="{negocio.mapa}" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>\n'
        '\t<!-- /wp:html -->\n'

        '\t<!-- wp:heading {"textAlign":"center"} -->\n'
        '\t\t<h2 class="wp-block-heading has-text-align-center">Fotografía</h2>\n'
        '\t<!-- /wp:heading -->\n'

        '\t\t<!-- wp:image {"sizeSlug":"large","align":"center","className":"is-style-default"} -->\n'
        f'\t\t\t<figure class="wp-block-image aligncenter size-large is-style-default"><img src="{negocio.foto}" alt=""/></figure>\n'
        '\t\t<!-- /wp:image --></div>\n'
        '\t<!-- /wp:column --></div>\n'
        '\t<!-- /wp:columns -->\n'

        '<!-- wp:shortcode -->\n'
        '\t[site_reviews_summary assigned_posts="post_id" schema="true" class="contenedor"]\n'
        '\t<!-- /wp:shortcode -->\n'

        '<!-- wp:buttons {"layout":{"type":"flex","justifyContent":"center"}} -->\n'
        '\t<div class="wp-block-buttons"><!-- wp:button {"textAlign":"center","style":{"border":{"radius":"15px"}},"fontSize":"medium"} -->\n'
        '\t\t<div class="wp-block-button"><a class="wp-block-button__link has-medium-font-size has-text-align-center has-custom-font-size wp-element-button" href="#formulario_resenya" style="border-radius:15px">DEJA UNA RESEÑA AHORA</a></div>\n'
        '\t<!-- /wp:button --></div>\n'
        '<!-- /wp:buttons -->\n'

        '<!-- wp:group {"className":"contenedor","layout":{"type":"constrained"}} -->\n'
        '\t<div class="wp-block-group contenedor"><!-- wp:heading {"textAlign":"center"} -->\n'
        '\t\t<h2 class="wp-block-heading has-text-align-center">Información</h2>\n'
        '\t<!-- /wp:heading -->\n'

        '<!-- wp:paragraph -->\n'
        '\t<p>Información del negocio</p>\n'
        '\t<!-- /wp:paragraph --></div>\n'
        '<!-- /wp:group -->\n'

        '<!-- wp:group {"className":"contenedor","layout":{"type":"constrained"}} -->\n'
        '<div class="wp-block-group contenedor"><!-- wp:heading {"textAlign":"center"} -->\n'
        '<h2 class="wp-block-heading has-text-align-center">¿Qué opinan los usuarios de negocio?</h2>\n'
        '<!-- /wp:heading -->\n'

        '<!-- wp:paragraph -->\n'
        '\t<p>A continuación, te dejamos un listado con las opiniones más destacadas que otros usuarios han dejado al negocio de localidad, provincia.</p>\n'
        '<!-- /wp:paragraph --></div>\n'
        '<!-- /wp:group -->\n'

        '<!-- wp:group {"className":"contenedor","layout":{"type":"constrained"}} -->\n'
        '\t<div class="wp-block-group contenedor"><!-- wp:heading -->\n'
        '\t\t<h2 class="wp-block-heading">Escribe tu reseña</h2>\n'
        '\t<!-- /wp:heading -->\n'

        '<!-- wp:shortcode /-->\n'

        '<!-- wp:shortcode -->\n'
        '\t[site_reviews_form assigned_posts="post_id"  class="contenedor" id="formulario_resenya"]\n'
        '\t\t<!-- /wp:shortcode --></div>\n'
        '\t<!-- /wp:group -->  \n'

        '<!-- wp:group {"layout":{"type":"constrained"}} -->\n'
        '\t<div class="wp-block-group"><!-- wp:heading {"textAlign":"center"} -->\n'
        f'\t\t<h2 class="wp-block-heading has-text-align-center">Otras creperías de {negocio.municipio}</h2>\n'
        '\t<!-- /wp:heading -->\n'

        f'<!-- wp:dpt/display-post-types {{"taxonomy":"category","terms":[{negocio.municipio}],"number":3,"styles":"dpt-slider1","imgAspect":"land1"}} /--></div>\n'
        '<!-- /wp:group -->\n'
        '<script>\n'
        '\t{\n'
        '\t"@context": "https://schema.org",\n'
        '\t"@type": "Restaurant",\n'
        f'\t"name": "{negocio.nombre}",\n'
        f'\t"image": "{negocio.foto}",\n'
        '\t"servesCuisine": "Creperie",\n'
        '\t"address": {\n'
        '\t\t"@type": "PostalAddress",\n'
        f'\t\t"streetAddress": "{negocio.direccion}",\n'
        f'\t\t"addressLocality": "{negocio.municipio}",\n'
        f'\t\t"addressRegion": "{negocio.provincia}",\n'
        '\t\t"addressCountry": "ES"\n'
        '\t},\n'
        f'\t"telephone": "{negocio.telefono}",\n'
        '\t"openingHours": [\n'
        f'\t\t"Mo 09:00-23:00",\n'
        f'\t\t"Tu 09:00-23:00",\n'
        f'\t\t"We 09:00-23:00",\n'
        f'\t\t"Th 09:00-23:00",\n'
        f'\t\t"Fr 09:00-23:00",\n'
        f'\t\t"Sa 10:00-00:00",\n'
        f'\t\t"Su 10:00-00:00"\n'
        '\t]\n'
    
  "url": "https://midominio.com/valladolid/creperia-la-dulce/",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.5",
    "reviewCount": "127"
  },
  "sameAs": [
    "https://www.facebook.com/creperialadulce",
    "https://www.instagram.com/creperialadulce"
  ]
}
'''
    )
    return res



