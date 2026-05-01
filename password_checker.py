import re

common_passwords = ["123456", "password", "qwerty"]

def check_strength(password):
    score = 0
    if len(password) >= 8: score += 1
    if re.search(r"[A-Z]", password): score += 1
    if re.search(r"[a-z]", password): score += 1
    if re.search(r"[0-9]", password): score += 1
    if re.search(r"[!@#$%^&*()]", password): score += 1

    if password.lower() in common_passwords:
        return "Weak"

    if score <= 2: return "Weak"
    elif score <= 4: return "Medium"
    else: return "Strong"

pwd = input("Enter password: ")
print("Strength:", check_strength(pwd))
