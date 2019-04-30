class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, number_served):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name.title() + " and " + self.cuisine_type.title() + " and " + str(self.number_served))

    def open_restaurant(self):
        print("Restaurant is on sale.")

    def set_number_served(self, numbers):
        self.number_served = numbers
        print(self.number_served)
    
    def increment_number_served(self, numbers):
        self.number_served += numbers
        print(self.number_served)
restaurant = Restaurant('a', 'b', 25)
restaurant.set_number_served(20)

restaurant.increment_number_served(20)