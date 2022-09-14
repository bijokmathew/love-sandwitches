import gspread 
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS= CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT=gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("love_sandwiches")

def get_sales_data():
    """
    Get sales figures input from the user.
    Run a while loop to collect a valid data from the user
    via the terminal, which must be a string of 6 numbers 
    seperated by commas.The loop will repeatdly request the data
    until it is valid
    """
    while True:
        print("Please enter the sales data from the last market")
        print("Data should be six numbers seperated by commaa.")
        print("Example : 10, 30, 60, 40, 90, 35 \n")

        data_str = input("Enter your data here: ")
        sales_data = data_str.split(",")
        if validate_data(sales_data) == True:
            print("Data is valid")
            break
        
    return sales_data

def validate_data(values):
    """
    Inside trt,converts all string values in to integers.
    Raise ValueError if strings cannot convert in to integer,
    or if there are not exactly 6 numbers
    """
    try:
        [int(value) for value in values]
        if(len(values)!=6):
            raise ValueError(f"Exactly 6 values required, you provided {len(values)}")
    except ValueError as e:
        print(f"Invalid data :{e},Please try again..")
        return False
    return True
def update_sales_worksheet(sales_data):
    """
    update sales worksheet,add new row with list data provided
    """
    print("Updating sales worksheet...\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(sales_data)
    print("sales worksheet updated successfully...\n")



data =get_sales_data()
sales_data = [int(val) for val in data]
update_sales_worksheet(sales_data)
