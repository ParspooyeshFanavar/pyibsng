"""Sample usage."""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import required header
from ibsng import IBSng
from ibsng.exception.general import ChainFormatError
from ibsng.exception.unknown import UnknownError

# Connect and authenticate
con = IBSng("system:sys@http://127.0.0.1:1237")
con.auth()

# Call method
users = con.user.searchUser({"credit": ">1000"}, 20, 10000, 'user_id', True)
charges = con.charge.getChargeInfo("sample1")
apps = con.appnama.getAppsByChargeId(1)

# Print server results
print("user result (inspect):", users.result)
print("user result:", users.inspect())

print("charge result (inspect):", charges.inspect())
print("charge name:", charges.result.charge_name)
print("charge result:", charges.result)

print("apps result:", apps.json["result"])

# exception sample
try:
    con.sample.sample1.sample2()
except ChainFormatError as e:
    print("invalid chain format: {}".format(e.error_msg))

try:
    con.charge.getChargeInfo("INVALID")
except UnknownError as e:
    print("response contains error: {}".format(e))
