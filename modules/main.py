from classes import Angle, Position, DeadReckoning

Salida = Position()

Llegada = Position()

Estima = DeadReckoning()

Salida = Position.get_position(Salida)

Llegada = DeadReckoning.dead_reckoning(Estima, Salida)


Position.position_console_print(Salida)

Position.position_console_print(Llegada)
