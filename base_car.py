import os
import csv

car_type = 0
brand = 1
passenger_seats_count = 2
photo_file_name = 3
body_whl = 4
carrying = 5
extra = 6


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


class CarBase:
    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(car_obj):
        file_ext = os.path.splitext(car_obj.photo_file_name)
        return file_ext[1]


class Car(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, passenger_seats_count):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, body_whl):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        self.body_whl = body_whl

        if body_whl == '':
            body_width = float(0)
            body_height = float(0)
            body_length = float(0)
        else:
            size = body_whl.split('x')
            body_width = float(size[0])
            body_height = float(size[1])
            body_length = float(size[2])

        self.body_width = body_width
        self.body_height = body_height
        self.body_length = body_length

    def get_body_volume(car_obj):
        return float(car_obj.body_width * car_obj.body_height * car_obj.body_length)


class SpecMachine(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, extra):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        self.extra = extra


def get_car_list(csv_filename="cars_week3.csv"):

    data = list()
    car_list = []

    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            data.append(row)

    for row in data:
        try:
            if row[car_type] == 'car':
                if row[body_whl] != '':
                    z = Car(row[car_type], row[brand], row[photo_file_name], row[carrying], row[passenger_seats_count])
                    car_list.append(z)
                else:
                    z = Car(row[car_type], row[brand], row[photo_file_name], row[carrying], row[passenger_seats_count])
                    car_list.append(z)
            elif row[car_type] == 'truck':
                z = Truck(row[car_type], row[brand], row[photo_file_name], row[carrying], row[body_whl])
                car_list.append(z)
            elif row[car_type] == 'spec_machine':
                z = SpecMachine(row[car_type], row[brand], row[photo_file_name], row[carrying], row[extra])
                car_list.append(z)
            else:
                pass
        except IndexError:
            pass
    return car_list

