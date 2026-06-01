print("=== SCRIPT STARTED ===")

import sys
print(f"Python: {sys.executable}")
print(f"Working dir check...")

import os
print(f"Current folder: {os.getcwd()}")
print(f"Files here: {os.listdir('.')}")

print("\n=== CHECKING CREDENTIALS ===")
if not os.path.exists("credentials.json"):
    print("ERROR: credentials.json NOT FOUND in this folder")
    sys.exit(1)
else:
    print("credentials.json found ✓")

print("\n=== IMPORTING LIBRARIES ===")
try:
    import gspread
    from google.oauth2.service_account import Credentials
    print("Libraries imported ✓")
except Exception as e:
    print(f"IMPORT ERROR: {e}")
    sys.exit(1)

print("\n=== AUTHENTICATING ===")
try:
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
    gc = gspread.authorize(creds)
    print("Authentication ✓")
except Exception as e:
    print(f"AUTH ERROR: {e}")
    sys.exit(1)

print("\n=== LISTING SHEETS THE SERVICE ACCOUNT CAN SEE ===")
try:
    all_sheets = gc.openall()
    if not all_sheets:
        print("⚠️ Service account sees ZERO sheets — sharing didn't work")
    else:
        for s in all_sheets:
            print(f"  - {s.title}")
except Exception as e:
    print(f"LIST ERROR: {e}")

print("\n=== OPENING 'Yellow Way Payroll' ===")
try:
    sh = gc.open("Yellow Way Payroll")
    worksheet = sh.sheet1
    print(f"Opened sheet ✓ — Title: {sh.title}")
except Exception as e:
    print(f"OPEN ERROR: {e}")
    sys.exit(1)

print("\n=== WRITING TEST ROW ===")
try:
    worksheet.append_row(["Test", "Connection", "Success"])
    print("Row written ✓")
except Exception as e:
    print(f"WRITE ERROR: {e}")
    sys.exit(1)

print("\n=== ALL DONE — CHECK YOUR SHEET ===")