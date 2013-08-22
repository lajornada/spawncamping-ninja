"""
Modulo de utilidades.
"""


def verificacion(vehiculo, dia):
    """ Verifica si el <vehiculo> puede circular en el <dia>.
    """
    date = datetime.now()
    anio_actual = date.year
    resultado = False
    prohibidos = RESTRICCION_BASE[dia]

    digito = int(vehiculo.placa[2])
    permitido = digito not in prohibidos

    if isinstance(vehiculo, Bus):
        resultado = True

    elif isinstance(vehiculo, Motocicleta):
        resultado = permitido and dia not in RESTRICCION_DIAS_MOTOS

    elif isinstance(vehiculo, Carro):
        restriccion_edad = anio_actual - vehiculo.anio >= RESTRICCION_EDAD_CARROS

        if restriccion_edad:
            resultado = permitido and dia not in RESTRICCION_DIAS_CARROS_X_EDAD
        else:
            resultado = permitido

    return resultado
