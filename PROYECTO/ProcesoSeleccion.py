class procesoSeleccion:
     def __init__(self, valida_requisicion, pruebas_psicotecnicas, soportes_academicos):
          
          self.__valida_requisicion= False
          self.__pruebas_psicotecnicas=False
          self.__soportes_academicos =False
          self.__estado_proceso= "Pendiente"
          self.__resultado_proceso= None
          
     def validar_procesos(self):
          if self.__valida_requisicion and self.pruebas_psicotecnicas and self.soportes_academicos:
               self.__estado_proceso= "valido"
      
    
     def get_valida_requisicion(self):
          return self.__valida_requisicion
     
     def set_valida_requisicion(self, valida_requisicion):
          self.__valida_requisicion= valida_requisicion


     def get_pruebas_psicotecnicas(self):
          return self.__pruebas_psicotecnicas
     
     def set_pruebas_psicotecnicas(self, pruebas_psicotecnicas):
          self.__pruebas_psicotecnicas= pruebas_psicotecnicas


     def get_soportes_academicos(self):
          return self.__soportes_academicos
     
     def set_soportes_academicos(self, soportes_academicos):
          self.__soportes_academicos= soportes_academicos





     """"
     def get_resultado_proceso(self):
          return self.__resultado_proceso
    
     def set_resultado_proceso(self, resultado_proceso
       self.__resultado_proceso= resultado_proceso
  """
  


 #proceso = procesoSeleccion()

   
     
    
"""
valida_requisicion=input("El proceso de requisicion del aprendiz es valido?:")
pruebas_psicotecnicas=input("Aprobo las pruebas psicotecnicas:")
soportes_academicos=input("Los soprtes academicos cumplen:")



procesoSeleccion1= procesoSeleccion (valida_requisicion, pruebas_psicotecnicas, soportes_academicos)

print("procesoSeleccion creado:")
print("valida_requisicion:", procesoSeleccion1.get_valida_requisicion())
print(" pruebas_psicotecnicas:",procesoSeleccion1.get_pruebas_psicotecnicas())
print(" soportes_academicos:",procesoSeleccion1. get_soportes_academicos())

"""


