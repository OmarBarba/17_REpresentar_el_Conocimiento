def diagnostico_enfermedad(sintomas):
    if "fiebre" in sintomas and "tos" in sintomas:
        return "Posible gripe"
    elif "dolor_de_cabeza" in sintomas and "cansancio" in sintomas:
        return "Posible migraña"
    else:
        return "No se puede determinar la enfermedad"

sintomas_paciente = ["fiebre", "tos"]
resultado_diagnostico = diagnostico_enfermedad(sintomas_paciente)
print(f"Diagnóstico: {resultado_diagnostico}")
