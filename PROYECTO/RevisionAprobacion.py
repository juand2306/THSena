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