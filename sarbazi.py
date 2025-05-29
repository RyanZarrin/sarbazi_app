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


srb1 = Sarbazi(2331, "123456", "2010-02-03", "2012-02-03", "Tehran", "Officer", "Ali Sardari")
srb2 = Sarbazi("2341", "123543", "2010-03-04","2013-05-01","Tabriz", "Soldier", "Parsa Kalantari")

print(srb1.id)
print(srb1.serial_number)
print(srb1.start_date)
print(srb1.end_date)
print(srb1.city)
print(srb1.organ)
print(srb1.full_name)
srb1.save()
print(srb2.id)
print(srb2.serial_number)
print(srb2.start_date)
print(srb2.end_date)
print(srb2.city)
print(srb2.organ)
print(srb2.full_name)
srb2.save()