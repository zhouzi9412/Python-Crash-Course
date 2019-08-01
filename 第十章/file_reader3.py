filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()        #readline()从文件中读取每一行，并存储在一个列表中    #创建了一个包含文件各行的列表

for line in lines:
    print(line.rstrip()) 