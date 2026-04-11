from supabase_client import get_supabase
from datetime import datetime
import csv
import os

# Get all contacts
supabase = get_supabase()
contacts = supabase.table("contacts").select("*").execute().data

total_contacts = len(contacts)

# Current date and time
now = datetime.now()
date = now.strftime("%Y-%m-%d")
time = now.strftime("%H:%M:%S")

file_name = "daily_contacts_log.csv"

# Check if file exists
file_exists = os.path.isfile(file_name)

with open(file_name, "a", newline="") as file:
    writer = csv.writer(file)

    # write header if file does not exist
    if not file_exists:
        writer.writerow(["Date", "Time", "Total Contacts"])

    writer.writerow([date, time, total_contacts])

print("Daily log updated successfully")