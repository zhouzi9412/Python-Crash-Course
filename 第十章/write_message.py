filename = 'programming.txt'

with open(filename, 'w') as file_object:   #第一个实参表示打开文件的名称，第二个实参代表以写入模式打开
    file_object.write("I love programming.")   #.write():写入文件

#r,读取模式，默认   w:写入模式   a：附加模式，将内容添加到已有内容末尾     r+：读取写入模式



