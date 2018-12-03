class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化汽车属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁性描述信息"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """打印出一条汽车里程的消息"""
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        """将里程表数值设置为指定值并禁止回调"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer.")


    def increment_odometer(self, miles):
        """将里程表增加指定数值"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer.")


class ElectricCar(Car):
    """电动车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super(ElectricCar, self).__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """打印一条描述电瓶容量的信息"""
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')

class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

#my_new_car = Car('audi', 'A6', 2018)
#print(my_new_car.get_descriptive_name())
#my_new_car.read_odometer()
my_tesla = ElectricCar('tesla', 'model s', 2018)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
