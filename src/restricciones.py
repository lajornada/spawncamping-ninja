# --*-- coding: utf8 --*--
"""
Definición de las restricciones para la circulación de vehiculos.
"""

RESTRICCION_BASE = {0: (),
                    1: (0, 1),
                    2: (2, 3),
                    3: (4, 5),
                    4: (6, 7),
                    5: (8, 9),
                    6: (),
                    }

RESTRICCION_DIAS_MOTOS = (0, 6)

RESTRICCION_EDAD_CARROS = 10

RESTRICCION_DIAS_CARROS_X_EDAD = (6)
