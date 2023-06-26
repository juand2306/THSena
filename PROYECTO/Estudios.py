from Persona import *

class Estuduios():
    def __init__(self, nivel_acad, fecha_fin, insEdu):
        self.__nivel_acad = nivel_acad
        self.__fecha_fin = fecha_fin
        self.__insEdu = insEdu
            
    def setNivel_acad(self,niv_acad):
        self.__nivel_acad=niv_acad
        
    def getNivel_acad(self):
        return self.__nivel_acad
    
    
    def setFecha_fin(self,fecha_fin):
        self.__fecha_fin=fecha_fin
        
    def getFecha_fin(self):
        return self.__fecha_fin
    
    
    def setInsEdu(self,insEdu):
        self.__insEdu=insEdu
        
    def getInsEdu(self):
        return self.__insEdu
    