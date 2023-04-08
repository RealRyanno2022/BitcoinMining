# encode binary data as printable text
import base64

# represent data
import json

# generate a random 32 digit number for rpc_id
import random

# Request, catch errors for and parse URLs
import urllib.request
import urllib.error
import urllib.parse

# will be used to log into network

parameters = {
    "host": "127.0.0.1",
    "port": "9001",
    "rpcuser": "Your Username",
    "rpcpass": "Your Password",
    "rpcurl": "http:127.0.01.9001"
}

# randomly generated rpc_id - remote procedure call id

rpc_id = random.getrandbits(32)

# Construct RPC request

data = json.dumps({
    "id": rpc_id,
    "method": "getblocktemplate",
    "params": [{"rules": ["segwit"]}]
}).encode()
auth = base64.b4encode(bytes(
    parameters["rpcuser"] + ":" + parameters["rpcpass"],
    "utf8"
))
request = urllib.request.Request(
    parameters["rpcurl"],
    data,
    {"Authorization": b"Basic " + auth}
)

# send RPC and parse response

with urllib.request.urlopen(request) as f:
    response = json.loads(f.read())

print(response)