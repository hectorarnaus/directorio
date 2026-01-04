def crea_lista_direccion(direccion):
    res=('<!-- wp:shortcode -->\n'
        f'\t[su_list icon="icon: map-marker" icon_color="{color_contrast}"  indent="20" class="lista"]\n'
        '\t\t<ul>\n'
        f'\t\t\t<li><strong>Dirección postal:</strong> {direccion}</li>\n'
        '\t\t</ul>'
        f'\t[/su_list]'
        '<!-- /wp:shortcode -->\n'
    )
    return res
def crea_lista_telefono(telefono):
    res=('<!-- wp:shortcode -->\n'
         f'\t[su_list icon="icon: phone" icon_color="{color_contrast}" indent="20" class="lista"]\n'
         '\t\t<ul>\n'
        f'\t\t\t<li><strong>Teléfono:</strong> <a href="tel:{telefono}">{telefono}</a></li>\n'
        '\t\t</ul>\n'
        '\t[/su_list]\n'
        '<!-- /wp:shortcode -->\n'
    )
    return res
    
def crea_lista_web(web):
    if web!=None:
        res=('<!-- wp:shortcode -->\n'
            f'\t[su_list icon="icon: dribbble" icon_color="{color_contrast}" indent="20" class="lista"]\n'
            '\t\t<ul>\n'
            f'\t\t\t<li><strong>Sitio web:</strong> <a href="{web}">{web}</a></li>\n'
            '\t\t</ul>\n'
            '\t[/su_list]\n'
            '<!-- /wp:shortcode -->\n'
        )
        return res

def crea_botones_datos_contacto(telefono,web):
    if web!=None:
        res=(
            '<!-- wp:shortcode -->\n'
            f'\t[su_button url="tel:{telefono}" color="{color_contrast}" background="{color_accent}" wide="yes" size="5" center="yes"]¡Llama ahora![/su_button]\n'
            '<!-- /wp:shortcode -->\n'

            '<!-- wp:shortcode -->\n'
            f'\t[su_button url="{web}" color="{color_contrast}" background="{color_accent}" wide="yes" size="5" center="yes"]Visitar web[/su_button]\n'
            '<!-- /wp:shortcode -->\n'
        )
        
    else:
        res=(
            '<!-- wp:shortcode -->\n'
            f'\t[su_button url="tel:{telefono}" color="{color_contrast}" background="{color_accent}" wide="yes" size="5" center="yes"]¡Llama ahora![/su_button]\n'
            '<!-- /wp:shortcode -->\n'

            '<!-- wp:shortcode -->\n'
            f'\t[su_button url="{dominio}" color="{color_contrast}" background="{color_accent}" wide="yes" size="5" center="yes"]Visitar web[/su_button]\n'
            '<!-- /wp:shortcode -->\n'
        )
    return res

def crea_parrafo(texto):
    res=('\t<!-- wp:paragraph -->\n'
        f'\t\t<p>{texto}</p>\n'
        '\t<!-- /wp:paragraph -->\n'
    )
    return res
def crea_heading(texto,numero):
    res=('<!-- wp:heading {"textAlign":"center"} -->\n'
        f'\t<h{numero} class="wp-block-heading has-text-align-center">{texto}</h{numero}>\n'
        '<!-- /wp:heading -->\n'
    )
    return res
def crea_lista_horario(horario):
    res=('<!-- wp:shortcode -->\n'
        f'\t[su_list icon="icon: clock-o" icon_color="{color_contrast}" indent="20" class="lista"]\n{horario}\n'
            '\t[/su_list]\n'
        '<!-- /wp:shortcode -->\n'
    )
    return res

def crea_mapa(negocio):
    res=('<!-- wp:html -->\n'
        f'\t<iframe src="{negocio.mapa}" width="600" height="450"  style="border:2px solid {color_contrast}; box-shadow: 0 2px 8px rgba(0,0,0,0.08); border-radius: 12px;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>\n'
        '<!-- /wp:html -->\n'
    )
    return res

def crea_imagen(negocio):
    res=('<!-- wp:image {"sizeSlug":"large","align":"center","className":"is-style-default"} -->\n'
        f'\t<figure class="wp-block-image aligncenter size-large is-style-default"><img src="{negocio.imagen}" alt="{negocio.nombre}"></figure>\n'
        '<!-- /wp:image -->\n'
    )
    return res




def crea_reviews(negocio):
    res=('[su_row]'
         '\t[su_column size="1/1" center="no" class=""]\n'
        '\t\t<!-- wp:shortcode -->\n'
        f'\t\t\t[site_reviews_summary rate="4" assigned_terms="{sluguiza(negocio.nombre)}" hide="average,stars,percentage,bar"]'
        '\t\t<!-- /wp:shortcode -->\n'        
        '\t</su_column>\n'
        '\t[su_column size="1/1" center="no" class=""]\n'
        '\t\t<!-- wp:shortcode -->\n'
        f'\t\t\t[site_reviews_form assigned_terms="{sluguiza(negocio.nombre)}" hide="content,email,terms,title,name"]'
        '\t\t<!-- /wp:shortcode -->\n'
        '\t</su_column>\n'
        '</su_row>\n'
    )
    return res
def crea_contenedor(contenido):
    res=(
        '<!-- wp:group {"layout":{"type":"constrained"}} -->\n'
        '\t<div class="wp-block-group contenedor">'
        f'\t\t{contenido}'
        '</div>\n'
        '<!-- /wp:group -->\n\n'
    )
    return res

def crea_bloque_contacto(negocio):
    res=(f'{crea_heading("Datos de contacto",2)}'    
        f'{crea_lista_direccion(negocio.direccion)}'
        f'{crea_lista_telefono(negocio.telefono)}'
    )
    if negocio.web!=None:
        res+=f'{crea_lista_web(negocio.web)}'

    res+='\t<!-- wp:shortcode -->\n'
    res+='\t\t[adinserter name="anuncio_manual"]\n'
    res+='\t<!-- /wp:shortcode -->\n'
    res+=f'{crea_botones_datos_contacto(negocio.telefono,negocio.web)}'
    return crea_contenedor(res)

def crea_bloque_horario(negocio):
    res=f'{crea_heading("Horario",2)}'
    res+=f'{crea_lista_horario(negocio.obten_horario_lista_html())}'
    return crea_contenedor(res)

def crea_bloque_mapa(negocio):
    res=f'{crea_heading("Localización",2)}'
    res+=f'{crea_mapa(negocio)}'
    return crea_contenedor(res)

def crea_bloque_imagen(negocio):
    res=f'{crea_heading("Fotografía",2)}'
    res+=f'{crea_imagen(negocio)}'
    return crea_contenedor(res)

def crea_bloque_reviews(negocio):
    res=f'{crea_heading(f"¿Qué opinan los usuarios de {negocio.nombre}?",2)}'
    res+=f'{crea_parrafo("Aquí puedes leer las opiniones y valoraciones de otros usuarios que han visitado "+negocio.nombre+". Si has estado aquí, no dudes en dejar tu propia reseña más abajo para ayudar a otros usuarios a conocer mejor este negocio.")}'
    res+=f'{crea_reviews(negocio)}'
    return crea_contenedor(res)

def crea_bloque_descripcion_seo(negocio):
    res=f'{crea_heading("Información",2)}'
    res+=f'{crea_parrafo(negocio.descripcion_seo)}'
    return crea_contenedor(res)

def crea_bloque_otros_negocios(negocio):
    res=crea_heading(f'Todas las creperías en {negocio.ciudad}',2)
    res+=(
        '<!-- wp:dpt/display-post-types {"taxonomy":"category","terms":['
        f'"{sluguiza(negocio.ciudad)}"'
        '],"number":100,"orderBy":"title","order":"ASC","styles":"dpt-list2","styleSup":["title"],"imgAspect":"land1","textPosHor":"center"}\n'
        '/-->'
    
        )
    return crea_contenedor(res)