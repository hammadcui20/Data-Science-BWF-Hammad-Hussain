from restaurant import Restaurant
from glossary import create_glossary, display_glossary
from dice import Die, roll_dice
from user_module import User
from admin_module import Admin

def main():
    my_restaurant = Restaurant("Tasty Treats", "Italian")
    my_restaurant.describe_restaurant()
    my_restaurant.open_restaurant()
    print(f"Number served: {my_restaurant.number_served}")
    my_restaurant.set_number_served(15)
    print(f"Number served: {my_restaurant.number_served}")
    my_restaurant.increment_number_served(5)
    print(f"Number served: {my_restaurant.number_served}")
    
    glossary = create_glossary()
    print("\nGlossary:")
    display_glossary(glossary)
    
    print("\nRolling dice:")
    six_sided_die = Die(6)
    ten_sided_die = Die(10)
    twenty_sided_die = Die(20)
    print(f"6-sided die: {roll_dice(six_sided_die)}")
    print(f"10-sided die: {roll_dice(ten_sided_die)}")
    print(f"20-sided die: {roll_dice(twenty_sided_die)}")
    
    user = User("Hammad", "Hussain", 23, "hammadasmat@gmail.com", "Rawalpindi")
    user.describe_user()
    user.greet_user()
    admin = Admin("Ali", "Ahmed", 28, "ali.ahmed@gmail.com", "Lahore", ["can add post", "can delete post", "can ban user"])
    admin.describe_user()
    admin.privileges.show_privileges()

if __name__ == "__main__":
    main()
