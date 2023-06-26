import uuid

def generate_requisition_id():
    return str(uuid.uuid4())

class Requisicion:
    def __init__(self, requisicionId, tituloPuesto, descripcion, responsabilidades, habilidadesRequeridas, experienciaRequerida, requisitosEducativos, competenciasNecesarias, ubicacion, salario):
        self.requisicionId = requisicionId
        self.tituloPuesto = tituloPuesto
        self.descripcion = descripcion
        self.responsabilidades = responsabilidades
        self.habilidadesRequeridas = habilidadesRequeridas
        self.experienciaRequerida = experienciaRequerida
        self.requisitosEducativos = requisitosEducativos
        self.competenciasNecesarias = competenciasNecesarias
        self.ubicacion = ubicacion
        self.salario = salario

    def obtenerDetalles(self):
        return f"Requisición {self.requisicionId}: {self.tituloPuesto} - {self.descripcion}"

    def setRequisicionId(self, requisicionId):
        self._requisicionId = requisicionId

    def setTituloPuesto(self, tituloPuesto):
        self._tituloPuesto = tituloPuesto

    def setDescripcion(self, descripcion):
        self._descripcion = descripcion

    def setResponsabilidades(self, responsabilidades):
        self._responsabilidades = responsabilidades

    def setHabilidadesRequeridas(self, habilidadesRequeridas):
        self._habilidadesRequeridas = habilidadesRequeridas

    def setExperienciaRequerida(self, experienciaRequerida):
        self._experienciaRequerida = experienciaRequerida

    def setRequisitosEducativos(self, requisitosEducativos):
        self._requisitosEducativos = requisitosEducativos

    def setCompetenciasNecesarias(self, competenciasNecesarias):
        self._competenciasNecesarias = competenciasNecesarias

    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion

    def setSalario(self, salario):
        self._salario = salario

    # Getters
    def getRequisicionId(self):
        return self._requisicionId

    def getTituloPuesto(self):
        return self._tituloPuesto

    def getDescripcion(self):
        return self._descripcion

    def getResponsabilidades(self):
        return self._responsabilidades

    def getHabilidadesRequeridas(self):
        return self._habilidadesRequeridas

    def getExperienciaRequerida(self):
        return self._experienciaRequerida

    def getRequisitosEducativos(self):
        return self._requisitosEducativos

    def getCompetenciasNecesarias(self):
        return self._competenciasNecesarias

    def getUbicacion(self):
        return self._ubicacion

    def getSalario(self):
        return self._salario


class FormularioRequisicion:
    def completarFormulario(self, tituloPuesto, descripcion, responsabilidades, habilidadesRequeridas, experienciaRequerida, requisitosEducativos, competenciasNecesarias, ubicacion, salario):
        requisicionId = generate_requisition_id()  
        requisicion = Requisicion(requisicionId, tituloPuesto, descripcion, responsabilidades, habilidadesRequeridas, experienciaRequerida, requisitosEducativos, competenciasNecesarias, ubicacion, salario)
        return requisicion



class RevisionAprobacion:
    def revisar(self, requisicion):
        print(f"Revisando requisición {requisicion.requisicionId}...")
        if (
            requisicion.tituloPuesto
            and requisicion.descripcion
            and requisicion.responsabilidades
            and requisicion.habilidadesRequeridas
            and requisicion.experienciaRequerida
            and requisicion.requisitosEducativos
            and requisicion.competenciasNecesarias
            and requisicion.ubicacion
            and requisicion.salario
        ):
            print("La requisición cumple todos los requisitos.")
        else:
            print("La requisición tiene campos incompletos y no cumple todos los requisitos.")

    def aprobar(self, requisicion):
        print(f"Aprobando requisición {requisicion.requisicionId}...")
        if requisicion.revisada:
            print("La requisición ha sido revisada correctamente y cumple con los criterios establecidos.")
        else:
            print("La requisición no ha sido revisada correctamente o no cumple con los criterios establecidos.")



class PaginaRequisicion:
    def mostrarDetalles(self, requisicion):
        return requisicion.obtenerDetalles()


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

    def publicarRequisicion(self, requisicion):
        self.requisiciones.append(requisicion)
        print(f"La requisición {requisicion.requisicionId} ha sido publicada correctamente.")

    def buscarRequisiciones(self, criterios):
        requisiciones_encontradas = []
        for requisicion in self.requisiciones:
            if criterios in requisicion.descripcion:
                requisiciones_encontradas.append(requisicion)
        return requisiciones_encontradas



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



# Ejemplo de uso
plataforma = PlataformaBusquedaEmpleo()
requisicion = plataforma.modulo_requisicion.crearRequisicion("Desarrollador Python", "Descripción del puesto", "Responsabilidades del puesto", "Habilidades requeridas", "Experiencia requerida", "Requisitos educativos", "Competencias necesarias", "Ubicación del trabajo", 5000)

plataforma.modulo_requisicion.publicarRequisicion(requisicion)
resultados = plataforma.buscarRequisiciones(criterios)
plataforma.aplicarRequisicion(requisicion.requisicionId, datosAplicante)
