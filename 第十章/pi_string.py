filename = 'C\Users\zhouz\Desktop\Python-Crash-Course\第十章\pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''                           #创建一个空变量，存储pi值
for line in lines:
    pi_string += line.rstrip()           #将line各行都加入空变量

print(pi_string)
print(len(pi_string))                   #len()长度
