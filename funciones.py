import html
from extraer_datos_excel import *
from ficheros_datos.constantes_configuracion import *
from random import randint
from negocio import *
from funciones_generar_texto import *
from ficheros_datos.keywords import *
from crea_elementos_web import *

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



def imprime_lista_negocios(lista_negocios):
    res = ""
    for negocio in lista_negocios:
        # Escapamos valores para seguridad
        nombre = html.escape(str(negocio.nombre))
        direccion = html.escape(str(negocio.direccion))
        telefono = html.escape(str(negocio.telefono))
        web = html.escape(str(negocio.web)) if negocio.web else None
        mapa = html.escape(str(negocio.mapa))
        #horario_html = negocio.obten_horario_html()  # devuelve HTML, no escapamos

        bloque = f"""
            <!-- wp:html -->
            [su_box title="{nombre}" box_color="{color_contrast}" title_color="{color_contrast3}" radius="6"]
            [su_row]
                [su_column size="1/2" center="no"]
            
                [su_list icon="icon: clock-o" icon_color="{color_contrast}" indent="40" class="lista-bloque"]
                    <ul>
                        <li>Horario\n
                
                """
                
        bloque+=negocio.obten_horario_lista_html()
        bloque += "[/su_list]\n"
        bloque += f'[su_list icon="icon: envelope" icon_color="{color_contrast}" indent="40" class="lista-bloque"]'
        bloque+=f"<ul>\n<li>Dirección: {direccion}</li>\n</ul>\n[/su_list]"
        if web:
            bloque +=f'[su_list icon="icon: dribbble" icon_color="{color_contrast}" indent="40" class="lista-bloque"]'
            bloque+=f'<ul>\n<li>Web: <a href="{web}">{web}</a></li>\n</ul>\n[/su_list]\n'
                    
            
        bloque += f"""
                [su_list icon="icon: phone" icon_color="{color_contrast}" indent="40" class="lista-bloque"]
                    <ul>
                    <li>Teléfono: <a href="tel:{telefono}">{telefono}</a></li>
                    </ul>
                [/su_list]
            
                [/su_column]
                [su_column size="1/2" center="no"]
            
                <iframe src="{mapa}"
                        width="600"
                        height="450"
                        style="border:1px solid {color_contrast}; box-shadow: 0 2px 8px rgba(0,0,0,0.08);"
                        allowfullscreen
                        loading="lazy"
                        referrerpolicy="no-referrer-when-downgrade"></iframe>
            
                [/su_column]
            [/su_row]
            
            [su_row]
                [su_column size="1/1" center="yes"]
            
                <!-- wp:buttons -->
                    <div class="wp-block-buttons">
                    <div class="wp-block-button has-custom-width wp-block-button__width-100 is-style-fill">
                        <a class="wp-block-button__link has-base-3-color has-accent-background-color has-text-color has-background has-link-color wp-element-button"
                        href="tel:{telefono}" style="border-radius:15px">
                        ¡Llama ahora!
                        </a>
                    </div>
                    </div>
                <!-- /wp:buttons -->
            
                [/su_column]
            [/su_row]
            [/su_box]
            <br>
            <!-- /wp:html -->
            """
        res += bloque
    return res


def obten_nombre_provincia(imagen):
   return imagen.split(".")[0]

def obten_nombre_municipio(imagen):
   return imagen.split("_")[0]

def obten_nombre_provincia_municipio(imagen):
    aux=imagen.split("_")[1]
    return aux.split(".")[0]



def obten_id_categoria_provincia(provincia,lista_categorias):
    for categoria in lista_categorias:
        if categoria.get('Nombre')==provincia:
            print("encontrada")
            return categoria['Id']
    return 0


def crea_schema_negocio(negocio):
    res=(
        '<script type="application/ld+json">\n'
        '\t{\n'
        '\t"@context": "https://schema.org",\n'
        )
    res+=obten_datos_chema_negocio(negocio)
    res+='\t}\n'
    res+='</script>\n'
    
    return res

def obten_datos_chema_negocio(negocio):
    res=(
        f'\t"@type": "{tipo_negocio_schema}",\n'
        f'\t"name": "{negocio.nombre}",\n'
        f'\t"image": "{negocio.imagen}",\n'
        '\t"address": {\n'
        '\t\t"@type": "PostalAddress",\n'
        f'\t\t"streetAddress": "{negocio.direccion}",\n'
        f'\t\t"addressLocality": "{negocio.ciudad}",\n'
        f'\t\t"addressRegion": "{negocio.provincia}",\n'
        '\t\t"addressCountry": "ES"\n'
        '\t\t},\n'
        f'\t"telephone": "{negocio.telefono}",\n'
        )
    res+=f'{negocio.obten_horario_schema()}'
    res+=f'\t"url": "{negocio.web}"\n'
    return res

def crear_schema_municipio(municipio):
    negocios=obten_lista_negocios_municipio(excel_datos,municipio)
    print(f"Lista de negocios de {municipio}")
    print(negocios)
    res=(
        '{\n'
        '\t"@context": "https://schema.org",\n'
        '\t"@type": "ItemList",\n'
        f'\t\t"name": "Mejores {tipo_negocio.lower()} en {municipio}",\n'
        f'\t"description": "Directorio de {tipo_negocio.lower()} recomendadas en {municipio}",\n'
        '\t"itemListElement": [\n'
        )
    i=0
    while i<len(negocios):
        schema_negocio=(
            '{\t\t\n'
            '\t\t"@type": "ListItem",\n'
            f'\t\t"position": {i},\n'
            '\t\t"item": {\n'
        )
        schema_negocio+=obten_datos_chema_negocio(negocios[i])
        schema_negocio+='\t\t\t}\n'
        schema_negocio+='\t\t}\n'
        schema_negocio+='\t}\n'

        if i<len(negocios)-1:
          schema_negocio+=","
        i+=1  
        res+=schema_negocio
    res+=']\n}\n'

        
    return res


def crea_provincia(provincia,imagen):

    res=('<!-- wp:html -->\n'
        '\t<div class="migas">\n'
        f'\t\t<p><a href="{dominio}">Inicio</a> &gt; {provincia}</p>\n'
        '\t</div>\n'
        '<!-- /wp:html -->\n'
        f'{crea_heading(f"{tipo_negocio} en la provincia de {provincia}",1)}'

        f'<!-- wp:media-text {{"mediaPosition":"right","mediaId":{imagen.get_id()},"mediaLink":"{dominio}/localidad/ciudad/#main","mediaType":"image"}} -->\n'
        '<div class="wp-block-media-text has-media-on-the-right is-stacked-on-mobile"><div class="wp-block-media-text__content"><!-- wp:paragraph {"placeholder":"Contenido…"} -->\n'
        f'\t\t<p>{obten_texto_H1(provincia)}</p>\n'
        f'\t\t<!-- /wp:paragraph -->\n'
        '\t</div>\n'
        
        f'<figure class="wp-block-media-text__media"><img src="{imagen.get_url()}" alt="" class="wp-image-178 size-full"/></figure></div>\n'
        '<!-- /wp:media-text -->\n'
        f'{crea_heading(f"Encuentra las mejores {tipo_negocio.lower()} en {provincia}",2)}'
        f'{crea_parrafo(obten_texto_H2_general("H2_transaccional.txt",keywords_transaccionales,provincia))}'
        f'{crea_heading(f"Guía para {tipo_negocio.lower()} en {provincia}",2)}'
        f'{crea_parrafo(obten_texto_H2_general('H2_informacional.txt',keywords_informacionales,provincia))}'
        f'{crea_heading(f"Tipos de maquinaria disponible en {provincia}",2)}'
        f'{crea_parrafo(obten_texto_H2_general('H2_tipo_maquinaria.txt',keywords_tipo_maquinaria,provincia))}'
        f'{crea_heading(f"Maquinaria especializada según tu tipo de proyecto en {provincia}",2)}'
        f'{crea_parrafo(obten_texto_H2_general('H2_proyecto_sector.txt',keywords_proyecto_sector,provincia))}'
        f'{crea_heading(f"Alquiler flexible de maquinaria y servicios urgentes en {provincia}",2)}'
        f'{crea_parrafo(obten_texto_H2_general('H2_urgencia_flexibilidad.txt',keywords_urgencia_flexibilidad,provincia))}'

        '<!-- wp:group {"layout":{"type":"constrained"}} -->\n'
        '\t<div class="wp-block-group">\n'
        '\t\t<!-- wp:heading {"textAlign":"center"} -->\n'
        f'\t\t\t<h2 class="wp-block-heading has-text-align-center">Todas las {tipo_negocio} de {provincia} ordenadas por nombre de municipio</h2>\n'
        '\t\t<!-- /wp:heading -->\n'
        f'\t\t<!-- wp:dpt/display-post-types {{"taxonomy":"category","terms":["Provincia de {provincia}"],"number":100,"styleSup":["title"],"showPgnation":true}} /-->\n'
        '\t</div>\n'
        '\t<!-- /wp:group -->\n')
    return res

def crea_ciudad(ciudad,provincia,imagen):
    res=('<!-- wp:html -->\n'
        '\t<div class="migas">\n'
        f'\t\t<p><a href="{dominio}">Inicio</a> &gt; <a href="{dominio}/{sluguiza("Provincia de "+provincia)}">{provincia}</a> &gt; {ciudad}</p>'
        '\t</div>\n'
        '<!-- /wp:html -->'
        f'<!-- wp:media-text {{"mediaPosition":"right","mediaId":{imagen.get_id()},"mediaLink":"{dominio}/localidad/ciudad/#main","mediaType":"image"}} -->\n'
        '<div class="wp-block-media-text has-media-on-the-right is-stacked-on-mobile"><div class="wp-block-media-text__content"><!-- wp:paragraph {"placeholder":"Contenido…"} -->\n'
        f'\t\t<p>{obten_texto_H1(ciudad)}</p>\n'
        f'<!-- /wp:paragraph --></div><figure class="wp-block-media-text__media"><img src="{imagen.get_url()}" alt="" class="wp-image-{imagen.get_id()} size-full"/></figure></div>\n'
        '<!-- /wp:media-text -->\n'
        f'{crea_texto_ciudad(ciudad)}'
        f'{crea_texto_ciudad(ciudad)}'
        '<!-- wp:group {"layout":{"type":"constrained"}} -->\n'
        '\t<div class="wp-block-group">\n'
        '\t\t<!-- wp:heading {"textAlign":"center"} -->\n'
        f'\t\t\t<h2 class="wp-block-heading has-text-align-center">Todas las creperias de {ciudad}</h2>\n'
        '\t\t<!-- /wp:heading -->\n'
        f'\t<!-- wp:dpt/display-post-types {{"taxonomy":"category","terms":["{ciudad}"],"number":100,"styleSup":["title"],"showPgnation":true}} /--></div>\n'

        '<!-- /wp:group -->'
        '<div>'
        f'{imprime_lista_negocios(obten_lista_negocios_municipio(excel_datos,ciudad))}'
        '<script type="application/ld+json">\n'
        f'{crear_schema_municipio(ciudad)}'
        '</script>\n'
      )
    
    


    return res

def crea_negocio_temp(negocio):
    res=('<!-- wp:html -->\n'
        '\t<div class="migas">\n'
        f'\t\t<p><a href="{dominio}">Inicio</a> &gt; <a href="{dominio}/{sluguiza("Provincia de "+negocio.provincia)}">{negocio.provincia}</a> &gt; <a href="{dominio}/{sluguiza(negocio.ciudad)}">{negocio.ciudad}</a> &gt; {negocio.nombre}</p>'
        '\t</div>\n'
        '<!-- /wp:html -->\n'
    )
    res+=crea_bloque_contacto(negocio)
    res+=crea_bloque_horario(negocio)       
    if negocio.mapa!=None:
        res+=crea_bloque_mapa(negocio)
    if negocio.imagen!=None:                                    
        res+=crea_bloque_imagen(negocio)
    res+=crea_bloque_reviews(negocio)
    res+=crea_bloque_descripcion_seo(negocio)

    res+=crea_bloque_otros_negocios(negocio)
   
    res+=crea_schema_negocio(negocio)
        
    
    return res

def nuevo_crea_negocio(negocio):
    res=('<!-- wp:html -->\n'
        '\t<div class="migas">\n'
        f'\t\t<p><a href="{dominio}">Inicio</a> &gt; <a href="{dominio}/{sluguiza("Provincia de "+negocio.provincia)}">{negocio.provincia}</a> &gt; <a href="{dominio}/{sluguiza(negocio.ciudad)}">{negocio.ciudad}</a> &gt; {negocio.nombre}</p>'
        '\t</div>\n'
        '<!-- /wp:html -->\n'
        '<!-- wp:columns -->\n'
        '<div class="wp-block-columns"><!-- wp:column {"className":"contenedor"} -->\n'
        '\t<div class="wp-block-column contenedor">'



        f'{crea_heading("Datos de contacto",2)}'    
        f'{crea_lista_direccion(negocio.direccion)}'
        f'{crea_lista_telefono(negocio.telefono)}'
        f'{crea_lista_web(negocio.web)}'

        '\t<!-- wp:shortcode -->\n'
        '\t\t[adinserter name="anuncio_manual"]\n'
        '\t<!-- /wp:shortcode -->\n'
        f'{crea_botones_datos_contacto(negocio.telefono,negocio.web)}'
        f'{crea_parrafo(negocio.descripcion_seo)}'
        f'{crea_heading("Horario",2)}'
        f'{crea_lista_horario(negocio.horario)}'    
        '\t<!-- /wp:column -->\n'

        '\t<!-- wp:column {"className":"contenedor"} -->\n'
        '\t\t<div class="wp-block-column contenedor">'

        f'{crea_heading("Localización",2)}'

        '\t<!-- wp:html -->\n'
        
        f'\t\t<iframe src="{negocio.mapa}" width="600" height="450"  style="border:2px solid {color_contrast}; box-shadow: 0 2px 8px rgba(0,0,0,0.08); border-radius: 12px;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>\n'
        '\t<!-- /wp:html -->\n'

        '\t<!-- wp:heading {"textAlign":"center"} -->\n'
        '\t\t<h2 class="wp-block-heading has-text-align-center">Fotografía</h2>\n'
        '\t<!-- /wp:heading -->\n'

        '\t\t<!-- wp:image {"sizeSlug":"large","align":"center","className":"is-style-default"} -->\n'
        f'\t\t\t<figure class="wp-block-image aligncenter size-large is-style-default"><img src="{negocio.imagen}" alt=""/></figure>\n'
        '\t\t<!-- /wp:image --></div>\n'
        '\t<!-- /wp:column --></div>\n'
        '\t<!-- /wp:columns -->\n'

        '<!-- wp:shortcode -->\n'
        '\t[site_reviews_summary assigned_posts="post_id" schema="true" class="contenedor"]\n'
        '\t<!-- /wp:shortcode -->\n'

        '<!-- wp:buttons {"layout":{"type":"flex","justifyContent":"center"}} -->\n'
        #'\t<div class="wp-block-buttons"><!-- wp:button {"textAlign":"center","style":{"border":{"radius":"15px"}},"fontSize":"medium"} -->\n'
        #'\t\t<div class="wp-block-button"><a class="wp-block-button__link has-medium-font-size has-text-align-center has-custom-font-size wp-element-button" href="#formulario_resenya" style="border-radius:15px">DEJA UNA RESEÑA AHORA</a></div>\n'
        '\t\t<div class="wp-block-buttons"><!-- wp:button {"backgroundColor":"base-3","textColor":"accent","width":100,"className":"is-style-fill","style":{"elements":{"link":{"color":{"text":"var:preset|color|contrast-3"}}},"border":{"radius":"10px"}},"fontSize":"medium"} -->\n'
        f'\t\t<div class="wp-block-button has-custom-width wp-block-button__width-100 is-style-fill"><a class="wp-block-button__link has-contrast-3-color has-contrast-2-background-color has-text-color has-background has-link-color has-medium-font-size has-custom-font-size wp-element-button" href="#formulario_resenya" style="border-radius:15px">¡DEJA UNA RESEÑA AHORA!</a></div>\n'
        '\t\t<!-- /wp:button -->\n'
        
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
        f'\t\t<h2 class="wp-block-heading has-text-align-center">Otras creperías de {negocio.ciudad}</h2>\n'
        '\t<!-- /wp:heading -->\n'

        f'<!-- wp:dpt/display-post-types {{"taxonomy":"category","terms":[{negocio.ciudad}],"number":3,"styles":"dpt-slider1","imgAspect":"land1"}} /--></div>\n'
        '<!-- /wp:group -->\n'
        
        '<script type="application/ld+json">\n'
        f'{crea_schema_negocio(negocio)}'
        '</script>\n'
        '<!-- /wp:html -->\n'
    )
   
    return res
    
def crea_negocio(negocio):
    print(negocio.nombre)
    res=('<!-- wp:html -->\n'
        '\t<div class="migas">\n'
        f'\t\t<p><a href="{dominio}">Inicio</a> &gt; <a href="{dominio}/{sluguiza("Provincia de "+negocio.provincia)}">{negocio.provincia}</a> &gt; <a href="{dominio}/{sluguiza(negocio.ciudad)}">{negocio.ciudad}</a> &gt; {negocio.nombre}</p>'
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
        f'{crea_lista_direccion(negocio.direccion)}'
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

        '\t\t<div class="wp-block-buttons"><!-- wp:button {"backgroundColor":"base-3","textColor":"accent","width":100,"className":"is-style-fill","style":{"elements":{"link":{"color":{"text":"var:preset|color|contrast-3"}}},"border":{"radius":"10px"}},"fontSize":"medium"} -->\n'
        f'\t\t<div class="wp-block-button has-custom-width wp-block-button__width-100 is-style-fill"><a class="wp-block-button__link has-contrast-3-color has-contrast-2-background-color has-text-color has-background has-link-color has-medium-font-size has-custom-font-size wp-element-button" href="{negocio.telefono}" style="border-radius:15px">¡Llama ahora!</a></div>\n'
        '\t\t<!-- /wp:button -->\n'

        '\t\t<div class="wp-block-buttons"><!-- wp:button {"backgroundColor":"base-3","textColor":"accent","width":100,"className":"is-style-fill","style":{"elements":{"link":{"color":{"text":"var:preset|color|contrast-3"}}},"border":{"radius":"10px"}},"fontSize":"medium"} -->\n'
        f'\t\t<div class="wp-block-button has-custom-width wp-block-button__width-100 is-style-fill"><a class="wp-block-button__link has-contrast-3-color has-contrast-2-background-color has-text-color has-background has-link-color has-medium-font-size has-custom-font-size wp-element-button" href="{negocio.web}" style="border-radius:15px">Visita web</a></div>\n'
        '\t\t<!-- /wp:button -->\n'

        '\t<!-- /wp:buttons -->\n'

        '\t<!-- wp:paragraph -->\n'
        f'\t\t<p>{negocio.descripcion_seo}</p>\n'
        '\t<!-- /wp:paragraph -->\n'

        '\t<!-- wp:heading {"textAlign":"center"} -->\n'
        '\t\t<h2 class="wp-block-heading has-text-align-center">Horario</h2>\n'
        '\t\t<!-- /wp:heading -->\n'

        '\t<!-- wp:html -->\n'
        f'\t\t[su_list icon="icon: clock-o" icon_color="{color_contrast}" indent="15" class="lista-bloque"]\n{negocio.horario}\n'
		    '\t\t[/su_list]\n'
        '\t<!-- /wp:html --></div>\n'
        '\t<!-- /wp:column -->\n'

        '\t<!-- wp:column {"className":"contenedor"} -->\n'
        '\t\t<div class="wp-block-column contenedor"><!-- wp:heading {"textAlign":"center"} -->\n'
        '\t\t\t<h2 class="wp-block-heading has-text-align-center">Localización</h2>\n'
        '\t\t<!-- /wp:heading -->\n'

        '\t<!-- wp:html -->\n'
        
        f'\t\t<iframe src="{negocio.mapa}" width="600" height="450"  style="border:2px solid {color_contrast}; box-shadow: 0 2px 8px rgba(0,0,0,0.08); border-radius: 12px;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>\n'
        '\t<!-- /wp:html -->\n'

        '\t<!-- wp:heading {"textAlign":"center"} -->\n'
        '\t\t<h2 class="wp-block-heading has-text-align-center">Fotografía</h2>\n'
        '\t<!-- /wp:heading -->\n'

        '\t\t<!-- wp:image {"sizeSlug":"large","align":"center","className":"is-style-default"} -->\n'
        f'\t\t\t<figure class="wp-block-image aligncenter size-large is-style-default"><img src="{negocio.imagen}" alt=""/></figure>\n'
        '\t\t<!-- /wp:image --></div>\n'
        '\t<!-- /wp:column --></div>\n'
        '\t<!-- /wp:columns -->\n'

        '<!-- wp:shortcode -->\n'
        '\t[site_reviews_summary assigned_posts="post_id" schema="true" class="contenedor"]\n'
        '\t<!-- /wp:shortcode -->\n'

        '<!-- wp:buttons {"layout":{"type":"flex","justifyContent":"center"}} -->\n'
        #'\t<div class="wp-block-buttons"><!-- wp:button {"textAlign":"center","style":{"border":{"radius":"15px"}},"fontSize":"medium"} -->\n'
        #'\t\t<div class="wp-block-button"><a class="wp-block-button__link has-medium-font-size has-text-align-center has-custom-font-size wp-element-button" href="#formulario_resenya" style="border-radius:15px">DEJA UNA RESEÑA AHORA</a></div>\n'
        '\t\t<div class="wp-block-buttons"><!-- wp:button {"backgroundColor":"base-3","textColor":"accent","width":100,"className":"is-style-fill","style":{"elements":{"link":{"color":{"text":"var:preset|color|contrast-3"}}},"border":{"radius":"10px"}},"fontSize":"medium"} -->\n'
        f'\t\t<div class="wp-block-button has-custom-width wp-block-button__width-100 is-style-fill"><a class="wp-block-button__link has-contrast-3-color has-contrast-2-background-color has-text-color has-background has-link-color has-medium-font-size has-custom-font-size wp-element-button" href="#formulario_resenya" style="border-radius:15px">¡DEJA UNA RESEÑA AHORA!</a></div>\n'
        '\t\t<!-- /wp:button -->\n'
        
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
        f'\t\t<h2 class="wp-block-heading has-text-align-center">Otras creperías de {negocio.ciudad}</h2>\n'
        '\t<!-- /wp:heading -->\n'

        f'<!-- wp:dpt/display-post-types {{"taxonomy":"category","terms":[{negocio.ciudad}],"number":3,"styles":"dpt-slider1","imgAspect":"land1"}} /--></div>\n'
        '<!-- /wp:group -->\n'
        
        '<script type="application/ld+json">\n'
        f'{crea_schema_negocio(negocio)}'
        '</script>\n'
    )
   
    return res




