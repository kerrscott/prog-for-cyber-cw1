# prog-for-cyber-cw1


Student ID
B01862966
Kerr Scott
Lanarkshire

This Python script is a simple login logger that keeps prompting for a username and password until you get them right. Every attempt is saved to a log list with a unique event ID, timestamp, local IP address, and whether the login passed or failed, printing the updated log history after each try.

How to run: Login Attempt Logger

1. Navigate to the project folder in your terminal and run the script:
   ```bash
   python3 task2_login_logger.py
   ```
2. Test Login Attempts: Enter any incorrect username and password to generate a `Failed Login` entry in the console log, along with a UUID, timestamp, and local IP address.
3. Complete Login: Enter `root` for both the username and password to record a `Succsessful Login` and exit the loop.

