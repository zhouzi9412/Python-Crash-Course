####导入类####

#将类存储在模块中，在主程序中导入所需的模块

####导入单个类####

#假定之前创建了表示汽车的类Car，现创建另一个文件my_car.py，其中导入Car类并创建实例

from car import Car                       #打开模块car，并导入其中的Car类，这样就可以直接使用Car类了

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#导入类可以使主程序变得简单易读，专注于主程序的高级逻辑

####在一个模块中存储多个类####

#假设一个模块car.py中有两个类Battery和ElectricCar,导入ElectricCar类，并创建一辆电动汽车

from car import ElectricCar
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

####从一个模块中导入多个类####

from car import Car, ElectricCar
my_beetle = Car('volkwagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

####导入整个模块####

#句点法#

import car

my_beetle = car.Car('volswagen', 'beetle', 2016)             #module_name.class_name   全部导入后访问所需的类
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

####导入模块中的所有类####

form module_name import *                                   #不推荐这种方式

#注：：：最好使用导入整个模块，再根据需要依次访问类

####在一个模块中导入另一个模块####

#一个模块的类可能依赖另一个模块的类

#假设将Car类存储在一个模块中，将ElectricCar和Battery类存储在另一个模块中，将第二个模块命名为electric_car.py，将Bettary和ElectricCar类复制在这个模块中:

from car import Car

class Battery():
    --snip--

class ElectricCar(Car):
    --snip--

#现在可以根据需要创建任何类型的汽车了：

from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElecticCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())





