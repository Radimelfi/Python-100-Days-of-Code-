MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def enought_resources(enought):
    for item in enought:
        if enought >= resources:
            print(f"Sorry there is not enough water {item}.")
            return False
    return True


def coins():
    """Return the total calculator"""
    print("pleace insert a coin")
    total = int(input("How many Quarter?")) * 0.25
    total += int(input("How many dimes?")) * 0.10
    total += int(input("How many nickeles?")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total


def transation_sucessfull(received, cost):
    """return true when the payment is accetable or false when money is insuficient"""
    if received >= cost:
        change = round(received - cost, 2)
        print(f"Here is {change} in change")
        global profit
        cost += profit
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def coffe(name, ingredient):
    for item in ingredient:
        resources[item] -= ingredient[item]


successfull = True

while successfull:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "off":
        successfull = False
    elif user_choice == "report":
        print("the current resource values. e.g. ")
        print(f"watter: 1000ml{resources['water']}")
        print(f"milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {profit}")

    else:
        drink = MENU[user_choice]
        enought_resources(drink['ingredients'])
        payment = coins()
        transation_sucessfull(payment, drink['cost'])
        coffe(user_choice, drink['ingredients'])
