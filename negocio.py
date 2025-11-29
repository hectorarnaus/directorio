
import re,html
from bs4 import BeautifulSoup


def obten_horario_dia(horario,dia):
       
    horario_troceado=horario.split(";")
    for trozo in horario_troceado:
        if dia in trozo:
            
            if "Cerrado" in trozo:
                return None
            elif f"{dia}, De " in trozo:                
                texto=trozo[len(f"{dia}, De "):]
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

def limpia_comillas(texto):
    if texto!=None:
        if texto.startswith('"') and texto.endswith('"'):
            texto=texto[1:-1]
    return texto

class Negocio:
    def __init__(self,nombre,direccion,CP,ciudad,provincia,telefono,pagina_web,actividad,actividades_relacionadas,marcas,descripcion,mapa,imagen,facebook,instagram,x,youtube,horario,descripcion_seo):
        self.nombre=html.escape(str(nombre))
        self.direccion=html.escape(str(direccion))
        self.CP=html.escape(str(CP))
        self.ciudad=html.escape(str(ciudad))
        self.provincia=html.escape(str(provincia))
        self.telefono=html.escape(str(telefono))
        self.web=html.escape(str(pagina_web))
        self.actividad=html.escape(str(actividad))
        self.actividades_relacionadas=html.escape(str(actividades_relacionadas))
        self.marcas=html.escape(str(marcas))
        self.descripcion=html.escape(str(descripcion))
        if (mapa!=None):
            inicio=mapa.find("src='")+5
            final=mapa.find("'",inicio+1)+1
            self.mapa=mapa[inicio:final-1]
        else:
            self.mapa=mapa
        self.imagen=html.escape(str(imagen))
        self.facebook=html.escape(str(facebook))
        self.instagram=html.escape(str(instagram))
        self.x=x
        self.youtube=html.escape(str(youtube))        
        #self.horario=(horario[1:])[:-1] if horario.startswith("[") and horario.endswith("]") else html.escape(str(horario))
        self.horario=limpia_comillas(horario)
        self.descripcion_seo=html.escape(str(descripcion_seo))
        
    '''
    def __init__(self,municipio,provincia,nombre,texto,direccion,telefono,web,mapa,horario,foto,rating,reviews):

        self.municipio=html.escape(str(municipio))
        self.provincia=html.escape(str(provincia))
        self.nombre=html.escape(str(nombre))
        self.texto=html.escape(str(texto))
        self.direccion=html.escape(str(direccion))
        self.telefono=html.escape(str(telefono))
        self.web=html.escape(str(web))
        inicio=mapa.find('src="')+5
        final=mapa.find('"',inicio+1)+1
        self.mapa=mapa[inicio:final-1]
        self.horario=horario
        self.horario_html=self.obten_horario_html()
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
        '''
    
    def __str__(self):
        return f'nombre={self.nombre} ciudad={self.ciudad}'
    
    def obten_horario_lista_html(self):
        dias=['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo']
        soup = BeautifulSoup(self.horario, "html.parser")
        soup.prettify()
        if self.horario=="":
            return ""
        itemprops = soup.select('time[itemprop="openingHours"]')
        horario_html=""
        if len(itemprops) == 5:
            horario_html=('<ul>\n'
                        f'\t<li><strong>{dias[0]}:</strong> {itemprops[0].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[1]}:</strong> {itemprops[1].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[2]}:</strong> {itemprops[2].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[3]}:</strong> {itemprops[3].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[4]}:</strong> {itemprops[4].get_text(strip=True)}</li>\n'
                        '</ul>\n')
            return horario_html
        elif len(itemprops) == 6:
            horario_html=('<ul>\n'
                        f'\t<li><strong>{dias[0]}:</strong> {itemprops[0].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[1]}:</strong> {itemprops[1].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[2]}:</strong> {itemprops[2].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[3]}:</strong> {itemprops[3].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[4]}:</strong> {itemprops[4].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[5]}:</strong> {itemprops[5].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[6]}:</strong> cerrado</li>\n'
                        '</ul>\n')
            return horario_html
        elif len(itemprops) == 7:
            horario_html=('<ul>\n'
                        f'\t<li><strong>{dias[0]}:</strong> {itemprops[0].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[1]}:</strong> {itemprops[1].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[2]}:</strong> {itemprops[2].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[3]}:</strong> {itemprops[3].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[4]}:</strong> {itemprops[4].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[5]}:</strong> {itemprops[5].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[6]}:</strong> {itemprops[6].get_text(strip=True)}</li>\n'
                        '</ul>\n')
        elif len(itemprops) == 10:
            horario_html=('<ul>\n'
                        f'\t<li><strong>{dias[0]}:</strong> {itemprops[0].get_text(strip=True)} y {itemprops[1].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[1]}:</strong> {itemprops[2].get_text(strip=True)} y {itemprops[3].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[2]}:</strong> {itemprops[4].get_text(strip=True)} y {itemprops[5].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[3]}:</strong> {itemprops[6].get_text(strip=True)} y {itemprops[7].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[4]}:</strong> {itemprops[8].get_text(strip=True)} y {itemprops[9].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[5]}:</strong> cerrado</li>\n'
                        f'\t<li><strong>{dias[6]}:</strong> cerrado</li>\n'
                        '</ul>\n')
        elif len(itemprops) == 11:
            horario_html=('<ul>\n'
                        f'\t<li><strong>{dias[0]}:</strong> {itemprops[0].get_text(strip=True)} y {itemprops[1].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[1]}:</strong> {itemprops[2].get_text(strip=True)} y {itemprops[3].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[2]}:</strong> {itemprops[4].get_text(strip=True)} y {itemprops[5].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[3]}:</strong> {itemprops[6].get_text(strip=True)} y {itemprops[7].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[4]}:</strong> {itemprops[8].get_text(strip=True)} y {itemprops[9].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[5]}:</strong> {itemprops[10].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[6]}:</strong> cerrado</li>\n'
                        '</ul>\n')
        elif len(itemprops) == 12:
            horario_html=('<ul>\n'
                        f'\t<li><strong>{dias[0]}:</strong> {itemprops[0].get_text(strip=True)} y {itemprops[1].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[1]}:</strong> {itemprops[2].get_text(strip=True)} y {itemprops[3].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[2]}:</strong> {itemprops[4].get_text(strip=True)} y {itemprops[5].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[3]}:</strong> {itemprops[6].get_text(strip=True)} y {itemprops[7].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[4]}:</strong> {itemprops[8].get_text(strip=True)} y {itemprops[9].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[5]}:</strong> {itemprops[10].get_text(strip=True)} y {itemprops[11].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[6]}:</strong> cerrado</li>\n'
                        '</ul>\n')
        elif len(itemprops) == 13:
            horario_html=('<ul>\n'
                        f'\t<li><strong>{dias[0]}:</strong> {itemprops[0].get_text(strip=True)} y {itemprops[1].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[1]}:</strong> {itemprops[2].get_text(strip=True)} y {itemprops[3].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[2]}:</strong> {itemprops[4].get_text(strip=True)} y {itemprops[5].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[3]}:</strong> {itemprops[6].get_text(strip=True)} y {itemprops[7].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[4]}:</strong> {itemprops[8].get_text(strip=True)} y {itemprops[9].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[5]}:</strong> {itemprops[10].get_text(strip=True)} y {itemprops[11].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[6]}:</strong> {itemprops[12].get_text(strip=True)}</li>\n' 
                        '</ul>\n')
        elif len(itemprops) == 14:
            horario_html=('<ul>\n'
                        f'\t<li><strong>{dias[0]}:</strong> {itemprops[0].get_text(strip=True)} y {itemprops[1].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[1]}:</strong> {itemprops[2].get_text(strip=True)} y {itemprops[3].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[2]}:</strong> {itemprops[4].get_text(strip=True)} y {itemprops[5].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[3]}:</strong> {itemprops[6].get_text(strip=True)} y {itemprops[7].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[4]}:</strong> {itemprops[8].get_text(strip=True)} y {itemprops[9].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[5]}:</strong> {itemprops[10].get_text(strip=True)} y {itemprops[11].get_text(strip=True)}</li>\n'
                        f'\t<li><strong>{dias[6]}:</strong> {itemprops[12].get_text(strip=True)} y {itemprops[13].get_text(strip=True)}</li>\n' 
                        '</ul>\n')
        return horario_html  

    '''
    def obten_horario_html(self):
        if self.horario=="":
            return ""

        inicio_lunes=self.horario.find("lunes,")
        final_lunes=self.horario.find(";",inicio_lunes+6)
        lunes=self.horario[inicio_lunes+6:final_lunes].lower()
        if final_lunes==-1:
            final_lunes=len(self.horario)

        inicio_martes=self.horario.find("martes,")
        final_martes=self.horario.find(";",inicio_martes+7)
        martes=self.horario[inicio_martes+7:final_martes].lower()
        if final_martes==-1:
            final_martes=len(self.horario)

        inicio_miercoles=self.horario.find("miércoles,")
        final_miercoles=self.horario.find(";",inicio_miercoles+10)
        miercoles=self.horario[inicio_miercoles+10:final_miercoles].lower()
        if final_miercoles==-1:
            final_miercoles=len(self.horario)

        inicio_jueves=self.horario.find("jueves,")
        final_jueves=self.horario.find(";",inicio_jueves+7)
        jueves=self.horario[inicio_jueves+7:final_jueves].lower()
        if final_jueves==-1:
            final_jueves=len(self.horario)

        inicio_viernes=self.horario.find("viernes,")
        final_viernes=self.horario.find(";",inicio_viernes+8)
        viernes=self.horario[inicio_viernes+8:final_viernes].lower()
        if final_viernes==-1:
            final_viernes=len(self.horario)

        inicio_sabado=self.horario.find("sábado,")
        final_sabado=self.horario.find(";",inicio_sabado+7)
        sabado=self.horario[inicio_sabado+7:final_sabado].lower()
        if final_sabado==-1:
            final_sabado=len(self.horario)

        inicio_domingo=self.horario.find("domingo,")
        final_domingo=self.horario.find(";",inicio_domingo+9)
        if final_domingo==-1:
            final_domingo=len(self.horario)
        domingo=self.horario[inicio_domingo+9:final_domingo].lower()

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
        '''