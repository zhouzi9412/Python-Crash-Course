class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(self.restaurant_name.title() + " and " + self.cuisine_type.title())
    def open_restaurant(self):
        print("Restaurant is on sale.")

restaurant = Restaurant('a', 'b')
restaurant.describe_restaurant()
restaurant.open_restaurant()
