
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv(override=True)

uri = os.getenv("MONGODB_URI")

try:
    client = MongoClient(
        uri,
        serverSelectionTimeoutMS=10000
    )

    result = client.admin.command("ping")

    print("SUCCESS! MongoDB Atlas connected.")
    print(result)

except Exception as e:
    print("CONNECTION FAILED:")
    print(type(e).__name__, e)

finally:
    if "client" in locals():
        client.close()
