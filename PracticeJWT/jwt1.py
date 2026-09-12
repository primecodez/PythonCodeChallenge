import json

header ={
    "alg":"HS256",
    "typ":"JWT"
}

payload ={
    "sub":"42",
    "username":"prime"
}

header_json=json.dumps(header)
payload_json=json.dumps(payload)

print(header_json)
print(payload_json)

import base64

encoded_header = base64.urlsafe_b64encode(
    header_json.encode()
).decode().rstrip("=")

encoded_payload = base64.urlsafe_b64encode(
    payload_json.encode()
).decode().rstrip("=")

print(encoded_header)
print(encoded_payload)

secret = "my-super-secret-key"

import hmac
import hashlib

message = encoded_header + "." + encoded_payload

signature = hmac.new(
    secret.encode(),
    message.encode(),
    hashlib.sha256
).digest()

encoded_signature = base64.urlsafe_b64encode(
    signature
).decode().rstrip("=")

print(encoded_signature)

token = (
    encoded_header
    + "."
    + encoded_payload
    + "."
    + encoded_signature
)

print(token)