is_hot = True
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")



hot_day = False
not_hot_day = True

if hot_day:
    print("It's a hot day")
    print("Drink plenty of water")

elif not_hot_day:
    print("It's not a hot day, wrap up warm!")


in_stock = False
not_in_stock = True

if in_stock: print("Go and buy it. It's in stock!")

elif not_in_stock:
    print("Don't go to buy it, it's out of stock!")
    print("Sorry")

hot_day = False
not_hot_day = True

if hot_day:
    print("It's a hot day")
elif not_hot_day:
    print("It's not a hot day")


price = int(1000000)
good_credit = False

if good_credit:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2
print(f"Down payment: £{down_payment}")


has_high_income = True
has_good_credit = False

if has_high_income and has_good_credit:
    print("Eligible for a loan")
else:
    print("Not eligible for a loan")


name = "Ba"

if len(name) < 3:
    print("Name must be at least 3 characters.")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters.")
else:
    print("Name looks good!")


# Very basic car game using if and else.
# Task: "Building a car game, 30.12.21"

print("Welcome!")
active_game = True
while active_game:
    activity = input("What do you want to do? > ").lower()
    if activity == "start":
        print("Game has started")
    elif activity == "help":
        print('''
start - to start the car
stop - to stop the car
quit - to quit the game
''')
    elif activity == "stop":
        print("Game has stopped")
        break
    elif activity == "quit":
        print("You left the game.")
        break
    else:
        print("I didn't understand that.")
