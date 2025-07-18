import os
import openpyxl 
from extraer_datos_excel import *

negocios=obten_lista_negocios("castilla_leon_1.xlsx")
for negocio in negocios:
    print(str(negocio))