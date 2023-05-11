import subprocess

import secrets
key = secrets.token_bytes(32).hex()
print(len(key))
