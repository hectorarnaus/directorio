import os
import openpyxl 
from funciones import *
from extraer_datos_excel import *
from autowordpress import *




dominio="https://calculadora-porcentajes-colombia.top"
wc=WpConnection(f"{dominio}//xmlrpc.php",'hector.arnaus@gmail.com','bolo3o,Eresgay')
wc.connect()

etiquetas=['crepería','crepes','creperias cerca','crepe suzette','crepe nutella','crepe nocilla','crepe chocolate']
lista_categorias=[]

ruta=os.getcwd()+("/provincia")
for img in os.listdir(ruta):
    provincia=obten_nombre_provincia(img)
    wp_img=Image(ruta+"/"+img,f"Descubre todas las creperías en la provincia de {provincia} ordenadas por orden alfabético")
    wp_img.upload(wc)
    wp_article=WpPost(f"Creperías en la provincia de {provincia}")
    print(f"sluguiza provincia de {provincia}={sluguiza("provincia de "+provincia)}")
    categoria=WPCategory("Provincia de "+provincia,sluguiza("provincia-"+provincia))
    id_categoria=categoria.creaCategoria(wc)
    d_categoria = {
        "Nombre": provincia,
        "Id": id_categoria
    }
    lista_categorias.append(d_categoria)
    '''wp_article.add_tag("provincias")
    for etiqueta in etiquetas:
        wp_article.add_tag(etiqueta)'''
    wp_article.add_element(crea_provincia(dominio,provincia,obten_texto_provincia(provincia),wp_img))
    wp_article.set_slug(sluguiza("provincia de "+provincia))
    print(wp_article.get_post())
    wc.publica_post(wp_article)


ruta=os.getcwd()+("/municipio")
for img in os.listdir(ruta):
    municipio=obten_nombre_municipio(img)
    provincia=obten_nombre_provincia_municipio(img)
    print(f"La provincia de {municipio} es {provincia}")
    print(f"Creando el artículo del municipio de {municipio}")
    wp_img=Image(ruta+"/"+img,f"Creperías en el municipio de {municipio}")
    wp_img.upload(wc)
    wp_article=WpPost(f"Creperías en el municipio de {municipio}","Provincia de "+provincia)
    ''' print(f"creando categoría nombre={municipio} slug={sluguiza(municipio)} provincia={provincia}")
    print(f"id de categoria de provincia={obten_id_categoria_provincia(provincia,lista_categorias)}")'''
    categoria=WPCategory(sluguiza(municipio),sluguiza(municipio),obten_id_categoria_provincia(provincia,lista_categorias))
    categoria.creaCategoria(wc)
    #wp_article.add_category("Provincia de "+provincia)
    wp_article.add_tag(provincia)
    for etiqueta in etiquetas:
        wp_article.add_tag(etiqueta)
    wp_article.add_element(crea_municipio(dominio,municipio,provincia,obten_texto_municipio(municipio),wp_img))
    wp_article.set_slug(sluguiza(municipio))
    wc.publica_post(wp_article)

    
negocios=obten_lista_negocios("castilla_leon_1.xlsx")
for negocio in negocios:
    wp_article=WpPost(f"{negocio.nombre}",sluguiza(negocio.municipio))
    '''print(f"categoría del articulo={sluguiza(negocio.municipio)}")
    wp_article.add_category(sluguiza(negocio.municipio))'''
    wp_article.add_tag(negocio.municipio)
    for etiqueta in etiquetas:
        wp_article.add_tag(etiqueta)
    wp_article.add_element(crea_negocio(dominio,negocio))
    print(sluguiza(negocio.provincia)+"/"+sluguiza(negocio.municipio)+"/"+sluguiza(negocio.nombre))
    wp_article.set_slug(sluguiza(negocio.nombre))
    wc.publica_post(wp_article)