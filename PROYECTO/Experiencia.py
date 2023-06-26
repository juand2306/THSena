from Persona import *

class Experiencia():
    def __init__(self, tiempo, actividades_realizadas,cargo_lab):
        self.__tiempo = tiempo
        self.__actividades_realizadas = actividades_realizadas
        self.__cargo_lab = cargo_lab
        
    def setTiempo(self,tiempo):
        self.__tiempo=tiempo
        
    def getTiempo(self):
        return self.__tiempo
    
    
    def setActividades_realizadas(self,acti_realizadas):
        self.__actividades_realizadas=acti_realizadas
        
    def getActividades_realizadas(self):
        return self.__actividades_realizadas
    
    
    def setCargo_lab(self,cargo_lab):
        self.__cargo_lab=cargo_lab
        
    def getCargo_lab(self):
        return self.__cargo_lab
    