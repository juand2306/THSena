from ModuloRequisicion import *
from PaginaRequisicion import *
class PlataformaBusquedaEmpleo:
    def __init__(self):
        self.modulo_requisicion = ModuloRequisicion()
        self.pagina_requisicion = PaginaRequisicion()

    def buscarRequisiciones(self, criterios):
        return self.modulo_requisicion.buscarRequisiciones(criterios)

    def aplicarRequisicion(self, requisicionId, datosAplicante):
        requisicion = self.pagina_requisicion.mostrarDetalles(requisicionId)
        if self.modulo_requisicion.cumpleRequisitos(requisicion, datosAplicante):
            print("¡Cumple con los requisitos! Puedes postularte a esta requisición.")
        else:
            print("No cumple con los requisitos. No es elegible para postularse a esta requisición.")

class CriteriosBusqueda:
    def __init__(self, ubicacion=None, industria=None, nivel_experiencia=None, nivel_educativo=None, tipo_empleo=None, otros_filtros=None):
        self.ubicacion = ubicacion
        self.industria = industria
        self.nivel_experiencia = nivel_experiencia
        self.nivel_educativo = nivel_educativo
        self.tipo_empleo = tipo_empleo
        self.otros_filtros = otros_filtros

    def mostrar_criterios(self):
        print("Criterios de búsqueda:")
        print("Ubicación:", self.ubicacion)
        print("Industria:", self.industria)
        print("Nivel de experiencia:", self.nivel_experiencia)
        print("Nivel educativo:", self.nivel_educativo)
        print("Tipo de empleo:", self.tipo_empleo)
        print("Otros filtros:", self.otros_filtros)



criterios = CriteriosBusqueda(
    ubicacion="Ciudad de México",
    industria="Tecnología",
    nivel_experiencia="Intermedio",
    nivel_educativo="Licenciatura",
    tipo_empleo="Tiempo completo",
    otros_filtros=["Remoto", "Inglés avanzado"]
)

criterios.mostrar_criterios()


