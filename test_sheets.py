import gspread
from google.oauth2.service_account import Credentials

try:
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
    gc = gspread.authorize(creds)
    sh = gc.open("Yellow Way Payroll")
    worksheet = sh.sheet1
    worksheet.append_row(["Test", "Connection", "Success"])
    print("Connected successfully!")
except Exception as e:
    print(f"ERROR: {e}")