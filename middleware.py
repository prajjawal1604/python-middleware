from flask import Flask, request, jsonify, abort
from utils import transformPayload, getCoercedPayload
import requests
from Config import Config
import json
import urllib
import time
from logger import Logger
logger = Logger().get_logger()

app = Flask(__name__)



@app.before_request
def before_request():
    """Record the start time before the request is processed."""
    request.start_time = time.time()
    print(type( request.get_json()))
    log_message = {"message" : "request payload recieved", "payload" : request.get_json() }
    logger.info(json.dumps(log_message) )

@app.route('/add', methods=['POST'])
def processRequest():
    input_request_data = request.get_json()
    try:
        domainReferenceNo = input_request_data.get("Alert Sequence No")
        logger.info(f"Processing domainReferenceNo : {domainReferenceNo}") 
        params = {
            "company" : Config.COMPANY.value
        }
        field_mapping  = Config.FIELD_MAPPING.value
        api_endpoint = Config.API_ENDPOINT.value
        field_datatype_mapping = Config.FIELD_DATATYPE_MAPPING.value
        
        username = Config.USERNAME.value
        password = Config.PASSWORD.value

        transformed_request_data = transformPayload(input_request_data, field_mapping)
        # log_message = {"message" : "field names changed", "payload" : transformed_request_data}
        # logger.info(log_message)
        
        coerced_request_data = getCoercedPayload(transformed_request_data, field_datatype_mapping)
        # log_message = {"message" : "handled datatypes", "payload" : coerced_request_data}
        # logger.info(log_message)

        coerced_request_data.update(Config.ADDITIONAL_FIELDS.value)
        print(coerced_request_data)
        # log_message = {"message" : "updated with additional fields", "payload" : coerced_request_data}
        # logger.info(log_message)

        response = requests.post(
            api_endpoint, 
            json=coerced_request_data, 
            auth = (username, password), 
            params=params
        )

        if response.status_code == 201:
            errorCode = "0"
            errorMessage = "Success"
            status_code = response.status_code
        elif response.status_code != 201:
            errorMessage = "TechnicalReject"
            status_code = response.status_code
    except Exception as e:
        print(e)
        errorMessage = "TechnicalReject"
        status_code = 500 
    finally:
        client_response = {
            "domainReferenceNo" : domainReferenceNo,
            "errorCode" : Config.RESPONSE_MAPPING.value.get(errorMessage),
            "errorMessage" : errorMessage
        }
        return  client_response, status_code

@app.after_request
def modify_response(response):
    response_data = response.get_json()
    if response_data:
        modified_response = dict()
        modified_response["GenericCorporateAlertResponse"] = response_data
        response.set_data(jsonify(modified_response).data)
    time_taken =  time.time() - request.start_time
    logger.info(f"time taken to process request : {time_taken} seconds, domainReferenceNo : {response_data.get('domainReferenceNo')}")
    if time_taken < 2:
        pass 
    else:
        logger.error(f"Error : time taken {time_taken} seconds, domainReferenceNo : {response_data.get('domainReferenceNo')}")
    return response

if __name__ == '__main__':
    res = app.run(host='0.0.0.0', port=443, debug=True)
