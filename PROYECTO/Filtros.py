

class Filtros():
    def __init__(self, rango_salario,rango_exp, tipo_ocupacion, ubicacion_des, horario_des, tipo_cont_des, teletrebajo):
        self.__rango_salario = rango_salario
        self.__rango_exp = rango_exp
        self.__tipo_ocupacion = tipo_ocupacion
        self.__ubicacion_des = ubicacion_des
        self.__horario_des = horario_des
        self.__tipo_cont_des = tipo_cont_des
        self.__teletrabajo = teletrebajo
        
    def setRango_salario(self,rango_salario):
        self.__rango_salario=rango_salario
        
    def getRango_salario(self):
        return self.__rango_salario
    
    
    def setRango_exp(self,rango_exp):
        self.__rango_exp=rango_exp
        
    def getRango_exp(self):
        return self.__rango_exp
    
    
    def setTipo_ocupacion(self,tipo_ocupacion):
        self.__tipo_ocupacion=tipo_ocupacion
        
    def getTipo_ocupacion(self):
        return self.__tipo_ocupacion
    
    
    def setUbicacion_des(self,Ubicacion_des):
        self.__ubicacion_des=Ubicacion_des
        
    def getTelefono(self):
        return self.__ubicacion_des
    
    
    def setHorario_des(self,horario_des):
        self.__horario_des=horario_des
        
    def getHorario_des(self):
        return self.__horario_des
    
    def setTipo_cont_des(self,tipo_cont_des):
        self.__tipo_cont_des = tipo_cont_des
        
    def getTipo_cont_des(self):
        return self.__tipo_cont_des
    
    def setTeletrabajo(self,teletrabajo:bool):
        self.__teletrabajo = teletrabajo
        
    def getTeletrabajo(self):
        return self.__teletrabajo