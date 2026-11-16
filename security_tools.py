import secrets
import string


def passwordValidity(pword):
    length = len(pword)

    digit_count = 0
    space_count = 0
    allowed_symbols = "!@#$%"

    # Loop through each character to count digits and track spaces
    for char in pword:

        if char.isdigit():
            digit_count += 1
        elif " " in pword:
            space_count += 1

    # Check if the password contains at least one of the allowed symbols
    contains_symbol = any(char in allowed_symbols for char in pword)

    # Check all conditions are met and return a 1 (success) or 0 (fail)
    if length > 9 and digit_count > 0 and space_count < 1 and contains_symbol == 1:
        return 1
    else:
        return 0

def validate_ip(ip):
    ip = ip.strip()

    # Ensure dots are present and there are exactly 3 of them
    if "." not in ip:
        return False

    if ip.count(".") != 3:
        return False

    numbers = ip.split(".")

    # Ensure the string splits into 4 bits
    if len(numbers) != 4:
        return False

    # Try converting each segment to an integer and check its value range
    try:
        for number in numbers:
            value = int(number)

            if value < 0 or value > 255:
                return False

    except ValueError:
        return False

    return True

def genPassword():
    # Define a range for the password length
    size = range(10,17)
    # Define character pool (letters, digits, and punctuation)
    alphabet = string.ascii_letters + string.digits + string.punctuation

    # Generate a 10-16 character password
    password = "".join(secrets.choice(alphabet) for _ in range(secrets.choice(size)))

    return password
