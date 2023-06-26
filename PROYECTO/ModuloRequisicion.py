from FormularioRequisicion import *
from RevisionAprobacion import *
from PaginaRequisicion import *

class ModuloRequisicion:
    def __init__(self):
        self.formulario = FormularioRequisicion()
        self.revision_aprobacion = RevisionAprobacion()
        self.pagina_requisicion = PaginaRequisicion()
        self.requisiciones = []

    def crearRequisicion(self, tituloPuesto, descripcion, responsabilidades, habilidadesRequeridas, experienciaRequerida, requisitosEducativos, competenciasNecesarias, ubicacion, salario):
        requisicion = self.formulario.completarFormulario(tituloPuesto, descripcion, responsabilidades, habilidadesRequeridas, experienciaRequerida, requisitosEducativos, competenciasNecesarias, ubicacion, salario)
        self.revision_aprobacion.revisar(requisicion)
        self.revision_aprobacion.aprobar(requisicion)
        return requisicion

    def publicar_requisicion(self):
        titulo_puesto = input("Ingrese el título del puesto: ")
        descripcion = input("Ingrese la descripción: ")
        responsabilidades = input("Ingrese las responsabilidades: ")
        habilidades_requeridas = input("Ingrese las habilidades requeridas: ")
        experiencia_requerida = input("Ingrese la experiencia requerida: ")
        requisitos_educativos = input("Ingrese los requisitos educativos: ")
        competencias_necesarias = input("Ingrese las competencias necesarias: ")
        ubicacion = input("Ingrese la ubicación: ")
        salario = input("Ingrese el salario: ")

        requisicion = self.crearRequisicion(titulo_puesto, descripcion, responsabilidades, habilidades_requeridas, experiencia_requerida, requisitos_educativos, competencias_necesarias, ubicacion, salario)
        self.publicarRequisicion(requisicion)
        print("Requisición publicada correctamente.")



        

    def buscarRequisiciones(self, criterios):
        requisiciones_encontradas = []
        for requisicion in self.requisiciones:
            if criterios in requisicion.descripcion:
                requisiciones_encontradas.append(requisicion)
        return requisiciones_encontradas
