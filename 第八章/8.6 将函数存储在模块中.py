####将函数存放在称为模块的独立文件中，再将模块导入到主程序中

####导入整个模块####

def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)

#在此文件所在目录下创建另一个py文件，这个文件导入刚创建的模块，再调用：

import 8.6

#用以下语法使用模块下的任意一个函数：
8.6.function_name()

####导入特定的函数

#导入模块中特定的函数：

from 8.6 import function_name0, function_name1, function_name2.....

####使用as给函数指定别名

#导入的函数名称与别的而程序现有名称冲突，或者太长，可指定别名（外号），例如make_pizza()指定了别名mp():

form pizza import make_pizza as mp
mp(16, 'pepperoni')

####使用as给模块指定别名####

import module_name as mnmnmn

####导入模块中的所有函数####

#使用*号可以导入模块中所有函数

form module_name import *

#注意：不建议用这种导入方法，以防逻辑混乱

