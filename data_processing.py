import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]
creds = ServiceAccountCredentials.from_json_keyfile_name(
    "client_id.json", scope
)
client = gspread.authorize(creds)

player_all = pd.DataFrame(
    client.open("data_final_10000")
    .get_worksheet(0)
    .get_all_records()
)