
from extraer_datos_excel import *
import re
import unicodedata



def obten_horario_dia(horario,dia):
    horario_troceado=horario.split(";")
    for trozo in horario_troceado:
        if dia in trozo:
            
            if "Cerrado" in trozo:
                return None
            elif "lunes, De " in trozo:                
                texto=trozo[len("lunes, De "):]
            elif "martes, De " in trozo:                
                texto=trozo[len("martes, De "):]
            elif "miércoles, De " in trozo:                
                texto=trozo[len("miércoles, De "):]
            elif "jueves, De " in trozo:                
                texto=trozo[len("jueves, De "):]
            elif "viernes, De " in trozo:                
                texto=trozo[len("viernes, De "):]
            elif "sábado, De " in trozo:                
                texto=trozo[len("sábado, De "):]
            elif "domingo, De " in trozo:                
                texto=trozo[len("domingo, De "):]

            # 00:00–23:59 amb hora d'1 o 2 xifres
            HORA = r'(?:[01]?\d|2[0-3]):[0-5]\d'

            patron = rf'(?:\bde\b[\s\u00A0]*)?({HORA})[\s\u00A0]*a[\s\u00A0]*({HORA})'
            res=re.findall(patron, texto, flags=re.IGNORECASE)
            print(res)
            print(len(res))
                


    return None

lista_negocios=[]
try:
    datos=openpyxl.load_workbook("castilla_leon_1.xlsx")
    hoja_activa = datos.active
    fila=2
    while fila<hoja_activa.max_row:
        horario=hoja_activa.cell(row=fila,column=5).value
        print(hoja_activa.cell(row=fila,column=1).value)
        print(obten_horario_dia(horario,"lunes"))
        fila+=1

except FileNotFoundError:
    print("Error: Archivo no encontrado.")
except Exception as e:
    print(f"Ocurrió un error: {e}")