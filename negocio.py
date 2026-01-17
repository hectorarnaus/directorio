import html
from bs4 import BeautifulSoup

def limpia_comillas(texto):
    if texto!=None:
        if texto.startswith('"') and texto.endswith('"'):
            texto=texto[1:-1]
    return texto

class Negocio:
    def __init__(self,nombre,direccion,CP,ciudad,provincia,telefono,pagina_web,actividad,actividades_relacionadas,marcas,descripcion,mapa,imagen,facebook,instagram,x,youtube,horario,descripcion_seo,tagline):
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
        self.tagline=tagline
        
   
    def __str__(self):
        return f'nombre={self.nombre} ciudad={self.ciudad}'
    
    def obten_horario_lista(self):
        soup = BeautifulSoup(self.horario, "html.parser")
        soup.prettify()
        if self.horario=="":
            return ""
        dias=soup.select('p')
        res="\t\t<ul>\n"
        for dia in dias:
            res+=f'\t\t\t<li>{dia.get_text(strip=True)}</li>\n'
        res+="\t\t</ul>\n"
        return res

    def obten_horario_schema(self):
        dias=['Mo','Tu','We','Th','Fr','Sa','Su']
        soup = BeautifulSoup(self.horario, "html.parser")
        soup.prettify()
        if self.horario=="":
            return ""
        datetimes = soup.select('time[datetime]')
        horario_schema='\t"openingHours": [\n'
                        
        if len(datetimes) == 5:
            horario_schema+=(
                        f'\t\t"{dias[0]} {datetimes[0].get_text(strip=True)}",\n'
                        f'\t\t"{dias[1]} {datetimes[1].get_text(strip=True)}",\n'
                        f'\t\t"{dias[2]} {datetimes[2].get_text(strip=True)}",\n'
                        f'\t\t"{dias[3]} {datetimes[3].get_text(strip=True)}",\n'
                        f'\t\t"{dias[4]} {datetimes[4].get_text(strip=True)}"\n'
                        #'\t\t"Sa closed",\n'
                        #'\t\t"Su closed"\n'                        
                        '\t\t],\n'
            )
            return horario_schema
        elif len(datetimes) == 6:   
            horario_schema+=(
                        f'\t\t"{dias[0]} {datetimes[0].get_text(strip=True)}",\n'
                        f'\t\t"{dias[1]} {datetimes[1].get_text(strip=True)}",\n'
                        f'\t\t"{dias[2]} {datetimes[2].get_text(strip=True)}",\n'
                        f'\t\t"{dias[3]} {datetimes[3].get_text(strip=True)}",\n'
                        f'\t\t"{dias[4]} {datetimes[4].get_text(strip=True)}",\n'
                        f'\t\t"{dias[5]} {datetimes[5].get_text(strip=True)}"\n'
                        #f'\t\t"{dias[6]} closed"\n'                        
                        '\t\t],\n'
            )
            return horario_schema
        elif len(datetimes) == 7:
            horario_schema+=(
                        f'\t\t"{dias[0]} {datetimes[0].get_text(strip=True)}",\n'
                        f'\t\t"{dias[1]} {datetimes[1].get_text(strip=True)}",\n'
                        f'\t\t"{dias[2]} {datetimes[2].get_text(strip=True)}",\n'
                        f'\t\t"{dias[3]} {datetimes[3].get_text(strip=True)}",\n'
                        f'\t\t"{dias[4]} {datetimes[4].get_text(strip=True)}",\n'
                        f'\t\t"{dias[5]} {datetimes[5].get_text(strip=True)}",\n'
                        f'\t\t"{dias[6]} {datetimes[6].get_text(strip=True)}"\n'                        
                        '\t\t],\n'
            )
            return horario_schema
        
        elif len(datetimes) == 9:
            horario_schema+=(
                        f'\t\t"{dias[0]} {datetimes[0].get_text(strip=True)} '
                        f'{datetimes[1].get_text(strip=True)}",\n'
                        f'\t\t"{dias[1]} {datetimes[2].get_text(strip=True)} '
                        f'{datetimes[3].get_text(strip=True)}",\n'
                        f'\t\t"{dias[2]} {datetimes[4].get_text(strip=True)} '
                        f'{datetimes[5].get_text(strip=True)}",\n'
                        f'\t\t"{dias[3]} {datetimes[6].get_text(strip=True)} '
                        f'{datetimes[7].get_text(strip=True)}",\n'
                        f'\t\t"{dias[4]} {datetimes[8].get_text(strip=True)}"\n'
                        '\t\t],\n'
            )
            return horario_schema
        
        elif len(datetimes) == 10:
            horario_schema+=(
                        f'\t\t"{dias[0]} {datetimes[0].get_text(strip=True)} '
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
            horario_schema+=(
                        f'\t\t"{dias[0]} {datetimes[0].get_text(strip=True)} '
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
            horario_schema+=(
                        f'\t\t"{dias[0]} {datetimes[0].get_text(strip=True)} '
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
            horario_schema+=(
                        f'\t\t"{dias[0]} {datetimes[0].get_text(strip=True)} '
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
            horario_schema+=(
                        f'\t\t"{dias[0]} {datetimes[0].get_text(strip=True)} '
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

    def obten_datos_schema(self,tipo_negocio_schema):
        res=(
            f'\t"@type": "{tipo_negocio_schema}",\n'
            f'\t"name": "{self.nombre}",\n'
            f'\t"image": "{self.imagen}",\n'
            '\t"address": {\n'
            '\t\t"@type": "PostalAddress",\n'
            f'\t\t"streetAddress": "{self.direccion}",\n'
            f'\t\t"addressLocality": "{self.ciudad}",\n'
            f'\t\t"addressRegion": "{self.provincia}",\n'
            '\t\t"addressCountry": "ES"\n'
            '\t\t},\n'
            f'\t"telephone": "{self.telefono}",\n'
            )
        res+=f'{self.obten_horario_schema()}'
        res+=f'\t"url": "{self.web}"\n'
        return res