# prog-for-cyber-cw1


Student ID
B01862966
Kerr Scott
Lanarkshire

This Python script is a simple password security program locked behind a master password. Once you're in, a menu lets you test three authentication exercises: tracking failed guesses out of 10, simulating a 30-try brute-force attack, and locking an account after 3 failed login attempts.

How to run: Authentication Simulator

1. Navigate to the project folder in your terminal and run the script:
   ```bash
   python3 auth_menu.py
   ```
2. Unlock the Master Password: When prompted with `Enter password:`, type `1234` and press Enter to access the main menu.
3. Select a Program: Enter a number from `1` to `4` to test each scenario:
   * Option 1 (`Event Counter`): Enter 10 password guesses (the target password is `6`).
   * Option 2 (`Brute Force`): Try guessing the password within 30 attempts (the target password is `root`).
   * Option 3 (`Login Auth`): Enter a username and password (`root` / `root`), or fail 3 times to trigger the account lockout.
   * Option 4 (`Exit`): Close the program.
