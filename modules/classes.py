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

class Position():
    "Postion defined through UTM Coordinates [latitude, longitude]"
    def __init__(self, latitude=0.0, longitude=0.0): # Inicializa la clase
        self.latitude = latitude
        self.longitude = longitude
        self.position_coordinates = [latitude, longitude]
        pass

    def get_user_position(self):
        'Asks user for a new position on decimal coordinates which is returned on a tuple'
        self.latitude = Angle.sexagesimal_user_input(self, "Latitude GG MM.m: ")
        self.longitude = Angle.sexagesimal_user_input(self, "Longitude GGG MM.m: ")
        self.departure_position = [self.latitude, self.longitude]
        return [self.latitude, self.longitude]

    def define_position(self):
        "Auxiliary method for defining position."
        return [self.latitude, self.longitude]

class Vessel():
    "Grabs Vessel basic data: Speed and COG"
    def __init__(self, SOG=0.0, COG=0.0):
        self.SOG = SOG
        self.COG = COG
        pass

    def speed_and_course(self):
        "Asks user to define Speed and Course."
        self.SOG = float(input("SOG: "))
        self.COG = float(input("COG: "))
        pass

class Time():
    def __init__(self):
        self.time = 0.0
        pass

    def get_user_time(self):
        self.time = input("Ellapsed Time HH:MM:SS: ")

        hours, minutes, seconds = self.time.split(":")
        hours = float(hours)
        minutes = float(minutes)/60
        seconds = float(seconds)/3600

        self.time = hours + minutes + seconds
        return self.time


class DeadReckoning(Vessel):
    def __init__(self, COG=0, SOG=0, distance = 0 ):
        Vessel.__init__(self, SOG, COG)
        self.distance = distance
    pass

    def direct(self, position, Vessel, time):
        "Calculates Latitude and Longitude differents from Vessel Data and Ellapsed Time"
        self.base_position = Position.define_position(position)          # Defines Departure Positio

        self.SOG = Vessel.SOG                                            # Defines SOG
        self.COG = math.radians(Vessel.COG)                              # Transforms COG into radians

        self.ellapsed_time = float(time)                                 # Gets Time
        self.distance = (self.ellapsed_time*self.SOG)                # Calculates distance in minutes D=(VxT)/60

        self.base_latitude = (self.base_position[0])         # Gets Latitude and Transforms 
        self.base_longitude = (self.base_position[1])        # Gets Latitude and Transforms 

        self.latitude_difference = math.cos(self.COG)*(self.distance/60)     # Calculates Latitude Difference LD=D*cos(COG)

        self.meridian_difference = math.sin(self.COG)*(self.distance/60)        # Calculates Meridian Difference mD=D*sin(COG)

        self.latitude_average = self.base_latitude + (self.latitude_difference/2)

        self.longitude_difference = self.meridian_difference/math.cos(math.radians(self.latitude_average))

        self.latitude_difference = self.latitude_difference
        self.longitude_difference = self.longitude_difference

        
        return [self.latitude_difference, self.longitude_difference]









