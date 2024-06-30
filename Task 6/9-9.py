class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        print(f"This car can go approximately {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
            print("Battery upgraded to 85 kWh.")
        else:
            print("Battery is already at 85 kWh.")

class ElectricCar:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery()

    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")

my_tesla = ElectricCar("Tesla", "Model S", 2020)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
