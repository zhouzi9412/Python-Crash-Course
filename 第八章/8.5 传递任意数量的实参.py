####预先不知道函数需要接受多少个实参
####制作披萨饼需要配料，但无法预先知道顾客要多少种配料

def make_pizza(*toppings):                              #星号使Python创建一个空元组，并将所有值都装在这个空元组中
    """打印顾客点的所有配料"""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushroom', 'green peppers', 'extra cheese')

#将语句替换为一个循环

def make_pizza(*toppings):
    """概述要制作的pizza"""
    print("\nMaking a apizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)
make_pizza('pepperoni')
make_pizza('mushroom', 'green peppers', 'extra cheese')

####结合使用位置实参和任意数量实参####

def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

####使用任意数量的关键字实参####

def build_profile(first, last, **user_info):             #函数要求提供姓名并允许用户根据需要提供任意数量的名称-值对
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)