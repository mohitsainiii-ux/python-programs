import re

emailAddress = input()
pattern = r"(\w+)@((\w+\.)+(com))"
result = re.match(pattern, emailAddress)

print(result.group(1))