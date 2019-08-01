#try-except代码块管理异常

print(5/0)
#程序报错，使用try-except代码块预处理可能发生的错误

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
#这种方法就将纯代码的traceback变为对用户友好的错误消息

#使用异常避免崩溃

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit." )

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)
#这个程序很容易就会崩溃,使用else代码块

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:                                                 #try-except-else代码块，成功执行的代码在else中，错误的代码放入except代码块中
        print(answer)

#处理FileNotFoundError异常---找不到文件

filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)

#分析文本
#split():以空格为分隔符将字符串分拆成多个部分，并存储到一个列表中

filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    #计算文件大致包含多少个单词
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")

#使用多个文件  
def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        #计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")

filename = 'alice.txt'
count_words(filename)

#调用
filenames = ['a', 'b', 'c', 'd']
for filename in filenames:
    count_words(filename)

#失败时一声不吭

#except代码块中明确告诉Python什么都不要做，用pass语句

def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        --snip--
    except FileNotFoundError:
        pass
    else:
        --snip--

filename = ['a', 'b', 'c', 'd']
for filename