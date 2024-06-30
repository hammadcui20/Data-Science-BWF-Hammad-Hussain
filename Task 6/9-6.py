class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, increment):
        self.number_served += increment

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors=[]):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print("Ice Cream Flavors Available:")
        for flavor in self.flavors:
            print(f"- {flavor}")

ice_cream_stand = IceCreamStand("Sweet Treats", "Ice Cream", ["Vanilla", "Chocolate", "Strawberry"])
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_flavors()
