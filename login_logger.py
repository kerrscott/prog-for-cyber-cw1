# Import libraries for networking, unique IDs, and timestamps
import socket
import uuid
from datetime import datetime

# Define valid login credentials and the log list
creds = ["root", "root"]
log = []
fail = 1 # Flag to control the authentication loop

# Loop until a successful login happens
while fail == 1:
    # Generate a unique tracking ID and get current time
    event_id = str(uuid.uuid4())
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Open a  network connection to find the  IP address
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()

    # Get input from the user
    username = input("Enter Username")
    password = input("Enter Password")

    # Check credentials to update the loop flag
    if username == creds[0] and password == creds[1]:
        fail = 0 # Break loop on success
    else:
        fail = 1 # Keep looping on failure

    # Add the login attempt details to the historical log
    log.append({
        "eventID":event_id,
        "username":username,
        "ipAddress":ip_address,
        "event":'Failed Login' if fail else 'Succsessful Login',
        "timestamp":timestamp
    })
    
    # Print the entire log history with each entry on a new line
    print(*log, sep="\n")
