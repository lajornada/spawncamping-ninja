# --*-- coding: utf8 --*--
"""
Implementacion de la aplicación que controla si se puede o no circular.
"""

from datetime import datetime

from vehiculos import Motocicleta
from vehiculos import Carro
from vehiculos import Bus

from restricciones import RESTRICCION_BASE
from restricciones import RESTRICCION_DIAS_MOTOS
from restricciones import RESTRICCION_EDAD_CARROS
from restricciones import RESTRICCION_DIAS_CARROS_X_EDAD

from utils import verificacion


def main():
    cviejo = Carro('001LLL', 1910)
    cnuevo = Carro('003LLL', 2000)
    moto = Motocicleta('005LLLLLLLL', 1000)
    bus = Bus('007', 3000)

    print "carro viejo"
    for dia in range(7):
        print "dia: %i, resultado: %s" \
            % (dia, str(verificacion(cviejo, dia)))
    print "carro nuevo"
    for dia in range(7):
        print "dia: %i, resultado: %s" \
            % (dia, str(verificacion(cnuevo, dia)))

    print "moto"
    for dia in range(7):
        print "dia: %i, resultado: %s" \
            % (dia, str(verificacion(moto, dia)))

    print "bus"
    for dia in range(7):
        print "dia: %i, resultado: %s" \
            % (dia, str(verificacion(bus, dia)))

if __name__ == '__main__':
    main()
