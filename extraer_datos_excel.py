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
    lista_localidades=[]
    try:
        datos=openpyxl.load_workbook(fichero_excel)
        hoja_activa = datos.active
        fila=2
        while fila<hoja_activa.max_row:
            localidad=hoja_activa.cell(row=fila,column=7).value#,hoja_activa.cell(row=fila,column=8).value]
            if localidad not in lista_localidades:
                lista.append([localidad,hoja_activa.cell(row=fila,column=8).value])
                lista_localidades.append(localidad)
            fila+=1
        #lista.sort()
        return lista

    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def obten_provincia_de_municipio(fichero_excel,municipio):
    try:
        datos=openpyxl.load_workbook(fichero_excel)
        hoja_activa = datos.active
        fila=2
        while fila<hoja_activa.max_row:
            if hoja_activa.cell(row=fila,column=7).value==municipio:
                return hoja_activa.cell(row=fila,column=8).value
            fila+=1
        return ""
    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


class Negocio:
    def __init__(self,municipio,provincia,nombre,texto,direccion,telefono,web,mapa,horario,foto):
        self.municipio=municipio
        self.provincia=provincia
        self.nombre=nombre
        self.texto=texto
        self.direccion=direccion
        self.telefono=telefono
        self.web=web
        self.mapa=mapa
        self.horario=horario
        self.foto=foto
    
    def __str__(self):
        return f'nombre={self.nombre} municipio={self.municipio}'
    
def obten_lista_negocios(fichero_excel):
    lista_negocios=[]
    try:
        datos=openpyxl.load_workbook(fichero_excel)
        hoja_activa = datos.active
        fila=2
        while fila<hoja_activa.max_row:
            municipio=hoja_activa.cell(row=fila,column=7).value
            provincia=hoja_activa.cell(row=fila,column=8).value
            nombre=hoja_activa.cell(row=fila,column=1).value
            texto=hoja_activa.cell(row=fila,column=13).value
            direccion=hoja_activa.cell(row=fila,column=6).value
            telefono=hoja_activa.cell(row=fila,column=10).value
            web=hoja_activa.cell(row=fila,column=9).value
            mapa=hoja_activa.cell(row=fila,column=11).value
            horario=hoja_activa.cell(row=fila,column=5).value
            foto=hoja_activa.cell(row=fila,column=12).value
            nuevo=Negocio(municipio,provincia,nombre,texto,direccion,telefono,web,mapa,horario,foto)
            lista_negocios.append(nuevo)
            fila+=1
        return lista_negocios
    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")