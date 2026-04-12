class Localidad:
    def __init__(self,nombre,provincia,actividades,texto):
        self.nombre=nombre
        self.provincia=provincia
        self.texto=texto
        self.actividades=actividades.split(',')
    
    def __str__(self):
        res=f"{self.nombre}\n{self.provincia}\n{self.texto}"
        aux="" 
        for actividad in self.actividades:
            aux+=actividad+"\n"
        return res+aux
        
    