with open('pi_digits.txt') as file_object:           #在py文件所在目录查找文件并打开   #with表示不在需要访问文件后将其关闭，否则还要调用close()
    contents = file_object.read()
    print(contents)