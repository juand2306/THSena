from Oferta import *

class Vacante():
    def __init__(self, vacantes_disp:int, num_postulaciones:int):
        self.__vacantes_disp = vacantes_disp
        self.__num_postulaciones = num_postulaciones
        
    def setVacantes_disp(self, vacantes_disp):
        self.__vacantes_disp = vacantes_disp
        
    def getVacantes_dips(self):
        return self.__vacantes_disp
    
    
    def setNum_postulaciones(self, num_postulaciones):
        self.__num_postulaciones = num_postulaciones
        
    def getNum_postulaciones(self):
        return self.__num_postulaciones

    