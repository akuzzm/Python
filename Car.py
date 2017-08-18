class Car:
    """Class describes Cars"""
    def __init__(self,
                 power,
                 max_speed,
                 color = "Red",
                 car_type = "Sport"):

        self.power = power
        self.color = color
        self.max_speed = max_speed
        self.car_type = car_type
        
    def fuel(self):
        return (self.max_speed*self.power)/1000.0
