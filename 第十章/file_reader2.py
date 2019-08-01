filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:          #for实现逐行读取
        print(line.rstrip())          #rstrip()可将每一行末尾的空字符段消去