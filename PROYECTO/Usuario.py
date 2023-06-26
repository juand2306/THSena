from sys import *

class Usuario: 
    def __init__(self,nombre,contraseña,correo,telefono):
        self.__nombre=nombre
        self.__contraseña=contraseña
        self.__correo= correo
        self.__telefono=telefono
        
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
    
    