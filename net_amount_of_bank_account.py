transactions = input("Enter transactions: ").split()

balance = 0

for i in range(0, len(transactions), 2):
    transaction = transactions[i]
    amount = int(transactions[i + 1])

    if transaction == "D":
        balance += amount
    elif transaction == "W":
        balance -= amount

print(balance)