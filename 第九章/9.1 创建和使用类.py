####定义一个”小狗“的类####

class Dog():                                           #定义了一个空的类
    """一次模拟小狗的简单尝试"""
    def __init__(self, name, age):                      #类中的函数称为方法，init（）是特殊用法，每当根据Dog创建实例时，Python都会自动运行它
        """初始化属性name和age"""                       #左右的下划线是一种约定,且注意是双下划綫！
        self.name = name                               #self可自动调用，以self为前缀的变量都可供类中的所有方法使用
        self.age = age                                 #这种可通过实例访问的变量称为属性

    def sit(self):                                     #这些方法不需要额外的信息如名字和年龄，所以只有一个形参self
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog's " + str(my_dog.age) + " years old.")

####根据类创建实例####