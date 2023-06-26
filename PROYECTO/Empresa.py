from Usuario import *
from Vacante import *

class Empresa(Usuario):
    def __init__(self, nombre, contraseña, correo, telefono, nit, ubicacion):
        Usuario.__init__(nombre, contraseña, correo, telefono)
        self.__nit=nit
        self.__ubicacion=ubicacion
        
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
    
    
    def setNit(self,nit):
        self.__nit=nit
    
    def getNit(self):
        return self.__nit
    
    
    def setUbicacion(self,ubicacion):
        self.__ubicacion=ubicacion
        
    def getUbicacion(self):
        return self.__ubicacion
    
    
    
def generar_Oferta(self):
    crg=input("Cargo: ")
    slr=input("Salario: ")
    ubi=input("Ubicacion: ")
    tcon=input("Tipo de contrato: ")
    h=input("Habilidades: ")
    fchp=input("Fecha de publicacion: ")
    fchc=input("Fecha de cierrre: ")
    of1=Oferta(slr,ubi,tcon,fchp,fchc)
    of1.agegarCargo(crg)
    of1.ingresarHabilidades(h)
    
