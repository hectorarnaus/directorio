from Modelo.negocio import *
from ficheros_datos.constantes_configuracion import *
from funciones_excel import *

lista_provincias=crea_lista_provincias(excel_provincias)
lista_localidades=crea_lista_localidades(excel_localidades)
for provincia in lista_provincias:
    for localidad in lista_localidades:
        if localidad.provincia==provincia.nombre:
            provincia.anyade_localidad(localidad)

for provincia in lista_provincias:
    print("**********************************************")
    print(provincia.nombre)
    for localidad in provincia.localidades:
        print(f"\t{localidad.nombre}")
