from Oferta import *

class Cargo():
    def __init__(self, nombre, niv_academico, funciones, descripcion, num_cuoc):
        self.__nombre = nombre
        self.__niv_academico = niv_academico
        self.__funciones = funciones
        self.__descripcion = descripcion
        self.__num_cuoc = num_cuoc
        
    def setNombre(self,nombre):
        self.__nombre=nombre
        
    def getNombre(self):
        return self.__nombre
    
    
    def setNiv_academico(self,niv_academico):
        self.__niv_academico=niv_academico
        
    def getontraseña(self):
        return self.__niv_academico
    
    
    def setFunciones(self,funciones):
        self.__funciones=funciones
        
    def getFunciones (self):
        return self.__funciones
    
    
    def setDescripcion(self,descripcion):
        self.__descripcion=descripcion
        
    def getDescripcion(self):
        return self.__descripcion
    
    
    def setNum_cuoc(self, num_cuoc):
        self.__num_cuoc = num_cuoc
        
    def getNum_cuoc(self):
        return self.__num_cuoc
    