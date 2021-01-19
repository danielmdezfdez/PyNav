import math


class Angle():
    def __init__(self):
        pass

    def sexagesimal_user_input(self, valor_entrada):
        "Transforms user data input in form GG MM.mm into GG.gg."

        x=input(valor_entrada)

        degrees, minutes=x.split()
        degrees=float(degrees)
        minutes=float(minutes)

        if degrees<0:
            minutes=minutes*(-1)

        decimal_degrees=round(degrees+(minutes/60), 6)

        return decimal_degrees


    def sexagesimal_console_print(self, valor):
        "Transforms decimal degrees into sexagesimal degrees for data printing."

        grados = int(valor)
        minutos = valor - int(valor)
        minutos = abs(minutos*60)

        minutos = round(minutos, 2)

        solution = str(grados) + "º " + str(minutos) + "'"

        return solution




class Position():
    'Class to define vessel position through a '
    def __init__(self): # Inicializa la clase
        self.coordinates = [0, 0]



    def get_position(self): # Pide al usuario que introduzca una latitud y longitud
        'Asks user for a new position on decimal coordinates which is returned on a tuple'

        self.latitude = Angle.sexagesimal_user_input(self, "Latitude (GG MM.mm): ")

        self.longitude = Angle.sexagesimal_user_input(self, "Longitude(GG MM.mm): ")

        self.coordinates = [self.latitude, self.longitude]

        return [self.latitude, self.longitude]


    def position_console_print(self):                                               # HAY QUE ARREGLAR ESTOOOOOOO
        "Prints on screen Latitude and Longitude on DD MM format."
        
        self.coordinates = Position

        self.decimal_latitude = self.coordinates[0]
        self.decimal_longitude = self.coordinates[1]

        self.sex_latitude = Angle.sexagesimal_console_print(self, self.decimal_latitude)
        self.sex_longitude = Angle.sexagesimal_console_print(self, self.decimal_longitude)

        self.position_sexagesimal_coordinates = [self.sex_latitude, self.sex_longitude]

        print(self.position_sexagesimal_coordinates)



        


class DeadReckoning():
    def __init__(self):
        pass
    
    def dead_reckoning(self, departure_position):

        "Makes all Dead Reckoning Calculations."

        self.coordinates = departure_position

        self.departure_latitude = self.coordinates[0]      
        self.departure_longitude = self.coordinates[1]


        self.ellapsed_time = float(input("Ellapsed Time (HH:MM:SS): "))
        
        self.course = float(input("Course: "))
        self.course_radians = math.radians(self.course)
        
        self.vessel_speed = float(input("Vessel Speed (kn): "))
        
        self.distance = self.ellapsed_time * self.vessel_speed


        self.delta_latitude = (self.distance/60)*math.cos(self.course_radians)

        self.arrival_latitude = self.departure_latitude + self.delta_latitude


        self.latitude_average = self.departure_latitude + self.arrival_latitude
        self.apartamiento = (self.distance/60)*math.sin(self.course_radians)
        self.delta_longitude = self.apartamiento / math.cos(math.radians(self.latitude_average))
        self.arrival_longitude = self.departure_longitude + self.delta_longitude


        #self.arrival_longitude = round(self.arrival_longitude, 2)
        #self.arrival_latitude = round(self.arrival_latitude, 2)
        
        #print([self.arrival_latitude, self.arrival_longitude])


        return [self.arrival_latitude, self.arrival_longitude]