class Provincia:
    def __init__(self,nombre,actividades,cabecera,cuerpo):
        self.nombre=nombre
        self.cabecera=cabecera
        self.cuerpo=cuerpo
        self.localidades=[]
        self.actividades=actividades.split(',')
    
    def __str__(self):
        res=f"{self.nombre}\n{self.cabecera}\n{self.cuerpo}"
        aux="" 
        for actividad in self.actividades:
            aux+=actividad+"\n"
        return res+aux
        
    
    def anyade_localidad(self,localidad):
        self.localidades.append(localidad)
    
