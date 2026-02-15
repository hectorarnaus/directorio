from ficheros_datos.constantes_configuracion import *
from funciones_excel import *

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

    res+=('\t"address": {\n'
        '\t\t"@type": "PostalAddress",\n'
        f'\t\t"streetAddress": "{negocio.direccion}",\n'
        f'\t\t"addressLocality": "{negocio.ciudad}",\n'
        f'\t\t"addressRegion": "{negocio.provincia}",\n'
        '\t\t"addressCountry": "ES"\n'
        '\t\t},\n'
        f'\t"telephone": "{negocio.telefono}",\n'
    )   
    if negocio.web!=None and negocio.web!="":
        res+=f'\t"url": "{negocio.web}",\n'
    if negocio.horario!=None and negocio.horario!="":
        if negocio.obten_horario_schema().endswith(",\n"):
            res+=negocio.obten_horario_schema()[:-2]+"\n"
   
    
    
    return res

def crea_schema_municipio(municipio):
    negocios=obten_lista_negocios_municipio(excel_empresas,municipio)
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

        if i<len(negocios)-1:
          schema_negocio+=","
        i+=1  
        res+=schema_negocio
    res+=']\n}\n'

        
    return res

