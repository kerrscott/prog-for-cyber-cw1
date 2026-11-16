def validate_ip(ip):
    # Remove any trailing or leading whitespace
    ip = ip.strip()

    # Ensure there is at least one dot present
    if "." not in ip:
        return False

    # Ensure there are exactly three dots total
    if ip.count(".") != 3:
        return False

    # Break the string into individual pieces using the dot as a divider
    numbers = ip.split(".")

    # Ensure the resulting list contains exactly 4 separate pieces
    if len(numbers) != 4:
        return False

    # Attempt to convert and validate each piece as an integer
    try:
        for number in numbers:
            value = int(number)

            # Check if the number falls outside the valid 0-255 range
            if value < 0 or value > 255:
                return False

    # Handle cases where a piece contains non-numeric text characters
    except ValueError:
        return False

    # Return True if all checks pass successfully
    return True


# loop to test user inputs
while True:
    # validation check on the input
    if validate_ip(input("Enter IP Address")):
        print("Valid Ip Address")
        
    else:
        print("Invalid IP Address")
