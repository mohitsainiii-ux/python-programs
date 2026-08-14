class DivisibleBySeven:
    def __init__(self, n):
        self.n = n

    def generator(self):
        for number in range(self.n+1):
            if number % 7 == 0:
                yield number

n = int(input("Enter a number: "))
obj = DivisibleBySeven(n)
for num in obj.generator():
    print(num)