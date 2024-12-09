from enum import Enum
class Config(Enum):

    FIELD_MAPPING = {
        "Alert_Sequence_No" : "Alert Sequence No"
        "Client_code": "Account number",
        "Amount": "Amount",
        "Posting_Date": "Value Date",
        "Reference_No": "User Reference Number",
        "Remitter_Account": "Remitter Account",
        "Remitter_Name": "Remitter Name",
        "Remitter_Bank": "Remitter Bank",
        "Remitter_IFSC": "Remitter IFSC"
    }

    FIELD_DATATYPE_MAPPING = {
        "Alert_Sequence_No": "string",
        "Client_code" : "string",
        "Amount": "float",
        "Posting_Date": "string",
        "Reference_No": "string",
        "Remitter_Account": "string",
        "Remitter_Name": "string",
        "Remitter_Bank": "string",
        "Remitter_IFSC": "string"
    }

    # Edit the variables before using them
    API_ENDPOINT = "https API Endpoint"

    USERNAME = "Username" 
    PASSWORD =  "Passowrd" 

    COMPANY = "Sampoorna Feeds Pvt. Ltd"

    RESPONSE_MAPPING = {
        "Duplicate" : "1",
        "TechnicalReject" : "1",
        "Success" : "0"
    }

    LOGS_PATH = "./"

    ADDITIONAL_FIELDS = {
        "Document_Type" : "Reciept"
    }
    

# {
#     "Account_No": "098584600000041",
#     "Amount": 123,
#     "Client_code": "SFFD01SFC05512",
#     "Client_name": "",
#     "Customer_No": "SFC05512",
#     "Document_No": "SRBR2425/22523",
#     "Document_Type": "Reciept",
#     "Posting_Date": "2024-09-22",
#     "Processed": true,
#     "Posted": false,
#     "Reference_No": "BARBX24266897517",
#     "Remitter_Account": "21500200001277",
#     "Remitter_Name": "JANNAT POULTRY FEED SUPPLIER",
#     "Remitter_Bank": "",
#     "Remitter_IFSC": "BARB0ALWDEL"
# }

# {
#     "Entry_No": 63597,
#     "Account_No": "098584600000041",
#     "Amount": 132000,
#     "Client_code": "SFFD01SFC02460",
#     "Client_name": "",
#     "Customer_No": "SFC02460",
#     "Document_No": "SRBR2425/22525",
#     "Document_Type": "Reciept",
#     "Posting_Date": "2024-09-22",
#     "Processed": true,
#     "Posted": false,
#     "Reference_No": "426615743923",
#     "Remitter_Account": "030605010221",
#     "Remitter_Name": "S G P FARMS",
#     "Remitter_Bank": "",
#     "Remitter_IFSC": "ICIC0000306",
#     "Posting_Erro": "",
#     "File_Name": "CMS_ECOLLECT_SFFD01_ALL_ALL22092024_1613.xls",
#     "Transaction_Status": "CREDITED"
# }


# {
#     "Alert Sequence No" : "000303100109572403173",
#     "Virtual Account": "ZERNSE",
#     "Account number": "00321234560198", 
#     "Debit Credit": "Credit",
#     "Amount": 5612.22,  
#     "Remitter Name": "PRAKASH KUMAR", 
#     "Remitter Account": "25781212184", 
#     "Remitter Bank": "Bank of Baroda", 
#     "Remitter IFSC": "CITI000241"
#     "Cheque No":"", 
#     "User Reference Number": "FT124542",
#     "Mnemonic Code": "NEFT",
#     "Value Date": "2017-03-24",
#     "Transaction Description": "Test NEFT transaction",
#     "Transaction Date": "2017-03-24 08:35"
# }

