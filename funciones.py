import html
from funciones_excel import *
from ficheros_datos.constantes_configuracion import *
from negocio import *
from funciones_generar_texto import *
from ficheros_datos.keywords import *
from crea_elementos_web import *
from funciones_schema import *



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
        bloque += f'[su_list icon="icon: map-marker" icon_color="{color_contrast}" indent="40" class="lista-bloque"]'
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
            
                    <div class="wp-block-buttons">
                    <div class="wp-block-button has-custom-width wp-block-button__width-100 is-style-fill">
                        <a class="wp-block-button__link has-base-3-color has-accent-background-color has-text-color has-background has-link-color wp-element-button"
                        href="tel:{telefono}" style="border-radius:15px">
                        ¡Llama ahora!
                        </a>
                    </div>
                    </div>        
                
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
            return categoria['Id']
    return 0



def crea_schema_negocio(negocio):
    res=(
        '<script type="application/ld+json">\n'
        '\t{\n'
        '\t"@context": "https://schema.org",\n'
        )
    res+=obten_datos_schema_negocio(negocio)
    res+='\t}\n'
    res+='</script>\n'
    
    return res

def obten_datos_schema_negocio(negocio):
    res=(
        f'\t"@type": "{tipo_negocio_schema}",\n'
        f'\t"name": "{negocio.nombre}",\n'
    )
    if negocio.imagen!=None:
        res+=f'\t"image": "{negocio.imagen}",\n'

    res+=(
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
    if negocio.web!=None:
        res+=f'\t"url": "{negocio.web}"\n'
    return res

def crear_schema_municipio(municipio):
    negocios=obten_lista_negocios_municipio(excel_datos,municipio)
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
            f'\t\t"position": {i+1},\n'
            '\t\t"item": {\n'
        )
        schema_negocio+=obten_datos_schema_negocio(negocios[i])
        schema_negocio+='\t\t\t}\n'
        schema_negocio+='\t\t}\n'
        schema_negocio+='\t}\n'




def crea_provincia(provincia,imagen):


    parrafos=extraer_parrafos(obten_texto_cuerpo_provincia(provincia))
    res=crea_migas_provincia(provincia)

    res+=(
        f'<!-- wp:media-text {{"mediaPosition":"right","mediaId":{imagen.get_id()},"mediaLink":"{dominio}/localidad/ciudad/#main","mediaType":"image"}} -->\n'
        '<div class="wp-block-media-text has-media-on-the-right is-stacked-on-mobile"><div class="wp-block-media-text__content">\n'
        f'\t\t{crea_parrafo(parrafos[0])}\n'
        '\t</div>\n'
        f'<figure class="wp-block-media-text__media"><img src="{imagen.get_url()}" alt="" class="wp-image-{imagen.get_id()} size-full"/></figure></div>\n'
        '<!-- /wp:media-text -->\n'
    )   
    for i in range(1,len(parrafos)-1)         :
        res+=f'\t\t{crea_parrafo(parrafos[i])}\n'
        i+=1

    res+=(     
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
    res=crea_migas_ciudad(ciudad,provincia)

    res+=(   
        f'<!-- wp:media-text {{"mediaPosition":"right","mediaId":{imagen.get_id()},"mediaLink":"{dominio}/localidad/ciudad/#main","mediaType":"image"}} -->\n'
        '\t<div class="wp-block-media-text has-media-on-the-right is-stacked-on-mobile">\n'
        '\t\t<div class="wp-block-media-text__content">\n'
        '\t\t\t<!-- wp:paragraph -->\n'
        f'\t\t\t\t<p>{obten_texto_cuerpo_localidad(ciudad)}</p>\n'
        '\t\t\t<!-- /wp:paragraph -->\n'
        '\t\t</div>\n'
        '\t\t<figure class="wp-block-media-text__media">\n'
        f'\t\t\t<img src="{imagen.get_url()}" alt="Panorámica de {ciudad}" class="wp-image-{imagen.get_id()} size-full"/>\n'
        '\t\t</figure>\t</div>\n'
        '<!-- /wp:media-text -->\n'
        f'{crea_texto_ciudad(ciudad)}'
        '<!-- wp:group {"layout":{"type":"constrained"}} -->\n'
        '\t<div class="wp-block-group">\n'
        '\t\t<!-- wp:heading {"textAlign":"center"} -->\n'
        f'\t\t\t<h2 class="wp-block-heading has-text-align-center">Todas las {tipo_negocio} de {ciudad}</h2>\n'
        '\t\t<!-- /wp:heading -->\n'
        f'\t<!-- wp:dpt/display-post-types {{"taxonomy":"category","terms":["{ciudad}"],"number":100,"styleSup":["title"],"showPgnation":true}} /--></div>\n'

        '<!-- /wp:group -->'
        f'{imprime_lista_negocios(obten_lista_negocios_municipio(excel_empresas,ciudad))}'
        '<script type="application/ld+json">\n'
        f'{crea_schema_municipio(ciudad)}'
        '</script>\n'
      )
    
    


    return res

def crea_negocio(negocio):
    res=crea_migas_negocio(negocio) 
    '''res=('<!-- wp:html -->\n'
        '\t<div class="migas">\n'
        f'\t\t<p><a href="{dominio}">Inicio</a> &gt; <a href="{dominio}/{sluguiza("Provincia de "+negocio.provincia)}">{negocio.provincia}</a> &gt; <a href="{dominio}/{sluguiza(negocio.ciudad)}">{negocio.ciudad}</a> &gt; {negocio.nombre}</p>'
        '\t</div>\n'
        '<!-- /wp:html -->\n'
    )'''
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
