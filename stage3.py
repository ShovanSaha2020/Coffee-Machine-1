# Write your code here
number_of_coffee = int(input())
water_per_cup_coffee = 200
milk_per_cup_coffee = 50
coffee_beans_per_cup_coffee = 15

total_water = number_of_coffee * water_per_cup_coffee
total_milk = number_of_coffee * milk_per_cup_coffee
total_coffee_beans = number_of_coffee * coffee_beans_per_cup_coffee

print("For 25 cups of coffee you will need:")
print(f"{total_water} ml of water")
print(f"{total_milk} ml of milk")
print(f"{total_coffee_beans} g of coffee beans")
