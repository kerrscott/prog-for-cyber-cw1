#master password
password = "1234"

# Loop forever
while True:
    # Get user input for the password
    attempt = input("Enter password: ")

    # Check if the guess is correct
    if attempt == password:
        print("Access granted!")
        break  # Exit the loop
    else:
        print("Wrong password! Try again.")


def eventCounter():
    password = "6"
    correct_count = 0
    incorrect_count = 0

    # Loop exactly 10 times
    for x in range(10):
        attempt = input("Enter Password")

        # Increment the correct or incorrect counter
        if attempt == password:
            correct_count +=1
        else: 
            incorrect_count +=1

    # Display the final counts
    print(correct_count,incorrect_count)
    # Check if more than half of the attempts failed
    if incorrect_count > 5:
        print("Incorrect Attempts exceeds 50% of all attempts")

# Define function to simulate a brute force
def bruteForce():
    password = "root"
    max_attempts = 30
    count = 0
    # Loop up to the maximum number of attempts allowed
    for x in range(max_attempts):
        attempt = input("Try and guess the password")
        count +=1
        # Stop looping if the password is found
        if attempt == password:
            break

    # Display total guesses made
    print("Number of attempts",count)

# Define function for user login authentication with an attempt limit
def loginAuth():
    creds = ["root","root"]

    failed_attempts = 0
    
    # Give the user up to 3 chances to log in
    for x in range(3):
        username = input("Enter Username")
        password = input("Enter Password")

        # Verify if both username and password match credentials
        if username == creds[0] and password == creds[1]:
            print("Login Succseful")
            break  # Exit loop on successful login
        else:
            print("Login Unsuccsesful, Try Again")
            failed_attempts +=1

    # Lock the account if all 3 attempts failed
    if failed_attempts == 3:
        print("Account locked for 24 hours")

        
# Continuous loop to display and manage the main menu selection
while True:
    print("\n=== MAIN MENU ===")
    print("1. Program 1")
    print("2. Program 2")
    print("3. Program 3")
    print("4. Exit")

    # Get the user's choice from the menu
    choice = input("Choose an option: ")

    # Route the user to the correct program based on choice
    if choice == "1":
        print("Running Program 1...")
        eventCounter()
    elif choice == "2":
        print("Running Program 2...")
        bruteForce()
    elif choice == "3":
        print("Running Program 3...")
        loginAuth()
    elif choice == "4":
        print("Goodbye!")
        break  # Exit the menu loop and end script

    # Handle invalid menu selections
    else:
        print("Invalid option. Try again.")
