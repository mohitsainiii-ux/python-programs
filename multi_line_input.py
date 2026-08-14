lines = []

while True:
    line = input()

    if line.lower() == "end":
        break

    lines.append(line.upper())

for line in lines:
    print(line)