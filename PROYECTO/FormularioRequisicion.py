from Requisicion import *
import uuid

def generate_requisition_id():
    return str(uuid.uuid4())

class FormularioRequisicion:
    def completarFormulario(self, tituloPuesto, descripcion, responsabilidades, habilidadesRequeridas, experienciaRequerida, requisitosEducativos, competenciasNecesarias, ubicacion, salario):
        requisicionId = generate_requisition_id()  
        requisicion = Requisicion(requisicionId, tituloPuesto, descripcion, responsabilidades, habilidadesRequeridas, experienciaRequerida, requisitosEducativos, competenciasNecesarias, ubicacion, salario)
        return requisicion
