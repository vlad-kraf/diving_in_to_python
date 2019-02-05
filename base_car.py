import os
import csv



class CarBase:

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        pass

    def get_photo_file_ext(self, photo_file_name):
        photo_file_ext = os.path.splitext(photo_file_name)
        return photo_file_ext


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


class DataCreator:
    def __init__(self, csv_filename="cars_week3.csv"):
        self.csv_filename = csv_filename
        data = list()
        self.data = data

        with open(csv_filename) as csv_fd:
            reader = csv.reader(csv_fd, delimiter=';')
            next(reader)  # пропускаем заголовок
            for row in reader:
                data.append(row)
