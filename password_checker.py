import string

def password_strength_checker():
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation

    password = input("enter the password: ")
    strength = 0

    # length check
    if len(password) >= 8:
        strength += 1
    else:
        print("password too short! must be at least 8 characters.")

    # uppercase check
    if any(char in upper for char in password):
        strength += 1
    else:
        print("add uppercase letters to strengthen your password.")

    # lowercase check
    if any(char in lower for char in password):
        strength += 1
    else:
        print("add lowercase letters to strengthen your password.")

    # digits check
    if any(char in digits for char in password):
        strength += 1
    else:
        print("include digits for better complexity.")

    # special characters check
    if any(char in special for char in password):
        strength += 1
    else:
        print("use special characters to increase security.")

    # final feedback
    if strength == 5:
        print("Strong password")
    elif 3 <= strength < 5:
        print("Moderate password. Can be improved.")
    else:
        print("Weak password. Consider revising it.")

password_strength_checker()
