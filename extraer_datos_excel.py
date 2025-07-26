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

def crea_horario_html(horario):
    if horario=="":
        return ""
    
    inicio_lunes=horario.find("lunes,")
    final_lunes=horario.find(";",inicio_lunes+6)
    lunes=horario[inicio_lunes+6:final_lunes].lower()
    if final_lunes==-1:
        final_lunes=len(horario)

    inicio_martes=horario.find("martes,")
    final_martes=horario.find(";",inicio_martes+7)
    martes=horario[inicio_martes+7:final_martes].lower()
    if final_martes==-1:
        final_martes=len(horario)
    
    inicio_miercoles=horario.find("miércoles,")
    final_miercoles=horario.find(";",inicio_miercoles+10)
    miercoles=horario[inicio_miercoles+10:final_miercoles].lower()
    if final_miercoles==-1:
        final_miercoles=len(horario)

    inicio_jueves=horario.find("jueves,")
    final_jueves=horario.find(";",inicio_jueves+7)
    jueves=horario[inicio_jueves+7:final_jueves].lower()
    if final_jueves==-1:
        final_jueves=len(horario)

    inicio_viernes=horario.find("viernes,")
    final_viernes=horario.find(";",inicio_viernes+8)
    viernes=horario[inicio_viernes+8:final_viernes].lower()
    if final_viernes==-1:
        final_viernes=len(horario)

    inicio_sabado=horario.find("sábado,")
    final_sabado=horario.find(";",inicio_sabado+7)
    sabado=horario[inicio_sabado+7:final_sabado].lower()
    if final_sabado==-1:
        final_sabado=len(horario)

    inicio_domingo=horario.find("domingo,")
    final_domingo=horario.find(";",inicio_domingo+9)
    if final_domingo==-1:
        final_domingo=len(horario)
    domingo=horario[inicio_domingo+9:final_domingo].lower()

    horario_html=('<ul>\n'
                  f'\t<li><stron>Lunes:</strong> {lunes}</li>\n'
                  f'\t<li><stron>Martes:</strong> {martes}</li>\n'
                  f'\t<li><stron>Miércoles:</strong> {miercoles}</li>\n'
                  f'\t<li><stron>Jueves:</strong> {jueves}</li>\n'
                  f'\t<li><stron>Viernes:</strong> {viernes}</li>\n'
                  f'\t<li><stron>Sábado:</strong> {sabado}</li>\n'
                  f'\t<li><stron>Domingo:</strong> {domingo}</li>\n'
				'</ul>\n')
    return horario_html

class Negocio:
    def __init__(self,municipio,provincia,nombre,texto,direccion,telefono,web,mapa,horario,foto):
        self.municipio=municipio
        self.provincia=provincia
        self.nombre=nombre
        self.texto=texto
        self.direccion=direccion
        self.telefono=telefono
        self.web=web
        inicio=mapa.find('src="')+5
        final=mapa.find('"',inicio+1)+1
        self.mapa=mapa[inicio:final-1]
        self.horario=crea_horario_html(horario)
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
            if horario==None:
                horario=""
            foto=hoja_activa.cell(row=fila,column=12).value
            nuevo=Negocio(municipio,provincia,nombre,texto,direccion,telefono,web,mapa,horario,foto)
            lista_negocios.append(nuevo)
            fila+=1
            
        return lista_negocios
    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")