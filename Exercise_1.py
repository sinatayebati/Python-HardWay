# exercise variables and names 

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven  = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")


# more exercise variables and printing

my_name = 'Sina Tayebati'
my_age = 27 
my_height = 178 #cm
my_weight = 65 #kg
my_eyes = 'black'
my_teeth = 'white'
my_hair = 'black'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} cm tall.")
print(f"He's {my_weight} kg heavy.")
print("Actually that's not too heavy!")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

total = my_age + my_height + my_weight
print(f"if I add {my_age}, {my_height}, and {my_weight} I get {total}.")


