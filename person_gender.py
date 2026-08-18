class Person:
    def getGender(self):
        print("Person")

class Male(Person):
    def getGender(self):
        print("Male")

class Female(Person):
    def getGender(self):
        print("Female")

male = Male()
female = Female()

male.getGender()
female.getGender()