from ficheros_datos.constantes_configuracion import *
import os
from funciones_excel import obten_lista_municipios_con_provincia
from funciones import *



lista_municipios=obten_lista_municipios(excel_localidades)
ruta=os.getcwd()+("/municipio")
for img in os.listdir(ruta):
    municipio=obten_nombre_municipio(img)    
    if municipio in lista_municipios:
        lista_municipios.remove(municipio)


ruta=os.getcwd()+("/municipio/temp")
for municipio in lista_municipios:
    print("Procesando el municipio de "+municipio)
    provincia=obten_provincia_de_municipio_con_fichero_localidades(excel_localidades,municipio)
    fichero=open(ruta+"/"+municipio+"_"+provincia+".jpg","w")
    fichero.write(municipio)