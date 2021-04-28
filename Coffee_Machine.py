water = 400
milk = 540
coffee_beans = 120
cups = 9
money = 550

def buy():
    global water
    global milk
    global coffee_beans
    global cups
    global money
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    usr_input = input()
    if usr_input == "1":
        if water < 250:
            print("Sorry, not enough water!")
        elif coffee_beans < 16:
            print("Sorry, not enough coffee beans!")
        elif cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            water -= 250
            coffee_beans -= 16
            cups -= 1
            money += 4
    elif usr_input == "2":
        if water < 350:
            print("Sorry, not enough water!")
        elif milk < 75:
            print("Sorry, not enough milk!")
        elif coffee_beans < 20:
            print("Sorry, not enough coffee beans!")
        elif cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            water -= 350
            milk -= 75
            coffee_beans -= 20
            cups -= 1
            money += 7
    elif usr_input == "3":
        if water < 200:
            print("Sorry, not enough water!")
        elif milk < 100:
            print("Sorry, not enough milk!")
        elif coffee_beans < 12:
            print("Sorry, not enough coffee beans!")
        elif cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a coffee!")
            water -= 200
            milk -= 100
            coffee_beans -= 12
            cups -= 1
            money += 6
    elif usr_input == "back":
        pass
    print()    
    
def fill():
    global water
    global milk
    global coffee_beans
    global cups
    print("Write how many ml of water do you want to add:")
    add_water = int(input())
    water += add_water
    print("Write how many ml of milk do you want to add:")
    add_milk = int(input())
    milk += add_milk
    print("Write how many grams of coffee beans do you want to add:")
    add_coffee = int(input())
    coffee_beans += add_coffee
    print("Write how many disposable cups of coffee do you want to add:")
    add_cups = int(input())
    cups += add_cups
    print()

def take():
    global money
    print("I gave you $" + str(money))
    money = 0
    print()    

def remaining():
    global water
    global milk
    global coffee_beans
    global cups
    global money
    print("The coffee machine has:")
    print(water, "of water")
    print(milk, "of milk")
    print(coffee_beans, "of coffee beans")
    print(cups, "of disposable cups")
    print("$" + str(money), "of money")
    print()

while True:
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    print()
    if action == "buy":
        buy()
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "remaining":
        remaining()
    elif action == "exit":
        break