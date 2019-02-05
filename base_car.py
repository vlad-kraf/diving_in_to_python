import os

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        pass

    def get_photo_file_ext(self, photo_file_name):
        photo_file_ext = os.path.splitext(photo_file_name)


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        car_type = "car"
        pass


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        car_type = "truck"
        pass


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        car_type = "spec_machine"
        pass


def get_car_list(csv_filename):
    car_list = []
    return car_list