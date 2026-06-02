import os
import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("WORKLY_CLIENT_ID")
CLIENT_SECRET = os.getenv("WORKLY_CLIENT_SECRET")
USERNAME = os.getenv("WORKLY_USERNAME")
PASSWORD = os.getenv("WORKLY_PASSWORD")
BASE_URL = os.getenv("WORKLY_BASE_URL")

print("=== ENV CHECK ===")
print(f"CLIENT_ID: '{CLIENT_ID}' (len={len(CLIENT_ID) if CLIENT_ID else 0})")
print(f"CLIENT_SECRET: '{CLIENT_SECRET[:10]}...' (len={len(CLIENT_SECRET) if CLIENT_SECRET else 0})")
print(f"USERNAME: '{USERNAME}' (len={len(USERNAME) if USERNAME else 0})")
print(f"PASSWORD: '{PASSWORD[:3]}***{PASSWORD[-2:]}' (len={len(PASSWORD) if PASSWORD else 0})")
print(f"BASE_URL: '{BASE_URL}'")

print("\n=== ATTEMPT 1: dict payload (current method) ===")
url = f"{BASE_URL}/v1/oauth/token"
payload = {
    "grant_type": "password",
    "client_id": CLIENT_ID,
    "client_secret": CLIENT_SECRET,
    "username": USERNAME,
    "password": PASSWORD
}
r = requests.post(url, data=payload)
print(f"Status: {r.status_code}")
print(f"Response: {r.text}")

print("\n=== ATTEMPT 2: raw string body (mimicking curl exactly) ===")
from urllib.parse import quote
body = (
    f"client_id={CLIENT_ID}"
    f"&client_secret={CLIENT_SECRET}"
    f"&grant_type=password"
    f"&username={quote(USERNAME)}"
    f"&password={quote(PASSWORD)}"
)
print(f"Body being sent: {body[:80]}...***")
headers = {"Content-Type": "application/x-www-form-urlencoded"}
r = requests.post(url, data=body, headers=headers)
print(f"Status: {r.status_code}")
print(f"Response: {r.text}")

print("\n=== ATTEMPT 3: as query parameters ===")
r = requests.post(url, params=payload)
print(f"Status: {r.status_code}")
print(f"Response: {r.text}")