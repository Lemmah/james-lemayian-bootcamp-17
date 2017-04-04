class Car(object):
    def __init__(self, name='General', model='GM', car_type=None, speed=0):
        self.name = name
        self.model = model
        self.car_type = car_type
        self.speed = speed

        if self.name == 'Koenigsegg' or self.name == 'Porshe':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        if self.car_type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4

    def is_saloon(self):
        if self.car_type is not 'trailer':
            self.car_type == 'saloon'
            return True
        return False

    def drive(self, value):
        if value == 3:
            self.speed = 1000
        elif value == 7:
            self.speed = 77
        return self