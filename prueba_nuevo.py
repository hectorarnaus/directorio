from funciones import *
from extraer_datos_excel import *
from negocio import *
from funciones import *
from extraer_datos_excel import *
from negocio import *
from autowordpress import *
from constantes_configuracion import *




wc=WpConnection(f"{dominio}//xmlrpc.php",'hector.arnaus@gmail.com','bolo3o,Eresgay')
wc.connect()




wc=WpConnection(f"{dominio}//xmlrpc.php",'hector.arnaus@gmail.com','bolo3o,Eresgay')
wc.connect()



excel_datos="/home/hector/proyectos/directorio/empresas_con_descripcion_corto.xlsx"

lista_provincias=obten_lista_provincias(excel_datos)
lista_municipios=obten_lista_municipios(excel_datos)
negocios=obten_lista_negocios(excel_datos)

for negocio in negocios:
    wp_article=WpPost(negocio.nombre,sluguiza(negocio.ciudad))
    wp_article.add_tag(negocio.ciudad)
    wp_article.add_element(crea_negocio_temp(negocio))
    print(sluguiza(negocio.provincia)+"/"+sluguiza(negocio.ciudad)+"/"+sluguiza(negocio.nombre))
    wp_article.set_slug(sluguiza(negocio.nombre))
    wc.publica_post(wp_article)

'''
wp_article=WpPost(negocios[4].nombre,sluguiza(negocios[4].ciudad))
wp_article.add_tag(negocios[4].ciudad)
wp_article.add_element(crea_negocio_temp(negocios[4]))
print(sluguiza(negocios[4].provincia)+"/"+sluguiza(negocios[4].ciudad)+"/"+sluguiza(negocios[4].nombre))
wp_article.set_slug(sluguiza(negocios[4].nombre))
wc.publica_post(wp_article)

'''
