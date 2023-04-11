class Person:
    def talk(self):
        print(f"Talk {self.name}")

    def __init__(self, name):
        self.name = name


x = Person("Joe")
x.talk()



class Relationship:
    def __init__(self, girlfriend, boyfriend):
        self.girlfriend = girlfriend
        self.boyfriend = boyfriend

    def talkgirlfriend(self):
        print(f"Talk {self.girlfriend}")

    def talkboyfriend(self):
        print(f"Shut up {self.boyfriend}")

    def talkboth(self):
        print(f"{self.boyfriend} + {self.girlfriend} love each other")

x = Relationship("Baljit", "BOB")
x.talkboth()
x.talkgirlfriend()
x.talkboyfriend()

y = Relationship(girlfriend="Baljit", boyfriend="Joe")
y.talkboth()


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"Sit {self.name}")

    def rollover(self):
        print(f"Roll over {self.name}")

    def walk(self):
        print(f"Walk {self.name}")


class Lamb(Dog):
    pass



x = Dog("Tom", 32)
x.sit()
x.rollover()
x.walk()

y = Lamb("Baljit", 28)
y.rollover()