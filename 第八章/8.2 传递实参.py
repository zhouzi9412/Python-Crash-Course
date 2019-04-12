####函数可能调用多个实参

####位置实参，实参顺序与形参相同####

def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster','harry')
describe_pet('dog','willie')                                               #多次调用实参是一种效率极高的工作方式

####关键字实参，每个实参都由变量名和值组成####

####关键字实参无需考虑调用的实参顺序，清楚指出了调用中各个值的作用####

def describe_pet(animal_type,pet_name):
    """显示宠物信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type='hamster', pet_name='harry')

####默认值####

#给形参指定默认值

def describe_pet(pet_name, animal_type='dog'):                         #注意！此时若后面任然为位置实参，则此处会将这个实参关联到第一个形参 
    """显示宠物信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    describe_pet(pet_name='willie')                                    #没有指定animal_type值时，则其使用默认值dog

####等效的函数调用####

####避免实参错误####

