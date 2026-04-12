import html
from turtle import width
from funciones_excel import *
from ficheros_datos.constantes_configuracion import *
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

                    <div class="map-wrapper">
                        <iframe src="{mapa}"
                                width="600"
                                height="450"
                                style="border:1px solid {color_contrast}; box-shadow: 0 2px 8px rgba(0,0,0,0.08);"
                                allowfullscreen
                                loading="lazy"
                                referrerpolicy="no-referrer-when-downgrade">
                        </iframe>
                    </div>
                    
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

def crear_schema_localidad(localidad):
    negocios=obten_lista_negocios_municipio(excel_datos,localidad)
    res=(
        '{\n'
        '\t"@context": "https://schema.org",\n'
        '\t"@type": "ItemList",\n'
        f'\t\t"name": "Mejores {tipo_negocio.lower()} en {localidad}",\n'
        f'\t"description": "Directorio de {tipo_negocio.lower()} recomendadas en {localidad}",\n'
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
    aux=dividir_parrafo(parrafos[0])
    primero=aux[0]
    segundo=aux[1]
    #crea_estilos()
    res=crea_migas_provincia(provincia)


    res+=(
        '<div class="bloque-intro-imagen">\n'
        f'<!-- wp:media-text {{"mediaPosition":"right","mediaId":{imagen.get_id()},"mediaType":"image"}} -->\n'
	    '\t\t<div class="wp-block-media-text has-media-on-the-right is-stacked-on-mobile">\n'
		'\t\t\t<div class="wp-block-media-text__content">\n'
			f'\t\t\t\t<span class="badge-intro">{tipo_negocio}</span>\n'
            f'\t\t\t\t<h2>Directorio de {tipo_negocio} en la provincia de {provincia}</h2>'
            f'\t\t\t\t{crea_parrafo(primero)}\n'
            f'\t\t\t\t{crea_parrafo(segundo)}\n'
			'\t\t\t\t<a class="intro-cta" href="#empresas">Ver empresas destacadas</a>\n'
		'\t\t\t</div>\n'
		'\t\t\t<figure class="wp-block-media-text__media">\n'
			f'\t\t\t\t<img src="{imagen.get_url()}" alt="Vista de {provincia} para el directorio de {tipo_negocio}" class="{imagen.get_id()} size-full"/>\n'
		'\t\t\t</figure>\n'
	'\t\t</div>\n'
	'\t<!-- /wp:media-text -->\n'
    '</div>\n'
    )


    res+=(
        '<div class="bloque-parrafo-normal">\n'
        f'\t<h3>Ventajas estratégicas en la provincia de {provincia}</h3>\n'
    )
    for i in range(1,len(parrafos)-1)         :
        res+=f'\t\t{crea_parrafo(parrafos[i])}\n'
        i+=1
    res+="</div>\n"
    res+=(     
        '<a id="#empresas">'
        '<!-- wp:group {"layout":{"type":"constrained"}} -->\n'
        '\t<div class="wp-block-group">\n'
        '\t\t<!-- wp:heading {"textAlign":"center"} -->\n'
        f'\t\t\t<h2 class="wp-block-heading has-text-align-center">Todas las {tipo_negocio} de {provincia} ordenadas por nombre de municipio</h2>\n'
        '\t\t<!-- /wp:heading -->\n'
        f'\t\t<!-- wp:dpt/display-post-types {{"taxonomy":"category","terms":["Provincia de {provincia}"],"number":100,"styleSup":["title"],"showPgnation":true}} /-->\n'
        '\t</div>\n'
        '\t<!-- /wp:group -->\n')
    return res

def crea_localidad(localidad,provincia,imagen):
    parrafos=extraer_parrafos(obten_texto_cuerpo_localidad(localidad))
    aux=dividir_parrafo(parrafos[0])
    primero=aux[0]
    segundo=aux[1]
    res=""
    res+=crea_migas_ciudad(localidad,provincia)

    res+=(   
        '<div class="bloque-intro-imagen">\n'
	    '\t<div class="wp-block-media-text has-media-on-the-right is-stacked-on-mobile">\n'
		'\t\t<div class="wp-block-media-text__content">\n'
		f'\t\t\t\t<span class="badge-intro">{tipo_negocio}</span>\n'
        f'\t\t\t\t<h2>Directorio de {tipo_negocio} en la provincia de {localidad}</h2>'
        f'\t\t\t{crea_parrafo(primero)}\n'
        f'\t\t\t{crea_parrafo(segundo)}\n'
		'\t\t\t<a class="intro-cta" href="#empresas">Ver empresas destacadas</a>\n'
		'\t\t</div>\n'
		'\t\t<figure class="wp-block-media-text__media">\n'
		f'\t\t\t<img src="{imagen.get_url()}" alt="Vista de {localidad} para el directorio de {tipo_negocio}" class="{imagen.get_id()} size-full"/>\n'
		'\t\t</figure>\n'
	    '\t</div>\n'
        '</div>\n'

        #f'<!-- wp:media-text {{"mediaPosition":"right","mediaId":{imagen.get_id()},"mediaLink":"{dominio}/localidad/ciudad/#main","mediaType":"image"}} -->\n'
        #'\t<div class="wp-block-media-text has-media-on-the-right is-stacked-on-mobile">\n'
        #'\t\t<div class="wp-block-media-text__content">\n'
     
        
        '<div class="bloque-parrafo-normal">\n'
        f'{crea_texto_ciudad(localidad)}'
        '</div>\n'

        #'\t\t</div>\n'
        #'\t\t<figure class="wp-block-media-text__media">\n'
        #f'\t\t\t<img src="{imagen.get_url()}" alt="Panorámica de {ciudad}" class="wp-image-{imagen.get_id()} size-full"/>\n'
        #'\t\t</figure>\t</div>\n'
        #'<!-- /wp:media-text -->\n'
        #'<div class="bloque-parrafo-normal">\n'
        #f'{crea_texto_ciudad(ciudad)}'
        #'</div>\n'

        '<!-- wp:group {"layout":{"type":"constrained"}} -->\n'
        '\t<div class="wp-block-group">\n'
        '\t\t<!-- wp:heading {"textAlign":"center"} -->\n'
        f'\t\t\t<h2 class="wp-block-heading has-text-align-center">Todas las {tipo_negocio} de {localidad}</h2>\n'
        '\t\t<!-- /wp:heading -->\n'
        f'\t<!-- wp:dpt/display-post-types {{"taxonomy":"category","terms":["{localidad}"],"number":100,"styleSup":["title"],"showPgnation":true}} /--></div>\n'

        '<!-- /wp:group -->'
        f'{imprime_lista_negocios(obten_lista_negocios_municipio(excel_empresas,localidad))}'
        '<script type="application/ld+json">\n'
        f'{crea_schema_municipio(localidad)}'
        '</script>\n'
        )
    
    


    return res

def crea_negocio(negocio):
    #res=crea_estilos()
    res+=crea_migas_negocio(negocio) 
    '''res=('<!-- wp:html -->\n'
        '\t<div class="migas">\n'
        f'\t\t<p><a href="{dominio}">Inicio</a> &gt; <a href="{dominio}/{sluguiza("Provincia de "+negocio.provincia)}">{negocio.provincia}</a> &gt; <a href="{dominio}/{sluguiza(negocio.ciudad)}">{negocio.ciudad}</a> &gt; {negocio.nombre}</p>'
        '\t</div>\n'
        '<!-- /wp:html -->\n'
    )'''
    res+=crea_bloque_contacto(negocio)
    if negocio.horario!=None:
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

def crea_estilos():
    fichero_css=open("./css/estilos.css","w")

    
    
    
    css=(
        "\t.lista-horario li {\n"
        "\t\tdisplay:flex;\n"
        "\t\tjustify-content:space-between;\n"
        "\t\tmax-width:320px;\n"
        f"\t\tgap:8px;\n"
        "\t}\n"
        
        "\t.map-wraper iframe {\n"
        "\t\twidth:100%;\n"
        "\t\tmax-width:100%;\n"
        "\t\theight:300px;\n"
        "\t\tborder-radius:12px;\n"
        "\t}\n"
        
        "@media (min-width:768px){\n"
        "\t.map-wraper iframe { height:400px; }\n"
        "}\n" \
        
        ".breadcrumb {\n"
        f"\tbackground-color: {color_base3};\n"
        "\tpadding:20px;\n"
        "\tborder-radius:8px;\n"
        "\tmargin-bottom:24px;\n"
        f"\tborder-left:4px solid {color_accent};\n"
        "\tmax-width:960px;\n"
        "\tmargin-inline:auto;\n"
        "}\n"
        "\n"
        
        ".breadcrumb ul {\n"
        "\tdisplay:flex;\n"
        "\tflex-wrap:wrap;\n"
        "\talign-items:center;\n"
        "\tlist-style:none;\n"
        "\tpadding:0;\n"
        "\tmargin:0;\n"
        "\tfont-size:16px;\n"
        "\tgap:10px;\n"
        "}\n"  
        
        ".breadcrumb a {\n"
        f"\tcolor: {color_base};\n"
        "\ttext-decoration:none;\n"
        "\tpadding:4px 10px;\n"
        "\tborder-radius:4px;\n"
        "\ttransition:background 0.2s, color 0.2s;\n"
        "}\n"

                
        ".breadcrumb a:hover {\n"
        f"\tbackground:{color_contrast3};\n"
        f"\tcolor:{color_contrast};\n"
        "}\n"


        ".breadcrumb-destacado{\n"
        f"\tcolor: {color_contrast};\n"
        "\tfont-weight: 600;\n"
        "\tpadding: 4px 12px;\n"
        f"\tbackground: {color_accent};\n"
        "\tborder-radius: 4px;\n"
        "}\n"

        ".breadcrumb-separador{\n"
        f"\tcolor: {color_contrast2};\n"
        "}\n"


        ".bloque-opiniones {\n"
        f"\tgap:20px;\n"
        "}\n"

        "@media (max-width:768px){\n"
        "\t.bloque-opiniones .su-column {\n"
        "\t\twidth:100% !important;\n"
        "\t\tmargin-bottom:16px;\n"
        "\t}\n"
        "}\n"
        
        "@media (min-width:769px){\n"
        "\t.bloque-opiniones .su-column {\n"
        "\t\twidth:50% !important;\n"
        "\t\tmax-width:50% !important;\n"
        "\t}\n"
        "}\n"

        
        ".bloque-intro-imagen {\n"
        "\tmax-width: 1100px;\n"
        "\tmargin: 48px auto;\n"
        "\tpadding: 32px;\n"
        f"\tbackground: {color_base3};\n"
        f"\tborder: 1px solid {color_contrast3};\n"
        "\tborder-radius: 20px;\n"
        "\tbox-shadow: 0 10px 30px rgba(31, 41, 55, 0.06);\n"
        "}\n"
        "\n"
        ".bloque-intro-imagen .wp-block-media-text {\n"
        "\tgap: 32px;\n"
        "\talign-items: center;\n"
        "}\n"
        "\n"
        ".bloque-intro-imagen .wp-block-media-text__content {\n"
        "\tpadding: 8px 0;\n"
        "}\n"
        "\n"
        ".badge-intro {\n"
        "\tdisplay: inline-block;\n"
        "\tpadding: 6px 14px;\n"
        "\tmargin-bottom: 16px;\n"
        "\tfont-size: 14px;\n"
        "\tfont-weight: 600;\n"
        f"\tcolor: {color_contrast};\n"
        f"\tbackground: {color_accent};\n"
        "\tborder-radius: 999px;\n"
        "}\n"
        "\n"
        ".bloque-intro-imagen h2 {\n"
        "\tmargin: 0 0 16px;\n"
        "\tfont-size: clamp(28px, 4vw, 40px);\n"
        "\tline-height: 1.1;\n"
        f"\tcolor: {color_contrast};\n"
        "}\n"
        "\n"
        ".bloque-intro-imagen p {\n"
        "\tmargin: 0 0 16px;\n"
        "\tfont-size: 17px;\n"
        "\tline-height: 1.75;\n"
        f"\tcolor: {color_base};\n"
        "}\n"
        "\n"
        ".bloque-intro-imagen .wp-block-media-text__media img {\n"
        "\twidth: 100%;\n"
        "\theight: 100%;\n"
        "\tobject-fit: cover;\n"
        "\tborder-radius: 18px;\n"
        "\tbox-shadow: 0 12px 30px rgba(31, 41, 55, 0.12);\n"
        f"\tborder: 1px solid {color_contrast3};\n"
        "}\n"
        "\n"
        ".intro-cta {\n"
        "\tdisplay: inline-block;\n"
        "\tmargin-top: 8px;\n"
        "\tpadding: 12px 20px;\n"
        "\tborder-radius: 12px;\n"
        f"\tbackground: {color_base};\n"
        "\tcolor: #ffffff;\n"
        "\ttext-decoration: none;\n"
        "\tfont-weight: 600;\n"
        "\ttransition: all .2s ease;\n"
        "}\n"
        "\n"
        ".intro-cta:hover {\n"
        f"\tbackground: {color_base2};\n"
        "\ttransform: translateY(-1px);\n"
        "}\n"
        "\n"
        ".intro-cta:active {\n"
        f"\tbackground: {color_contrast};\n"
        "}\n"
        "\n"
        "@media (max-width: 781px) {\n"
        "\t.bloque-intro-imagen {\n"
        "\t\tpadding: 20px;\n"
        "\t\tmargin: 32px auto;\n"
        "\t}\n"
        "\n"
        "\t.bloque-intro-imagen .wp-block-media-text {\n"
        "\t\tgap: 20px;\n"
        "\t}\n"
        "}\n"

            
        ".bloque-parrafo-normal {\n"
        "\tmax-width: 960px;\n"
        "\tmargin: 32px auto;\n"
        "\tpadding: 24px 28px;\n"
        f"\tcolor: {color_base};\n"
        f"\tbackground: {color_base3};\n"
        f"\tborder: 1px solid {color_contrast3};\n"
        f"\tborder-left: 6px solid {color_accent};\n"
        "\tborder-radius: 0 18px 18px 0;\n"
        "\tbox-shadow: 0 10px 24px rgba(31, 41, 55, 0.05);\n"
        "}\n"

        ".bloque-parrafo-normal h3 {\n"
        "\tmargin: 0 0 12px;\n"
        "\tfont-size: 23px;\n"
        "\tline-height: 1.2;\n"
        f"\tcolor: {color_contrast};\n"
        "}\n"
        ".bloque-parrafo-normal p {\n"
        "\tmargin: 0;\n"
        "\tfont-size: 17px;\n"
        "\tline-height: 1.8;\n"
        f"\tcolor: {color_base};\n"
        "\t}\n"    

        "t.bloque-parrafo-normal strong {\n"
        f"\tcolor: {color_contrast};\n"
        "}\n"

        "@media (max-width: 768px) {\n"
        "\t.bloque-parrafo-normal {\n"
        f"\tpadding: 20px;\n"
        f"\tmargin: 24px auto;\n"
        f"\tborder-left-width: 5px;\n"
        "\t}\n"
        "}\n"
        

        )

            
    fichero_css.write(css)
    fichero_css.close()