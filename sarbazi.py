from validator import payankhedmat_validator

class Sarbazi:
    def __init__(self, id, serial_number, start_date, end_date, city, organ, full_name):
        self.id = id
        self.serial_number = serial_number
        self.start_date = start_date
        self.end_date = end_date
        self.city = city
        self.organ = organ
        self.full_name = full_name

    def save(self):
        print(
            self.id , self.serial_number , self.start_date ,self.end_date,self.city, self.organ , self.full_name, "saved")

    def find_by_serial_number(self):
        print(f"{self.serial_number} Found ")

    def to_tuple(self):
        return(self.id, self.serial_number, self.start_date, self.end_date, self.city, self.organ, self.full_name)

    def validatior(self):
        return payankhedmat_validator(self)