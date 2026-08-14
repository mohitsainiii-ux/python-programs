import re
passwords = input("Enter passwords: ").split(",")
valid_passwords = []
for password in passwords:
    if (len(password) >= 6 and len(password) <= 12 and
            re.search(r"[a-z]", password) and
            re.search(r"[A-Z]", password) and
            re.search(r"[0-9]", password) and
            re.search(r"[@#$]", password)):
        valid_passwords.append(password)
print(",".join(valid_passwords))