# prog-for-cyber-cw1

This repository contains a collection of Python scripts developed for my university coursework. Each task focuses on fundamental programming concepts—such as loops, dictionaries, modular code, and input validation—applied to basic cybersecurity scenarios.

Student ID
B01862966

Task 1 Description
This Python script is a simple password security program locked behind a master password. Once you're in, a menu lets you test three authentication exercises: tracking failed guesses out of 10, simulating a 30-try brute-force attack, and locking an account after 3 failed login attempts.

Task 2 Description
This Python script is a simple login logger that keeps prompting for a username and password until you get them right. Every attempt is saved to a log list with a unique event ID, timestamp, local IP address, and whether the login passed or failed, printing the updated log history after each try.

Task 3 Description
This Python script is a simple IPv4 address validator that continuously asks for an IP address and checks if it's properly formatted. It verifies that the input has four number sections separated by three dots, and ensures each section is a valid integer between 0 and 255 before printing whether it's valid or invalid.

Task 4 Description
This Python script demonstrates basic dictionary manipulation using a mock security event log. It starts by printing specific details like the username and IP address, then updates the risk level, adds a new status field, and deletes the event type before looping through and counting the remaining key-value pairs.

Task 5 Description
This Python project splits security utilities into a custom module (security_tools.py) and imports them into a main script (main.py). The main program prompts for a password and an IP address, checking if the password meets length, digit, symbol, and spacing rules—automatically generating a random strong password if it's too weak—and verifying that the IP address follows a valid IPv4 format.

