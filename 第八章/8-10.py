def show_magicians(magician_names):
    """魔术师的名字"""
    for magician_name in magician_names:
        print(magician_name)

def make_great(magician_names):
    """添加Great"""
    great_names = []
    while magician_names:
        magician_name = magician_names.pop()
        great_name = magician_name + ' the great'
        great_names.append(great_name)
    for great_name in great_names:
        magician_names.append(great_name)
magician_names = ['a', 'b', 'c']
show_magicians(magician_names)
print("\n")
make_great(magician_names)
show_magicians(magician_names)