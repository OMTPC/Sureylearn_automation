

from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

email = os.getenv("EMAIL_ADDRESS")
password = os.getenv("EMAIL_PASSWORD")

print(f"Email: {email}")
print(f"Password: {password}")  

