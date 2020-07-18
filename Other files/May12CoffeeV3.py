# resources
resource_money = 550
resource_water = 400
resource_milk = 540
resource_beans = 120
resource_cups = 9


def check_resource(water, milk, beans, cups):
    global resource_water
    global resource_milk
    global resource_beans
    global resource_cups
    if water <= resource_water and milk <= resource_milk and beans <= resource_beans and cups <= resource_cups:
        print("I have enough resources, making you a coffee!")
        return True
    elif water > resource_water:
        print("Sorry, not enough water!")
        # print()
        return False
    elif milk > resource_milk:
        print("Sorry, not enough milk!")
        # print()
        return False
    elif beans > resource_beans:
        print("Sorry, not enough coffee beans!")
        # print()
        return False
    elif cups > resource_cups:
        print("Sorry, not enough disposable cups!")
        # print()
        return False


def update_resource_info(money, water, milk, beans):
    global resource_money
    global resource_water
    global resource_milk
    global resource_beans
    global resource_cups
    resource_money = resource_money + money
    resource_water = resource_water - water
    resource_milk = resource_milk - milk
    resource_beans = resource_beans - beans
    resource_cups = resource_cups - 1


# def types_of_coffee():
# coffee_flavor = input("What do you want to buy? 1"
#                       " - espresso, 2 - latte, 3 - cappuccino:\n")
# if coffee_flavor == 'back':
#     print()
#     main_loop()
#
# elif coffee_flavor == '1':
#     if check_resource(water=250, milk=0, beans=16, cups=1):
#         update_resource_info(money=4, water=250, milk=0, beans=16)
#
# elif coffee_flavor == '2':
#     if check_resource(water=350, milk=75, beans=20, cups=1):
#         update_resource_info(money=7, water=350, milk=75, beans=20)
#
# elif coffee_flavor == '3':
#     if check_resource(water=200, milk=100, beans=12, cups=1):
#         update_resource_info(money=6, water=200, milk=100, beans=12)


def refill(water, milk, beans, cups):
    global resource_water
    global resource_milk
    global resource_beans
    global resource_cups

    resource_water = resource_water + water
    resource_milk = resource_milk + milk
    resource_beans = resource_beans + beans
    resource_cups = resource_cups + cups


def fill():
    water = int(input("Write how many ml of water do you want to add:\n"))
    milk = int(input("Write how many ml of milk do you want to add:\n"))
    beans = int(input("Write how many grams of coffee beans do you want to add\n"))
    cups = int(input("Write how many disposable cups of coffee do you want to add:\n"))

    refill(water, milk, beans, cups)


def take():
    global resource_money
    cash = resource_money
    resource_money = 0
    print(f"I gave you ${cash}")


def remaining_resources():
    print('The coffee machine has:')
    print(f'{resource_water} of water')
    print(f'{resource_milk} of milk')
    print(f'{resource_beans} of coffee beans')
    print(f'{resource_cups} of disposable cups')
    print(f'${resource_money} of money')


while True:
    user_input = input("Write action (buy, fill, take, remaining, exit):\n")
    if user_input.strip() == "buy":
        print()
        coffee_flavor = input("What do you want to buy? 1"
                              " - espresso, 2 - latte, 3 - cappuccino:\n")
        if coffee_flavor == 'back':
            # print()
            continue
        elif coffee_flavor == '1':
            if check_resource(water=250, milk=0, beans=16, cups=1):
                update_resource_info(money=4, water=250, milk=0, beans=16)

        elif coffee_flavor == '2':
            if check_resource(water=350, milk=75, beans=20, cups=1):
                update_resource_info(money=7, water=350, milk=75, beans=20)

        elif coffee_flavor == '3':
            if check_resource(water=200, milk=100, beans=12, cups=1):
                update_resource_info(money=6, water=200, milk=100, beans=12)
        print()
    if user_input.strip() == "fill":
        print()
        fill()
        print()
    if user_input.strip() == "take":
        print()
        take()
        print()
    if user_input.strip() == "remaining":
        print()
        remaining_resources()
        print()
    if user_input.strip() == "exit":
        break
