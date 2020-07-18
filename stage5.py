# supply variables
stored_money = 550
stored_water = 400
stored_milk = 540
stored_beans = 120
stored_cups = 9


def prompt():
    print("The coffee machine has:")
    print(f"{stored_water} of water")
    print(f"{stored_milk} of milk")
    print(f"{stored_beans} of coffee beans")
    print(f"{stored_cups} of disposable cups")
    print(f"{stored_money} of money")
    print()


def update_storage_info(money, water, milk, beans):
    global stored_money
    global stored_water
    global stored_milk
    global stored_beans
    global stored_cups
    stored_money = stored_money + money
    stored_water = stored_water - water
    stored_milk = stored_milk - milk
    stored_beans = stored_beans - beans
    stored_cups = stored_cups - 1


def refill(water, milk, beans, cups):
    global stored_water
    global stored_milk
    global stored_beans
    global stored_cups

    stored_water = stored_water + water
    stored_milk = stored_milk + milk
    stored_beans = stored_beans + beans
    stored_cups = stored_cups + cups


def fill():
    water = int(input("Write how many ml of water do you want to add:\n"))
    milk = int(input("Write how many ml of milk do you want to add:\n"))
    beans = int(input("Write how many grams of coffee beans do you want to add\n"))
    cups = int(input("Write how many disposable cups of coffee do you want to add:\n"))

    refill(water, milk, beans, cups)


def types_of_coffee():
    coffee_flavor = int(
        input("What do you want to buy? 1" " - espresso, 2 - latte, 3 - cappuccino:\n")
    )

    if coffee_flavor == 1:
        update_storage_info(money=4, water=250, milk=0, beans=16)

    elif coffee_flavor == 2:
        update_storage_info(money=7, water=350, milk=75, beans=20)

    elif coffee_flavor == 3:
        update_storage_info(money=6, water=200, milk=100, beans=12)


def take():
    global stored_money
    cash = stored_money
    stored_money = 0
    print(f"I gave you ${cash}")


# first prompt
prompt()
# second prompt
answer = input("Write action (buy, fill, take):\n")

if answer == "buy":
    types_of_coffee()
    print()
    prompt()

elif answer == "fill":
    fill()
    print()
    prompt()

elif answer == "take":
    take()
    print()
    prompt()
