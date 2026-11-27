
import os
from dotenv import load_dotenv
from urllib.parse import urlsplit, unquote, parse_qs

load_dotenv(".env", override=True)

uri = os.getenv("MONGODB_URI")

if not uri:
    print("ERROR: MONGODB_URI is not loaded!")
    exit()

parsed = urlsplit(uri)

print("\n--- MongoDB Diagnostics ---")
print("URI loaded:", bool(uri))
print("Hostname:", parsed.hostname)
print("Username:", unquote(parsed.username or ""))
print("Password present:", bool(parsed.password))
print("Password length:", len(unquote(parsed.password or "")))
print(
    "Auth source:",
    parse_qs(parsed.query).get("authSource", ["default"])[0]
)
print("---------------------------")
