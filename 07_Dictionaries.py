"""
Tuesday 11th January 2022
Example of a Dictionary 11.01.22
"""

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer["age"])

phone = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}

digits = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six"
}
phone = input("What is your phone number? ")
for ch in phone:
    print(digits[ch])

thesaurus = {
    "nice": "delightful",
    "sad": "despondent",
    "fast": "briskly",
    "happy": "overjoyed"
}
paragraph = input("Write a few sentences about your walk in the park: ")
for word in thesaurus:
    paragraph = paragraph.replace(word, thesaurus[word])
print(paragraph)


for word in paragraph:
    translated = thesaurus.get(word)
    if translated is None:
        print(word)
    else:
        print(translated)