from funciones import *
from funciones_excel import *
from Modelo.negocio import *
from funciones_generar_texto import *
from funciones_excel import *
from Modelo.negocio import *
from autowordpress import *
from ficheros_datos.constantes_configuracion import *
import os


crea_estilos()






lista_provincias=obten_lista_provincias(excel_empresas)
lista_municipios=obten_lista_municipios(excel_empresas)
for municipio in lista_municipios:
    print(municipio)
negocios=obten_lista_negocios(excel_empresas)
lista_actividades_municipio=obten_lista_actividades_municipios(excel_empresas)

etiquetas=['crepería','crepes','creperias cerca','crepe suzette','crepe nutella','crepe nocilla','crepe chocolate']
lista_categorias=[]


wc=WpConnection(f"{dominio}//xmlrpc.php",'hector.arnaus@gmail.com','bolo3o,Eresgay')
wc.connect()
ruta=os.getcwd()+("/provincia")
for img in os.listdir(ruta):
    Provincia=obten_nombre_provincia(img)
    print("Creando el artículo de la provincia de "+Provincia)
    if Provincia in lista_provincias:
        wp_img=Image(ruta+"/"+img,f"Descubre todas las {tipo_negocio.lower()} en la provincia de {Provincia} ordenadas por orden alfabético")
        wp_img.upload(wc)
        wp_article=WpPost(f"{tipo_negocio} en la provincia de {Provincia}")
        wp_article.add_element(crea_provincia(Provincia,wp_img))
        wp_article.set_slug(sluguiza("provincia de "+Provincia))
        wp_article.add_category("provincia")
        wc.publica_post(wp_article)


ruta=os.getcwd()+("/municipio")
for img in os.listdir(ruta):
    municipio=obten_nombre_municipio(img)
    print("Creando el artículo del municipio de "+municipio)
    if municipio in lista_municipios:
        Provincia=obten_nombre_provincia_municipio(img)
        wp_img=Image(ruta+"/"+img,f"{tipo_negocio} en el municipio de {municipio}")
        wp_img.upload(wc)
        wp_article=WpPost(f"{tipo_negocio} en el municipio de {municipio}","Provincia de "+Provincia)
        wp_article.add_element(crea_localidad(municipio,Provincia,wp_img))
        wp_article.set_slug(sluguiza(municipio))
        wc.publica_post(wp_article)

for negocio in negocios:
    print("Creando el artículo del negocio "+negocio.nombre)
    wp_article=WpPost(negocio.nombre,sluguiza(negocio.ciudad))
    wp_article.add_tag(negocio.ciudad)
    wp_article.add_element(crea_negocio(negocio))
    wp_article.set_slug(sluguiza(negocio.nombre))
    wc.publica_post(wp_article)

