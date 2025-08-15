import re

def password_strength(password):
    length_error = len(password) < 8
    uppercase_error = not re.search(r"[A-Z]", password)
    lowercase_error = not re.search(r"[a-z]", password)
    digit_error = not re.search(r"\d", password)
    special_error = not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    score = 5 - sum([length_error, uppercase_error, lowercase_error, digit_error, special_error])

    if score == 5:
        return "✅ Strong password"
    elif score >= 3:
        return "⚠️ Moderate password"
    else:
        return "❌ Weak password"

print("\n🔑 Password Strength Checker")
pwd = input("Enter a password to test: ")
print(password_strength(pwd))
