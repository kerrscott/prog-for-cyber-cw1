# prog-for-cyber-cw1

Student ID
B01862966
Kerr Scott
Lanarkshire

This Python project splits security utilities into a custom module (security_tools.py) and imports them into a main script (main.py). The main program prompts for a password and an IP address, checking if the password meets length, digit, symbol, and spacing rules—automatically generating a random strong password if it's too weak—and verifying that the IP address follows a valid IPv4 format.

How to Run: Modular Security Utilities

1. Ensure both `security_tools.py` and `main.py` are saved in the same folder, then run `main.py` from your terminal:
   ```bash
   python3 main.py
   ```
2. Enter a Password: Type a password to test its strength. To pass, it must be at least 10 characters long, contain at least one digit and one symbol (`!@#$%`), and have no spaces. If it fails, the script will generate and suggest a strong random password.
3. Enter an IP Address: Type an IPv4 address (such as `10.0.0.1`) to verify whether it is valid or invalid.****
