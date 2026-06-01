print("=== START ===")
import gspread
from google.oauth2.service_account import Credentials
import traceback

scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
gc = gspread.authorize(creds)
print("Auth OK")

# PASTE YOUR SHEET URL HERE
SHEET_URL = "https://docs.google.com/spreadsheets/d/1XS4RIrmU20RRESIDim13D1UYmUSNX-dbjT-C0M3L_Dc/edit?gid=0#gid=0"

try:
    sh = gc.open_by_url(SHEET_URL)
    print(f"Opened: {sh.title}")
    ws = sh.sheet1
    print(f"Worksheet: {ws.title}")
    ws.append_row(["Test", "Connection", "Success"])
    print("WROTE ROW ✓")
except Exception as e:
    print(f"\nFULL ERROR:\n{traceback.format_exc()}")