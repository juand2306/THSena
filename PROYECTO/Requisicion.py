class Requisicion:
    def __init__(self, requisicionId, tituloPuesto, descripcion, responsabilidades, habilidadesRequeridas, experienciaRequerida, requisitosEducativos, competenciasNecesarias, ubicacion, salario):
        self._requisicionId = requisicionId
        self._tituloPuesto = tituloPuesto
        self._descripcion = descripcion
        self._responsabilidades = responsabilidades
        self._habilidadesRequeridas = habilidadesRequeridas
        self._experienciaRequerida = experienciaRequerida
        self._requisitosEducativos = requisitosEducativos
        self._competenciasNecesarias = competenciasNecesarias
        self._ubicacion = ubicacion
        self._salario = salario

    def setRequisicionId(self, requisicionId):
        self._requisicionId = requisicionId

    def getRequisicionId(self):
        return self._requisicionId

    def setTituloPuesto(self, tituloPuesto):
        self._tituloPuesto = tituloPuesto

    def getTituloPuesto(self):
        return self._tituloPuesto

    def setDescripcion(self, descripcion):
        self._descripcion = descripcion

    def getDescripcion(self):
        return self._descripcion

    def setResponsabilidades(self, responsabilidades):
        self._responsabilidades = responsabilidades

    def getResponsabilidades(self):
        return self._responsabilidades

    def setHabilidadesRequeridas(self, habilidadesRequeridas):
        self._habilidadesRequeridas = habilidadesRequeridas

    def getHabilidadesRequeridas(self):
        return self._habilidadesRequeridas

    def setExperienciaRequerida(self, experienciaRequerida):
        self._experienciaRequerida = experienciaRequerida

    def getExperienciaRequerida(self):
        return self._experienciaRequerida

    def setRequisitosEducativos(self, requisitosEducativos):
        self._requisitosEducativos = requisitosEducativos

    def getRequisitosEducativos(self):
        return self._requisitosEducativos

    def setCompetenciasNecesarias(self, competenciasNecesarias):
        self._competenciasNecesarias = competenciasNecesarias

    def getCompetenciasNecesarias(self):
        return self._competenciasNecesarias

    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion

    def getUbicacion(self):
        return self._ubicacion

    def setSalario(self, salario):
        self._salario = salario

    def getSalario(self):
        return self._salario
