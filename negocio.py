
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
        if pagina_web!=None:
            self.web=html.escape(str(pagina_web))
        else:
            self.web=None
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
        if (imagen!=None):
            if (imagen=="//estaticos.paginasamarillas.es/paginasamarillas/9_11_2/ficha/images/empty.png"):
                self.imagen=None
            else:self.imagen=html.escape(str(imagen))
        else:
            self.imagen=None
        self.facebook=html.escape(str(facebook))
        self.instagram=html.escape(str(instagram))
        self.x=x
        self.youtube=html.escape(str(youtube))        
        self.horario=limpia_comillas(horario)
        self.descripcion_seo=html.escape(str(descripcion_seo))
        
   
    def __str__(self):
        return f'nombre={self.nombre} ciudad={self.ciudad}'
    
    def obten_horario_schema(self):
        dias=['Mo','Tu','We','Th','Fr','Sa','Su']
        soup = BeautifulSoup(self.horario, "html.parser")
        soup.prettify()
        if self.horario=="":
            return ""
        datetimes = soup.select('time[datetime]')
        horario_schema='\t\t"openingHours": [\n'
                        
        if len(datetimes) == 5:
            horario_schema+=(f'\t\t"{dias[0]} {datetimes[0].get_text(strip=True)}",\n'
                        f'\t\t"{dias[1]} {datetimes[1].get_text(strip=True)}",\n'
                        f'\t\t"{dias[2]} {datetimes[2].get_text(strip=True)}",\n'
                        f'\t\t"{dias[3]} {datetimes[3].get_text(strip=True)}",\n'
                        f'\t\t"{dias[4]} {datetimes[4].get_text(strip=True)}",\n'
                        '\t\t"Sa closed",\n'
                        '\t\t"Su closed"\n'                        
                        '\t\t],\n'
            )
            return horario_schema
        elif len(datetimes) == 6:   
            horario_schema+=(f'\t\t"{dias[0]} {datetimes[0].get_text(strip=True)}",\n'
                        f'\t\t"{dias[1]} {datetimes[1].get_text(strip=True)}",\n'
                        f'\t\t"{dias[2]} {datetimes[2].get_text(strip=True)}",\n'
                        f'\t\t"{dias[3]} {datetimes[3].get_text(strip=True)}",\n'
                        f'\t\t"{dias[4]} {datetimes[4].get_text(strip=True)}",\n'
                        f'\t\t"{dias[5]} {datetimes[5].get_text(strip=True)}",\n'
                        f'\t\t"{dias[6]} closed"\n'                        
                        '\t\t],\n'
            )
            return horario_schema
        elif len(datetimes) == 7:
            horario_schema+=(f'\t\t"{dias[0]} {datetimes[0].get_text(strip=True)}",\n'
                        f'\t\t"{dias[1]} {datetimes[1].get_text(strip=True)}",\n'
                        f'\t\t"{dias[2]} {datetimes[2].get_text(strip=True)}",\n'
                        f'\t\t"{dias[3]} {datetimes[3].get_text(strip=True)}",\n'
                        f'\t\t"{dias[4]} {datetimes[4].get_text(strip=True)}",\n'
                        f'\t\t"{dias[5]} {datetimes[5].get_text(strip=True)}",\n'
                        f'\t\t"{dias[6]} {datetimes[6].get_text(strip=True)}"\n'                        
                        '\t\t],\n'
            )
            return horario_schema
        elif len(datetimes) == 10:
            horario_schema+=(f'\t\t"{dias[0]} {datetimes[0].get_text(strip=True)} '
                        f'{datetimes[1].get_text(strip=True)}",\n'
                        f'\t\t"{dias[1]} {datetimes[2].get_text(strip=True)} '
                        f'{datetimes[3].get_text(strip=True)}",\n'
                        f'\t\t"{dias[2]} {datetimes[4].get_text(strip=True)} '
                        f'{datetimes[5].get_text(strip=True)}",\n'
                        f'\t\t"{dias[3]} {datetimes[6].get_text(strip=True)} '
                        f'{datetimes[7].get_text(strip=True)}",\n'
                        f'\t\t"{dias[4]} {datetimes[8].get_text(strip=True)} '
                        f'{datetimes[9].get_text(strip=True)}"\n'
                        '\t\t],\n'
            )
            return horario_schema
        elif len(datetimes) == 11:
            horario_schema+=(f'\t\t"{dias[0]} {datetimes[0].get_text(strip=True)} '
                        f'{datetimes[1].get_text(strip=True)}",\n'
                        f'\t\t"{dias[1]} {datetimes[2].get_text(strip=True)} '
                        f'{datetimes[3].get_text(strip=True)}",\n'
                        f'\t\t"{dias[2]} {datetimes[4].get_text(strip=True)} '
                        f'{datetimes[5].get_text(strip=True)}",\n'
                        f'\t\t"{dias[3]} {datetimes[6].get_text(strip=True)} '
                        f'{datetimes[7].get_text(strip=True)}",\n'
                        f'\t\t"{dias[4]} {datetimes[8].get_text(strip=True)} '
                        f'{datetimes[9].get_text(strip=True)}",\n'
                        f'\t\t"{dias[5]} {datetimes[10].get_text(strip=True)}"\n '
                        '\t\t],\n'
            )
            return horario_schema
        elif len(datetimes) == 12:
            horario_schema+=(f'\t\t"{dias[0]} {datetimes[0].get_text(strip=True)} '
                        f'{datetimes[1].get_text(strip=True)}",\n'
                        f'\t\t"{dias[1]} {datetimes[2].get_text(strip=True)} '
                        f'{datetimes[3].get_text(strip=True)}",\n'
                        f'\t\t"{dias[2]} {datetimes[4].get_text(strip=True)} '
                        f'{datetimes[5].get_text(strip=True)}",\n'
                        f'\t\t"{dias[3]} {datetimes[6].get_text(strip=True)} '
                        f'{datetimes[7].get_text(strip=True)}",\n'
                        f'\t\t"{dias[4]} {datetimes[8].get_text(strip=True)} '
                        f'{datetimes[9].get_text(strip=True)}",\n'
                        f'\t\t"{dias[5]} {datetimes[10].get_text(strip=True)} '
                        f'{datetimes[11].get_text(strip=True)}"\n'
                        '\t\t],\n'
            )
            return horario_schema
        elif len(datetimes) == 13:  
            horario_schema+=(f'\t\t"{dias[0]} {datetimes[0].get_text(strip=True)} '
                        f'{datetimes[1].get_text(strip=True)}",\n'
                        f'\t\t"{dias[1]} {datetimes[2].get_text(strip=True)} '
                        f'{datetimes[3].get_text(strip=True)}",\n'
                        f'\t\t"{dias[2]} {datetimes[4].get_text(strip=True)} '
                        f'{datetimes[5].get_text(strip=True)}",\n'
                        f'\t\t"{dias[3]} {datetimes[6].get_text(strip=True)} '
                        f'{datetimes[7].get_text(strip=True)}",\n'
                        f'\t\t"{dias[4]} {datetimes[8].get_text(strip=True)} '
                        f'{datetimes[9].get_text(strip=True)}",\n'
                        f'\t\t"{dias[5]} {datetimes[10].get_text(strip=True)} '
                        f'{datetimes[11].get_text(strip=True)}",\n'
                        f'\t\t"{dias[6]} {datetimes[12].get_text(strip=True)}"\n'                                     
                        '\t\t],\n'
            )
            return horario_schema
        elif len(datetimes) == 14:  
            horario_schema+=(f'\t\t"{dias[0]} {datetimes[0].get_text(strip=True)} '
                        f'{datetimes[1].get_text(strip=True)}",\n'
                        f'\t\t"{dias[1]} {datetimes[2].get_text(strip=True)} '
                        f'{datetimes[3].get_text(strip=True)}",\n'
                        f'\t\t"{dias[2]} {datetimes[4].get_text(strip=True)} '
                        f'{datetimes[5].get_text(strip=True)}",\n'
                        f'\t\t"{dias[3]} {datetimes[6].get_text(strip=True)} '
                        f'{datetimes[7].get_text(strip=True)}",\n'
                        f'\t\t"{dias[4]} {datetimes[8].get_text(strip=True)} '
                        f'{datetimes[9].get_text(strip=True)}",\n'
                        f'\t\t"{dias[5]} {datetimes[10].get_text(strip=True)} '
                        f'{datetimes[11].get_text(strip=True)}",\n'
                        f'\t\t"{dias[6]} {datetimes[12].get_text(strip=True)} '
                        f'{datetimes[13].get_text(strip=True)}"\n'                        
                        '\t\t],\n'
            )
            return horario_schema

        
    def obten_horario_lista_html(self):
        dias=['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo']
        soup = BeautifulSoup(self.horario, "html.parser")
        soup.prettify()
        if self.horario=="":
            return ""
        itemprops = soup.select('time[itemprop="openingHours"]')
        print(f'{self.nombre} Itemprops length: {len(itemprops)}')
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

    