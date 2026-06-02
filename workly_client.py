import os
import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("WORKLY_CLIENT_ID")
CLIENT_SECRET = os.getenv("WORKLY_CLIENT_SECRET")
USERNAME = os.getenv("WORKLY_USERNAME")
PASSWORD = os.getenv("WORKLY_PASSWORD")
BASE_URL = os.getenv("WORKLY_BASE_URL")


def get_access_token():
    """Authenticate with Workly and return access token."""
    url = f"{BASE_URL}/v1/oauth/token"
    payload = {
        "grant_type": "password",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "username": USERNAME,
        "password": PASSWORD
    }
    response = requests.post(url, data=payload)
    response.raise_for_status()
    return response.json().get("access_token")


def get_salaries(token):
    """Get all employees and their salary rates."""
    url = f"{BASE_URL}/v1/payroll/salaries"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


import json

if __name__ == "__main__":
    print("=== TESTING WORKLY CONNECTION ===")
    print(f"Server: {BASE_URL}")
    try:
        print("\nGetting access token...")
        token = get_access_token()
        print(f"✓ Token received: {token[:25]}...")
        
        print("\nFetching salaries...")
        salaries = get_salaries(token)
        
        # Save full response to file for inspection
        with open("workly_salaries_response.json", "w", encoding="utf-8") as f:
            json.dump(salaries, f, indent=2, ensure_ascii=False)
        
        # Print summary
        items = salaries.get("items", [])
        print(f"✓ Got {len(items)} employees")
        print(f"✓ Full response saved to: workly_salaries_response.json")
        
        # Check if anyone has salary data
        with_salary = [e for e in items if e.get("employeeSalaries")]
        without_salary = [e for e in items if not e.get("employeeSalaries")]
        print(f"\n  Employees WITH salary data: {len(with_salary)}")
        print(f"  Employees WITHOUT salary data: {len(without_salary)}")
        
        if with_salary:
            print(f"\nExample employee WITH salary:")
            print(json.dumps(with_salary[0], indent=2, ensure_ascii=False))
        
    except requests.exceptions.HTTPError as e:
        print(f"\n✗ HTTP ERROR: {e}")
        print(f"Response: {e.response.text}")
    except Exception as e:
        print(f"\n✗ ERROR: {type(e).__name__}: {e}")