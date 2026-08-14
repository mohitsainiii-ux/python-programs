class Person:
    name = "Mohit"
    def __init__(self, name = None):
        self.name = name

Person1 = Person()
Person2 = Person("Naman")

print(Person1.name)
print(Person2.name)
print(Person.name)