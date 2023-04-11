

prices = [10, 20, 30]

total = 0
for item in prices:
    total += item
print(f"{total}")


for x in range(4):
    for y in range(3):
        for z in range(2):
            print(f"({x}, {y}, {z})")


numbers = [2, 2, 2, 2, 5]
for number in numbers:
    final_value = ""
    for item in range(number):
        final_value += "x"
    print(final_value)


pizzas = ["Pepperoni", "Veggie", "Chicken"]

for pizza in pizzas:
    print(f"I really like {pizza} pizza!\n")
print("Pizza is my favourite food!")


animals = ["Cats", "Dogs", "Hamsters"]

for animal in animals:
    print(f"{animal} have soft fur.")
print("All of these animals have soft fur.")




numbers = [5, 2, 5, 2, 2]
for number in numbers:
    final_value = ""
    for value in range(number):
        final_value += "*"
    print(final_value)


for x in range(2):
    for y in range(2):
        print(x, y)

dates = []
start = 2010_01
for x in range(2):
    for y in range(12):
        dates.append(start+y)
    start = start + 100
print(dates)


start = 2010_01
for x in range(2):

    ## for each month
    for y in range(12):
        date = start + y
        print(date)

    #increment year
    start = start + 100


names = ['Baljit', 'Tom', 'John', 'Dave']
names[3] = 'Davy'
print(names[1:])


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][1])

# List Comprehension example below (includes a for loop and an expression  all in one line of code)
numbers = [print(number) for number in range(1, 101)]

numbers = [print(number) for number in range(1, 21)]#