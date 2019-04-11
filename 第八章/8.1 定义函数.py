####定义函数####

def greet_user():                                #必须要有括号#
    """显示简单的问候语"""                         #文档字符串，描述了函数做什么#
    print("Hello")                               
greet_user()

####向函数传递信息####

def greet_user(username):                      #username可让函数接受你给username指定任何值
    """显示简单的问候语"""
    print("Hello, " + username.title() + "!")
greet_user('jesse')

####实参和形参####

#username即为一个形参，为函数完成其工作所需的一项信息
# 'jesse'即为实参，为调用函数时传递给函数的信息

