#Password strenght checker
passwords = ["hello", "Hello123", "H3ll0@World", "12345678", "MyP@ss!"]
for password in passwords:
    print("Password:", password)
    weak = False
    # Rule 1: Length
    if len(password) < 8:
        print("  - Too short, need 8 characters")
        weak = True
    # Rule 2: Uppercase
    has_upper = False
    for c in password:
        if c.isupper():
            has_upper = True
    if has_upper == False:
        print("  - Missing uppercase letter")
        weak = True
     # Rule 3: Lowercase
    has_lower = False
    for c in password:
        if c.islower():
            has_lower = True
    if has_lower == False:
        print("  - Missing lowercase letter")
        weak = True
    # Rule 4: Digit
    has_digit = False
    for c in password:
        if c.isdigit():
            has_digit = True
    if has_digit == False:
        print("  - Missing a number")
        weak = True
    # Rule 5: Special character
    special = "!@#$%^&*"
    has_special = False
    for c in password:
        if c in special:
            has_special = True
    if has_special == False:
        print("  - Missing special character")
        weak = True
    # Final result
    if weak == False:
        print("  Strong Password!")
    else:
        print("  Weak Password!")
