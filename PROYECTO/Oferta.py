from Empresa import *
from Vacante import *
from sys import *

class Oferta():
    def __init__(self,salario, ubicacion, tip_contrato,fecha_publi, fecha_cierre):
        self.__cargos = []
        self.__salario = salario
        self.__ubicacion = ubicacion
        self.__tip_contrato = tip_contrato
        self.__habilidades = []
        self.__fecha_publi = fecha_publi
        self.__fecha_cierre = fecha_cierre
        
    def agegarCargo(self,cargo):
        self.__cargos.append(cargo)
        
    
    def setSalrio(self,salario):
        self.__salario=salario
        
    def getSalario(self):
        return self.__salario
    
    
    def setUbicacion(self,ubicacion):
        self.__ubicacion=ubicacion
        
    def getUbicacion(self):
        return self.__ubicacion
    
    
    def setTip_contrato(self,tip_contrato):
        self.__tip_contrato=tip_contrato
        
    def getTip_contrato(self):
        return self.__tip_contrato
    
    
    def ingresarHabilidades(self,habilidad):
        self.__habilidades.append(habilidad)
    
    
    def setFecha_publi(self,fecha_publi):
        self.__fecha_publi=fecha_publi
        
    def getFecha_publi(self):
        return self.__fecha_publi
    
    
    def setFecha_cierre(self, fecha_cierre):
        self.__fecha_cierre = fecha_cierre
        
    def getFecha_cierre(self):
        return self.__fecha_cierre
    
    
    def crearFichaInfo(self):
        print(self.__cargos)
        print(self.__salario)
        print(self.__ubicacion)
        print(self.__tip_contrato)
        print(self.__habilidades)
        print(self.__fecha_publi)
        print(self.__fecha_cierre)
        
    def filtrarOfertas(self, buscar):
        pass
    
    