class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(self.restaurant_name.title() + " and " + self.cuisine_type.title())
    def open_restaurant(self):
        print("Restaurant is on sale.")

restaurant_1 = Restaurant('a', 'b')
restaurant_2 = Restaurant('c', 'd')
restaurant_3 = Restaurant('e', 'f')
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()