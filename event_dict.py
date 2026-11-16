# Dictionary containing security event details
security_event = {
    "username": "jdoe_admin",
    "ip_address": "192.168.1.105",
    "event_type": "Failed Login Attempt",
    "risk_level": "Medium"
}

# Display specific key values
print("Username and Ip Address")
print(security_event["username"], security_event["ip_address"],"\n")

# Add a new key and update an existing key in the dictionary
security_event.update({
    "status": "1",
    "risk_level": "High"
})

# Remove a key from the dictionary
del security_event["event_type"]

# Loop through and print all key-value pairs
print("Remaining KV Pairs")
for key, value in security_event.items():
    print(f"{key}: {value}")


# Display the total count of key-value pairs remaining
print()
print(len(security_event),"Key Value Pairs")
