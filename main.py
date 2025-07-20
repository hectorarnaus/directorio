import os
import openpyxl 
from funciones import *
from extraer_datos_excel import *
from autowordpress import *




dominio="https://calculadora-porcentajes-colombia.top"
wc=WpConnection(f"{dominio}//xmlrpc.php",'hector.arnaus@gmail.com','bolo3o,Eresgay')
wc.connect()

etiquetas=['crepería','crepes','creperias cerca','crepe suzette','crepe nutella','crepe nocilla','crepe chocolate']


'''
ruta=os.getcwd()+("/provincia")
for img in os.listdir(ruta):
    provincia=obten_nombre_provincia(img)
    print(f"Creando el artículo de la provincia de {provincia}")
    wp_img=Image(ruta+"/"+img,f"Creperías en la provincia de {provincia}")
    wp_img.upload(wc)
    wp_article=WpPost(f"Creperías en la provincia de {provincia}")
    #imagen=WpImage(wp_img)
    for etiqueta in etiquetas:
        wp_article.add_tag(etiqueta)
    wp_article.add_element(crea_provincia(dominio,provincia,obten_texto_provincia(provincia),wp_img))
    wp_article.set_slug(sluguiza(provincia))
    print(wp_article.get_post())
    wc.publica_post(wp_article)


ruta=os.getcwd()+("/municipio")
for img in os.listdir(ruta):
    municipio=obten_nombre_municipio(img)
    provincia=obten_nombre_provincia_municipio(img)
    print(f"La provincia de {municipio} es {provincia}")
    print(f"Creando el artículo del municipio de {municipio}")
    #texto_con_estado=cambia_estado(texto_base,estado)
    #parrafos=texto_con_estado.split("\n")
    wp_img=Image(ruta+"/"+img,f"Creperías en el municipio de {municipio}")
    wp_img.upload(wc)
    wp_article=WpPost(f"Creperías en el municipio de {municipio}")
    wp_article.add_category(provincia)
    wp_article.add_tag(provincia)
    for etiqueta in etiquetas:
        wp_article.add_tag(etiqueta)
    #imagen=WpImage(wp_img)
    wp_article.add_element(crea_municipio(dominio,municipio,provincia,obten_texto_municipio(municipio),wp_img))
    wp_article.set_slug(sluguiza(provincia)+"/"+sluguiza(municipio))
    wc.publica_post(wp_article)

    ''' 
negocios=obten_lista_negocios("castilla_leon_1.xlsx")
for negocio in negocios:
    wp_article=WpPost(f"{negocio.nombre}")
    wp_article.add_category(negocio.municipio)
    wp_article.add_tag(negocio.municipio)
    for etiqueta in etiquetas:
        wp_article.add_tag(etiqueta)
    wp_article.add_element(crea_negocio(dominio,negocio))
    wp_article.set_slug(sluguiza(negocio.provincia)+"/"+sluguiza(negocio.municipio)+"/"+sluguiza(negocio.nombre))
    wc.publica_post(wp_article)