class ListaVacantes:
    def __init__ (self, hoja_de_vida, id_Seleccionados, id_Preseleccionados):
        self.__hoja_de_vida=hoja_de_vida
        self.__id_Seleccionados=id_Seleccionados
        self.__id_Preseleccionados= id_Preseleccionados

    def get_hoja_de_vida(self):
         return self.__hoja_de_vida
     
    def set_hoja_de_vida(self,hoja_de_vida):
         self.__hoja_de_vida=hoja_de_vida


    def get_id_Seleccionado(self):
          return self.__id_Seleccionado
     
    def set_id_Seleccionado(self, id_Seleccionado):
          self.__id_Seleccionado= id_Seleccionado


    def get_soportes_academicos(self):
          return self.__soportes_academicos
     
    def set_id_Preseleccionados(self,id_Preseleccionados):
          self.__id_Preseleccionados= id_Preseleccionados

