class postulacion :
    def __init__(self ,id_postulacion ,id_aspirante ,id_oferta):
        self.__id_postulacion = id_postulacion
        self.__id_aspirante = id_aspirante
        self.__id_oferta = id_oferta

    def get_id_postulacion(self):
        return self.__id_postulacion
    
    def set_id_postulacion(self, nuv_id_postulacion):
        self.__id_postulacion 

    def get_id_aspirante(self):
        return self.__id_aspirante
    
    def set_id_aspirante (self, nuv__id_aspirante):
        self.__id_aspirante     

    def get_id_oferta(self):
        return self.__id_oferta
    
    def set_id_oferta(self, nuv_id_oferta):
        self.__id_oferta     
        