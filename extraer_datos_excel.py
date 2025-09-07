import openpyxl 
import re
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
            localidad=hoja_activa.cell(row=fila,column=7).value#,hoja_activa.cell(row=fila,column=8).value]
            if localidad not in lista:
                lista.append(localidad)#,hoja_activa.cell(row=fila,column=8).value])
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
                  f'\t<li><strong>Lunes:</strong> {lunes}</li>\n'
                  f'\t<li><strong>Martes:</strong> {martes}</li>\n'
                  f'\t<li><strong>Miércoles:</strong> {miercoles}</li>\n'
                  f'\t<li><strong>Jueves:</strong> {jueves}</li>\n'
                  f'\t<li><strong>Viernes:</strong> {viernes}</li>\n'
                  f'\t<li><strong>Sábado:</strong> {sabado}</li>\n'
                  f'\t<li><strong>Domingo:</strong> {domingo}</li>\n'
				'</ul>\n')
    return horario_html


def obten_horario_dia(horario,dia):
       
    horario_troceado=horario.split(";")
    for trozo in horario_troceado:
        if dia in trozo:
            
            if "Cerrado" in trozo:
                return None
            elif f"{dia}, De " in trozo:                
                texto=trozo[len(f"{dia}, De "):]

            #HORA = r'(?:[01]?\d|2[0-3])(?::[0-5]\d)?'
            HORA = r'(?:2[0-3]|[01]?\d)(?::[0-5]\d)?'

            # Expresión regular que captura todos los intervalos
            patron = rf'(?:\bde\b[\s\u00A0]*)?({HORA})[\s\u00A0]*a[\s\u00A0]*({HORA})'
            
            # Encuentra todos los pares de horas
            tramos = re.findall(patron, texto, flags=re.IGNORECASE)
            # Aplana la lista de tuplas [(ini, fin), ...] → [ini, fin, ...]
            horas = [h if ":" in h else f"{h}:00" for par in tramos for h in par]


            d_dias=dict([
                ('lunes','Mo'),
                ('martes','Tu'),
                ('miércoles','We'),
                ('jueves','Th'),
                ('viernes','Fr'),
                ('sábado','Sa'),
                ('domingo','Su')
            ])
            if len(horas)==2:
                return f'\t\t"{d_dias[dia]} {horas[0]}-{horas[1]}"'
            elif len(horas)==4:
                return f'\t\t"{d_dias[dia]} {horas[0]}-{horas[1]}, {horas[2]}-{horas[3]}"'
                     
    return None

def obten_horario_semanal(horario):
    horario_dias=[]
    if obten_horario_dia(horario,"lunes")!=None:
        horario_dias.append(obten_horario_dia(horario,"lunes"))
    if obten_horario_dia(horario,"martes")!=None:
        horario_dias.append(obten_horario_dia(horario,"martes"))
    if obten_horario_dia(horario,"miércoles")!=None:
        horario_dias.append(obten_horario_dia(horario,"miércoles"))
    if obten_horario_dia(horario,"jueves")!=None:
        horario_dias.append(obten_horario_dia(horario,"jueves"))
    if obten_horario_dia(horario,"viernes")!=None:
        horario_dias.append(obten_horario_dia(horario,"viernes"))
    if obten_horario_dia(horario,"sábado")!=None:
        horario_dias.append(obten_horario_dia(horario,"sábado"))
    if obten_horario_dia(horario,"domingo")!=None:
        horario_dias.append(obten_horario_dia(horario,"domingo"))
    
    res=""
    i=0
    while i<len(horario_dias)-2:
        res+=f'{horario_dias[i]},\n'
        i+=1
    res+=f'{horario_dias[i]}\n'  
    return res

class Negocio:
    def __init__(self,municipio,provincia,nombre,texto,direccion,telefono,web,mapa,horario,foto,rating,reviews):
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
        self.horario=horario
        self.horario_html=crea_horario_html(horario)
        self.horario_lunes=obten_horario_dia(horario,"lunes")
        self.horario_martes=obten_horario_dia(horario,"martes")
        self.horario_miercoles=obten_horario_dia(horario,"miércoles")
        self.horario_jueves=obten_horario_dia(horario,"jueves")
        self.horario_viernes=obten_horario_dia(horario,"viernes")
        self.horario_sabado=obten_horario_dia(horario,"sábado")
        self.horario_domingo=obten_horario_dia(horario,"donmingo")
        self.foto=foto
        self.rating=rating
        self.reviews=reviews
    
    def __str__(self):
        return f'nombre={self.nombre} municipio={self.municipio}'
    
def obten_lista_negocios(fichero_excel):
    lista_negocios=[]
    try:
        datos=openpyxl.load_workbook(fichero_excel)
        hoja_activa = datos.active
        fila=1
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
            rating=hoja_activa.cell(row=fila,column=3).value
            reviews=hoja_activa.cell(row=fila,column=4).value
            if horario==None:
                horario=""
            foto=hoja_activa.cell(row=fila,column=12).value
            nuevo=Negocio(municipio,provincia,nombre,texto,direccion,telefono,web,mapa,horario,foto,rating,reviews)
            lista_negocios.append(nuevo)
            fila+=1
                  
        return lista_negocios
    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


def obten_lista_negocios_municipio(fichero_excel,municipio):
    lista_negocios=[]
    try:
        datos=openpyxl.load_workbook(fichero_excel)
        hoja_activa = datos.active
        fila=1
        while fila<hoja_activa.max_row:
            if hoja_activa.cell(row=fila,column=7).value==municipio:
                provincia=hoja_activa.cell(row=fila,column=8).value
                nombre=hoja_activa.cell(row=fila,column=1).value
                texto=hoja_activa.cell(row=fila,column=13).value
                direccion=hoja_activa.cell(row=fila,column=6).value
                telefono=hoja_activa.cell(row=fila,column=10).value
                web=hoja_activa.cell(row=fila,column=9).value
                mapa=hoja_activa.cell(row=fila,column=11).value
                horario=hoja_activa.cell(row=fila,column=5).value
                rating=hoja_activa.cell(row=fila,column=3).value
                reviews=hoja_activa.cell(row=fila,column=4).value
                if horario==None:
                    horario=""
                foto=hoja_activa.cell(row=fila,column=12).value
                nuevo=Negocio(municipio,provincia,nombre,texto,direccion,telefono,web,mapa,horario,foto,rating,reviews)
                lista_negocios.append(nuevo)
            fila+=1
                  
        return lista_negocios
    except FileNotFoundError:
        print("Error: Archivo no encontrado.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
               