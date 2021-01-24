from classes import *

# Cálculo de Estima



Salida = Position()                     # Creates Departure Point within Position class.
Position.get_user_position(Salida)      # Defines Departure Point within Position class.


OwnVessel = Vessel()                    # Creates ownVessel for Vessel Data entry.
Vessel.speed_and_course(OwnVessel)      # Defines ownVessel parameters

sailed_time = Time()
sailed_time = Time.get_user_time(Time)


Calculo = DeadReckoning(OwnVessel)                                   # Creates "calc" for Estima Calculations
DeadReckoning.direct(Calculo, Salida, OwnVessel, sailed_time)        # Calculates Dead Reckoning Parameters

Llegada = Position()

