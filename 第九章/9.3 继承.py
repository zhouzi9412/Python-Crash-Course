####子类的方法__init__()，可以编写另一个现成的类的特殊版本，一个类继承另一个类时，将获得另一个类的所有属性和方法

class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
        
    def increment_odometer(self, miles):
        self.odometer_reading += miles                                          #父类必须在子类之前

class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):                                      #__init__接收Car实例的所有信息
        """初始化父类的属性""" 
        super().__init__(make, model, year)                                     #super()函数将子类与父类联系在一起，使子类包含父类的所有属性，也称超类

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

####给子类定义属性和方法####

class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
        
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    """电动车的独特之处"""
    def __init__(self, make, model, year):
        """
        电动车的独特之处
        初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery_size = 70                                               #添加了新属性battery，子类所有实例都包括，父类实例都不包括
    
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

####重写父类的方法####

class ElectricCar(Car):
    --snip--

    def fill_gas_tank(self):                                                 #油箱对电动汽车毫无意义，所以可调用此函数替换父类中的相同函数，父类将转而运行此代码
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")

####将实例用作属性####用于将类的一部分提取出来

class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
        
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():                                                               #定义一个battery新类，且无继承
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size=70):                                       #定义一个形参battery_size，且默认值为70
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """
        初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery = battery()                                               #创建一个battery实例，__init__调用时都将执行该操作

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()                                            #调用battery
