class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(self.restaurant_name.title() + " and " + self.cuisine_type.title())
    def open_restaurant(self):
        print("Restaurant is on sale.")

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("We have thse icecreams: ")
        for flavor in self.flavors:
            print("-" + flavor.title())

big_one = IceCreamStand('The big one', 'icecream')
big_one.flavors = ['vantile', 'chocolate', 'balck berry']

big_one.describe_restaurant()
big_one.show_flavors()
