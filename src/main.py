# --*-- coding: utf8 --*--
"""
Implementacion de la aplicación que controla si se puede o no circular.
"""

from datetime import datetime

from vehiculos import Motocicleta
from vehiculos import Carro
from vehiculos import Bus

from utils import verificacion


def main():
    cviejo = Carro(1910, '001LLL')
    cnuevo = Carro(2010, '003LLL')
    moto = Motocicleta(10000, '005LLLLLLLL')
    bus = Bus(3000, '007')

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
