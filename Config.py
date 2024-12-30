from enum import Enum
class Config(Enum):

    FIELD_MAPPING = {
        "Alert_Sequence_No" : "Alert Sequence No",
        "Account_no": "Account number",
        "Client_code": "Virtual Account",
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
        "Client_code": "string",
        "Account_no" : "string",
        "Amount": "float",
        "Posting_Date": "string",
        "Reference_No": "string",
        "Remitter_Account": "string",
        "Remitter_Name": "string",
        "Remitter_Bank": "string",
        "Remitter_IFSC": "string"
    }

    # Edit the variables before using them
    API_ENDPOINT = "API Endpoint"

    USERNAME = "Username" 
    PASSWORD =  "Password" 

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