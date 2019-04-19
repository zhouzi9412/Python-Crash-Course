def make_sandwich(*foods):
    """三明治的配料"""
    print("This is your sandwich's foods: ")
    for food in foods:
        print(food)

make_sandwich('a', 'b', 'c')
