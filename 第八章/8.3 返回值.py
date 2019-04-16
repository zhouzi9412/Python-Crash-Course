####返回简单值####

def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()                              #将结果返回到函数调用行
musician = get_formatted_name('jimi','hendrix')
print(musician)

#### 让实参变成可选的####

def get_formatted_name(first_name, middle_name, last_name):                    
    """返回整洁的姓名"""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('john','lee','hooker')
print(musician)

#不一定所有人都由中间名，所以需要使实参可选

def get_formatted_name(first_name, last_name, middle_name=''):          #middle_name设置为空字符串，使实参可选
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi','hendrix')
print(musician)
musician = get_formatted_name('john','hooker','lee')
print(musician)

####返回字典####

def build_person(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)

####结合使用函数和while循环####

def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
#这是个无限循环！
while True:
    print("\nPlease tell me your name: ")
    f_name = input("Full name: ")
    l_name = input("Last name: ")
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

#用break语句退出循环

def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
#这是个无限循环！
while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")
    f_name = input("Full name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")