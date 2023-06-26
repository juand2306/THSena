class Seleccionador:
    def __init__(self, id,usuario,contraseña):
        self.__id=id
        self.__usuario=usuario
        self.__contraseña=contraseña       

    def get_id(self):
        return self.__id
    def set_id(self,id):
        self.__id=id

    def get_usuario(self):
        return self.__usuario
    def set_usuario(self,usuario):
        self.__usuario=usuario

    def get_contraseña(self):
        return self.__contraseña
    def set_contraseña(self,contraseña):
        self.__contraseña=contraseña

"""
    def consultar_proceso_vacantes(self):
     
    def Seguimiento_vacantes(self):
       
    def Citar_pos_entrevistas(self):

    def Registrar_resultados(self):
"""
    
    