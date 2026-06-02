import json
with open("credentials.json") as f:
    data = json.load(f)
print("=" * 60)
print("EMAIL TO SHARE:")
print(data["client_email"])
print("=" * 60)
print("PROJECT:", data["project_id"])