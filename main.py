import security_tools

# Take user inputs
password = input("Enter Password")
ip_addr = input("Enter IP Address")

# Check if given password passes validity function
if security_tools.passwordValidity(password):
    print("Password Ok")
else: # Reject Password and use password generator to prompt strong password
    print("Weak Password, Use This Instead",security_tools.genPassword())

# Check if given IP Address passes validity function
if security_tools.validate_ip(ip_addr):
    print("IP Address Ok")
else:
    print("IP Address NOT OK")
