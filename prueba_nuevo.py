from funciones import *
from extraer_datos_excel import *
from negocio import *
from funciones_generar_texto import *
from extraer_datos_excel import *
from negocio import *
from autowordpress import *
from ficheros_datos.constantes_configuracion import *
import os





wc=WpConnection(f"{dominio}//xmlrpc.php",'hector.arnaus@gmail.com','bolo3o,Eresgay')
wc.connect()




wc=WpConnection(f"{dominio}//xmlrpc.php",'hector.arnaus@gmail.com','bolo3o,Eresgay')
wc.connect()



#excel_datos="/home/hector/proyectos/directorio/empresas_con_descripcion_corto.xlsx"

lista_provincias=obten_lista_provincias(excel_datos)
print("Lista de provincias obtenida:", lista_provincias)
lista_municipios=obten_lista_municipios(excel_datos)
print("Lista de municipios obtenida:", lista_municipios)
negocios=obten_lista_negocios(excel_datos)

etiquetas=['crepería','crepes','creperias cerca','crepe suzette','crepe nutella','crepe nocilla','crepe chocolate']
lista_categorias=[]

ruta=os.getcwd()+("/provincia")
for img in os.listdir(ruta):
    provincia=obten_nombre_provincia(img)
    print("Creando el artículo de la provincia de "+provincia)
    if provincia in lista_provincias:
        wp_img=Image(ruta+"/"+img,f"Descubre todas las {tipo_negocio.lower()} en la provincia de {provincia} ordenadas por orden alfabético")
        wp_img.upload(wc)
        wp_article=WpPost(f"{tipo_negocio} en la provincia de {provincia}")
        print(f"sluguiza provincia de {provincia}={sluguiza("provincia de "+provincia)}")
        wp_article.add_element(crea_provincia(provincia,wp_img))
        wp_article.set_slug(sluguiza("provincia de "+provincia))
        wp_article.add_category("provincia")
        wc.publica_post(wp_article)


ruta=os.getcwd()+("/municipio")
for img in os.listdir(ruta):
    municipio=obten_nombre_municipio(img)
    print("Creando el artículo del municipio de "+municipio)
    if municipio in lista_municipios:
        provincia=obten_nombre_provincia_municipio(img)
        wp_img=Image(ruta+"/"+img,f"{tipo_negocio} en el municipio de {municipio}")
        wp_img.upload(wc)
        wp_article=WpPost(f"{tipo_negocio} en el municipio de {municipio}","Provincia de "+provincia)
        wp_article.add_element(crea_ciudad(municipio,provincia,wp_img))
        wp_article.set_slug(sluguiza(municipio))
        wc.publica_post(wp_article)

for negocio in negocios:
    wp_article=WpPost(negocio.nombre,sluguiza(negocio.ciudad))
    wp_article.add_tag(negocio.ciudad)
    wp_article.add_element(crea_negocio(negocio))
    print(sluguiza(negocio.provincia)+"/"+sluguiza(negocio.ciudad)+"/"+sluguiza(negocio.nombre))
    wp_article.set_slug(sluguiza(negocio.nombre))
    wc.publica_post(wp_article)

