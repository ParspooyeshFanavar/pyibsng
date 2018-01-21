import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import required header
from ibsng import IBSng

# Connect and authenticate
conn = IBSng("system:sys@http://172.17.0.2:1237")
conn.auth()

# Call method
s_users = conn.user().searchUser({"user_id": 1}, 20, 10000, 'user_id', True)

# Print the server result
print("OBJ Result:", s_users.result)
print("JSON Result:", s_users.json)
