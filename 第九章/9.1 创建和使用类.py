####定义一个”小狗“的类####

class Dog():                                           #定义了一个空的类
    """一次模拟小狗的简单尝试"""
    def __init__(self, name, age):                      #类中的函数称为方法，init（）是特殊用法，每当根据Dog创建实例时，Python都会自动运行它
        """初始化属性name和age"""                       #左右的下划线是一种约定,且注意是双下划綫！
        self.name = name                               #self可自动调用，以self为前缀的变量都可供类中的所有方法使用
        self.age = age                                 #这种可通过实例访问的变量称为属性

    def sit(self):                                     #这些方法不需要额外的信息如名字和年龄，所以只有一个形参self
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")  #访问属性，句点表示法,python先找到实例my_dog，在查找与此实例相关的属性name，Dog中引用这个属性时，使用的是self.name

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")
####根据类创建实例####
my_dog = Dog('willie', 6)                              #这两个实参调用方法__init__，方法创建一个表示特定小狗的实例，并使用我们提供的值来设置属性name和age，python自动返回一个表示小狗的实例，存储在变量my_dog中
print("My dog's name is " + my_dog.name.title() + ".") #命名约定：首字母大写的名称代表类，小写的名称代表类创建的实例
print("My dog's " + str(my_dog.age) + " years old.")

####调用方法####

my_dog.sit()                                            #句点表示法调用Dog类中定义的任何方法，这里让小狗蹲下和打滚
my_dog.roll_over()

####创建多个实例####

my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog's " + str(my_dog.age) + " years old.")
my_dog.sit()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()


