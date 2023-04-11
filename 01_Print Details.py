#Task: Print out name and favourite colour
name = input("What is your name? ")
favourite_colour = input("What is your favourite colour? ")
print("Hello " + name)
print(name + " likes " + favourite_colour)
#

birth_year = input("In what year were you born? ")
age = (2021 - int(birth_year))
print("You are " + str(age) + " years old")

weight = float(input("What is your weight in Lbs? "))
weight_in_kg = str(weight*0.45)
print("Your weight in kg is " + weight_in_kg + " kg")


first_name = "Baljit"
last_name = "Padda"
msg = (first_name + " [" + last_name + "]" + " is stupid")
print(msg)
msg = f"{first_name} {last_name} is a loser"
print(msg)


#Using .upper()

course = "English Studies"
print(course.upper())
