class Aspirante():
   def __init__(self,id_aspirante, profesion, id_educacion, id_exp ):
    self.__id_aspirante = id_aspirante
    self.__profesion = profesion
    self.__id_educacion = id_educacion
    self.__id_exp = id_exp

    
    
    def get_id_aspirante(self):
      return self.__id_aspirante

    def set_id_aspirante(self,nuevo_id_aspirante):
       self.__id_aspirante = nuevo_id_aspirante 

    def get_profesion(self):
      return self.__profesion 
    
    def set_profesion(self,nueva_profesion):
      self.__profecion = nueva_profesion
    
    def get_id_educacion(self):
      return self.__id_educacion
    
    def set_id_educacion(self,nuevo_id_educacion):
      self.__id_educacion = nuevo_id_educacion
    
    def get_id_exp(self):
      return self.__id_exp
    
    def set_id_exp(self,nuevo_id_exp):
      self.__id_exp = nuevo_id_exp
