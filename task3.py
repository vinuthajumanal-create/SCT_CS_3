import re

def check_password_strength(password):
    score = 0
    length = len(password) >= 8
    upper = any(c.isupper() for c in password)
    lower = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    if length:
        score += 1
    if upper:
        score += 1
    if lower:
        score += 1
    if digit:
        score += 1
    if special:
        score += 1

    if score == 5:
        strength = "Strong 💪"
    elif score >= 3:
        strength = "Medium ⚖️"
    else:
        strength = "Weak ⚠️"

    print("\nPassword Analysis:")
    print("Length >= 8:", length)
    print("Uppercase present:", upper)
    print("Lowercase present:", lower)
    print("Digit present:", digit)
    print("Special character present:", special)
    print("\nPassword Strength:", strength)

password = input("Enter your password: ")
check_password_strength(password)
