from Usuario import *

class Persona(Usuario):
    def __init__(self, nombre, contraseña, correo, telefono, profesion):
        Usuario.__init__(nombre, contraseña, correo, telefono)
        self.__profesion=profesion
        
    def setNombre(self,nombre):
        self.__nombre=nombre
        
    def getNombre(self):
        return self.__nombre
    
    
    def setContraseña(self,contraseña):
        self.__contraseña=contraseña
        
    def getontraseña(self):
        return self.__contraseña
    
    
    def setCorreo(self,correo):
        self.__correo=correo
        
    def getCorreo (self):
        return self.__correo
    
    
    def setTelefono(self,telefono):
        self.__telefono=telefono
        
    def getTelefono(self):
        return self.__telefono
    
    
    def setProfesion(self,profesion):
        self.__profesion=profesion
        
    def getProfesion(self):
        return self.__profesion
    