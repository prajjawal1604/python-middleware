from enum import Enum
class Config(Enum):

    FIELD_MAPPING = {
        "alertSequenceNo" : "Alert Sequence No",
        "account_No": "Account number",
        "client_code": "Virtual Account",
        "amount": "Amount",
        "posting_Date": "Value Date",
        "reference_No": "User Reference Number",
        "remitter_Account": "Remitter Account",
        "remitter_Name": "Remitter Name",
        "remitter_Bank": "Remitter Bank",
        "remitter_IFSC": "Remitter IFSC"
    }

    FIELD_DATATYPE_MAPPING = {
        "alertSequenceNo": "string",
        "client_code": "string",
        "account_No" : "string",
        "amount": "float",
        "posting_Date": "string",
        "reference_No": "string",
        "remitter_Account": "string",
        "remitter_Name": "string",
        "remitter_Bank": "string",
        "remitter_IFSC": "string"
    }

    # Edit the variables before using them
    API_ENDPOINT = "API ENDPOINT"

    USERNAME = "USERNAME" 
    PASSWORD =  "PASSWORD" 


    COMPANY = "Sampoorna Feeds Pvt. Ltd"

    RESPONSE_MAPPING = {
        "Duplicate" : "1",
        "TechnicalReject" : "1",
        "Success" : "0"
    }

    LOGS_PATH = "./"

    ADDITIONAL_FIELDS = {
        # "Document_Type" : "Reciept"

    }