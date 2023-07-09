# Employee Management System designed by Hunter Laberge

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('python-library-key.json', scope)

# Create a client to interact with Google Sheets
client = gspread.authorize(creds)

# Open the desired Google Sheet
spreadsheet_id = 'https://docs.google.com/spreadsheets/d/1UVIAJKWEkbPNAVJOaXCSRDSQ66T_Qgz0GHjP1U492ig/edit#gid=0'
sheet_name = 'Sheet1'
sheet = client.open_by_key(spreadsheet_id).worksheet(sheet_name)


while True:
    print("*****Query for Employee Records*****")
    print("1.) Add Employee")
    print("2.) Find Employee")
    print("3.) Edit Employee")
    print("4.) Exit Application")

    choice = input("Select an option: ")

    if choice == "1":
        print("*****ADD EMPLOYEE*****")


    elif choice == "2":
        print("You Selected 'Find Employee' ")
    elif choice == "3":
        print("You Selected 'Edit Employee' ")
    elif choice == "4":
        print("You Selected 'Exit Application' ")
        break
    else:
        print("Invalid choice. Make sure to only use numbers. Ex: 1, 2, 3, 4")