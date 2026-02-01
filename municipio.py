class Municipio:
    def __init__(self, nombre,provincia):
        self.nombre=nombre
        self.provincia=provincia
        self.actividades=[]
    def anyade_actividad(self,actividad):
        if actividad not in self.actividades:
            self.actividades.append(actividad)
    def esta_actividad(self,actividad):
        return actividad in self.actividades
    def __str__(self):
        return f"Municipio: {self.nombre}, Provincia: {self.provincia}, Actividades: {', '.join(self.actividades)}"
