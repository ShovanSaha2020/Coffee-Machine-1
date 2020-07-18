# Write your code here
water_in_storage = int(
    input("Write how many ml of water the coffee machine has:\n"))
milk_in_storage = int(
    input("Write how many ml of milk the coffee machine has:\n"))
coffee_beans_in_storage = int(
    input("Write how many grams of coffee beans the coffee machine has:\n")
)
number_of_coffee = int(input("Write how many cups of coffee you will need:\n"))

water_per_cup_coffee = 200
milk_per_cup_coffee = 50
coffee_beans_per_cup_coffee = 15

total_water = number_of_coffee * water_per_cup_coffee
total_milk = number_of_coffee * milk_per_cup_coffee
total_coffee_beans = number_of_coffee * coffee_beans_per_cup_coffee

water_remaining = water_in_storage - total_water
milk_remaining = milk_in_storage - total_milk
coffee_beans_remaining = coffee_beans_in_storage - total_coffee_beans

extra_coffee_1 = water_remaining // water_per_cup_coffee
extra_coffee_2 = milk_remaining // milk_per_cup_coffee
extra_coffee_3 = coffee_beans_remaining // coffee_beans_per_cup_coffee

possible_extra_coffee = min(extra_coffee_1, extra_coffee_2, extra_coffee_3)

# print("For 25 cups of coffee you will need:")
# print(f"{total_water} ml of water")
# print(f"{total_milk} ml of milk")
# print(f"{total_coffee_beans} g of coffee beans")


if (
    total_water <= water_in_storage
    and total_milk <= milk_in_storage
    and total_coffee_beans <= coffee_beans_in_storage
):
    if possible_extra_coffee >= 1:
        print(
            f"Yes, I can make that amount of coffee (and even {possible_extra_coffee} more than that)"
        )
    else:
        print("Yes, I can make that amount of coffee")
else:
    cups1 = water_in_storage // water_per_cup_coffee
    cups2 = milk_in_storage // milk_per_cup_coffee
    cups3 = coffee_beans_in_storage // coffee_beans_per_cup_coffee
    max_cups = min(cups1, cups2, cups3)
    print(f"No, I can make only {max_cups} cup(s) of coffee")
