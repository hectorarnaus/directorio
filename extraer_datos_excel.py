import openpyxl 
def obten_lista_provincias(fichero_excel):
    lista=[]
    try:
        datos=openpyxl.load_workbook(fichero_excel)
        hoja_activa = datos.active
        fila=2
        while fila<hoja_activa.max_row:
            if hoja_activa.cell(row=fila,column=8).value not in lista:
                lista.append(hoja_activa.cell(row=fila,column=8).value)
            fila+=1
        lista.sort()
        return lista
        
    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def obten_lista_municipios(fichero_excel):
    lista=[]
    try:
        datos=openpyxl.load_workbook(fichero_excel)
        hoja_activa = datos.active
        fila=2
        while fila<hoja_activa.max_row:
            localidad=[hoja_activa.cell(row=fila,column=7).value,hoja_activa.cell(row=fila,column=8).value]
            if localidad not in lista:
                lista.append(localidad)
            fila+=1
        #lista.sort()
        return lista

    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")