import math

# Definimos las clases con las que vamos a trabajar



class Angle():
    def __init__(self):
        pass

    def sexagesimal_user_input(self, valor_entrada):

        x=input(valor_entrada)

        degrees, minutes=x.split()
        degrees=float(degrees)
        minutes=float(minutes)

        if degrees<0:
            minutes=minutes*(-1)

        decimal_degrees=round(degrees+(minutes/60), 6)

        return decimal_degrees


    def sexagesimal_console_print(valor):

        grados = int(valor)

        minutos = valor - int(valor)

        minutos = abs(minutos*60)

        solution = str(grados) + "º " + str(minutos) + "'"

        print(solution)

        return solution








class Position():
    'Class to define vessel position'
    def __init__(self): # Inicializa la clase
        pass

    def get_position(self): # Pide al usuario que introduzca una latitud y longitud
        'Asks user for a new position on decimal coordinates which is returned on a tuple'

        self.latitude = Angle.sexagesimal_user_input(self, "Latitude: ")

        self.longitude = Angle.sexagesimal_user_input(self, "Longitude: ")

        self.departure_position = [self.latitude, self.longitude]

        return [self.latitude, self.longitude]


class Estima():
    def __init__(self):
        pass

    def calculation(self, position):

        self.departure_position = Position.get_position(position)
        self.departure_latitude = self.departure_position[0]        
        self.departure_longitude = self.departure_position[1]


        self.ellapsed_time = float(input("Ellapsed Time (HH:MM:SS): "))
        self.course = float(input("Course: "))
        self.vessel_speed = float(input("Vessel Speed (kn): "))
        self.distance = self.ellapsed_time * self.vessel_speed


        self.delta_latitude = (self.distance/60)*math.cos(self.course)
        self.arrival_latitude = self.departure_latitude + self.delta_latitude


        self.latitude_average = self.departure_latitude + self.arrival_latitude
        self.apartamiento = (self.distance/60)*math.sin(self.course)
        self.delta_longitude = self.apartamiento / math.cos(self.latitude_average)
        self.arrival_longitude = self.departure_longitude + self.delta_longitude
        
        print([self.arrival_latitude, self.arrival_longitude])


        return [self.arrival_latitude, self.arrival_longitude]



Salida = Position()

Llegada = Position()

Estim = Estima()

Estima.calculation(Estim, Salida)


