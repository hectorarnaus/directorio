from funciones import *
from extraer_datos_excel import *
from negocio import *




#wc=WpConnection(f"{dominio}//xmlrpc.php",'hector.arnaus@gmail.com','bolo3o,Eresgay')
#wc.connect()



excel_datos="empresas_con_descripcion_corto.xlsx"

lista_provincias=obten_lista_provincias(excel_datos)
lista_municipios=obten_lista_municipios(excel_datos)
negocios=obten_lista_negocios(excel_datos)
print(crea_negocio_temp(negocios[4]))

