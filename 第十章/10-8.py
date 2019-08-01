def count_words(filename):
    """读取并打印猫狗文件"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print("Your file is missed.")
    else:
        print(contents)

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    count_words(filename)