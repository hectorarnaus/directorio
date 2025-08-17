
from extraer_datos_excel import *



lista_negocios=[]
try:
    datos=openpyxl.load_workbook("castilla_leon_1.xlsx")
    hoja_activa = datos.active
    fila=1
    while fila<hoja_activa.max_row:
        print(hoja_activa.cell(row=fila,column=1).value)
        horario=hoja_activa.cell(row=fila,column=5).value
        print(obten_horario_semanal(horario))
        fila+=1

except FileNotFoundError:
    print("Error: Archivo no encontrado.")
except Exception as e:
    print(f"Ocurrió un error: {e}")