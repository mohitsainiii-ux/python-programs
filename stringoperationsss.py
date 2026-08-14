class StringOperations:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input("Enter a string: ")

    def printString(self):
        print(self.text.upper())

def test():
    obj = StringOperations()
    obj.getString()
    obj.printString()

test()