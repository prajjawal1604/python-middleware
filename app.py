from flask import Flask, request, render_template
from utils import transformPayload, getCoercedPayload, validateRequest, getDomainReferenceNumber
import requests
from Config import Config
import json
from exceptions import InvalidPayloadException
# import urllib
import time
from logger import Logger

logger = Logger().get_logger()

app = Flask(__name__)

# Route to serve the HTML page
@app.route('/')
def home():
    return render_template('index.html')

@app.before_request
def before_request():
    """Record the start time before the request is processed."""
    request.start_time = time.time()
    if request.content_type == 'application/json':
        log_message = {
            "message": "request payload received",
            "payload": request.get_json()
        }
        logger.info(json.dumps(log_message))
    else:
        logger.info("Non-JSON request received.")


@app.route('/add', methods=['POST'])
def processRequest():
    try:
        domainReferenceNo = getDomainReferenceNumber(request)
        input_request_data = validateRequest(request) 
        log_message = {
            "message" : f"processing domainReferenceNo {domainReferenceNo}"
        }
        logger.info(json.dumps(log_message))
        params = {
            "company": Config.COMPANY.value
        }
        field_mapping = Config.FIELD_MAPPING.value
        api_endpoint = Config.API_ENDPOINT.value
        field_datatype_mapping = Config.FIELD_DATATYPE_MAPPING.value

        username = Config.USERNAME.value
        password = Config.PASSWORD.value

        transformed_request_data = transformPayload(input_request_data, field_mapping)
        coerced_request_data = getCoercedPayload(transformed_request_data, field_datatype_mapping)
        coerced_request_data.update(Config.ADDITIONAL_FIELDS.value)
        log_message = {
            "message": "final request payload",
            "payload": coerced_request_data
        }
        logger.info(json.dumps(log_message))

        response = requests.post(
            api_endpoint,
            json=coerced_request_data,
            auth=(username, password),
            params=params
        )
        log_message = {
            "message" : f"processed domainReferenceNo {domainReferenceNo}",
            "ERP Response" : response.json()
        }
        logger.info(json.dumps(log_message))
        if response.status_code == 200:
            errorMessage = "Success"
            status_code = response.status_code
        elif "Duplicate" in response.json().get("error",{}).get("message"):
            errorMessage = "Duplicate"
            status_code = response.status_code
        else:
            errorMessage = "TechnicalReject"
            status_code = response.status_code
    except InvalidPayloadException as e:
        logger.error(f"Exception occurred: {e}")
        errorMessage = "TechnicalReject"
        status_code = e.error_code
    except Exception as e:
        logger.error(f"Exception occurred: {e}")
        errorMessage = "TechnicalReject"
        status_code = 500
    finally:
        client_response = {
            "domainReferenceNo": domainReferenceNo,
            "errorCode": Config.RESPONSE_MAPPING.value.get(errorMessage),
            "errorMessage": errorMessage
        }
        return client_response, status_code

@app.after_request
def modify_response(response):
    try:
        # Modify only JSON responses
        if response.content_type == 'application/json':
            response_data = response.get_json() or {}
            if response_data:
                modified_response = {"GenericCorporateAlertResponse": response_data}
                response.set_data(json.dumps(modified_response))

        time_taken = time.time() - request.start_time
        logger.info(f"time taken to process request: {time_taken} seconds")

        if response.content_type == 'application/json':
            domainReferenceNo = response_data.get('domainReferenceNo', 'N/A')
            if time_taken >= 2:
                logger.error(f"Error: time taken {time_taken} seconds, domainReferenceNo: {domainReferenceNo}")
            else:
                logger.info(f"Request processed successfully, domainReferenceNo: {domainReferenceNo}")
    except Exception as e:
        logger.error(f"Exception in modify_response: {e}")
        raise
    return response

if __name__ == '__main__':
    # Run the application on localhost at port 5000
    app.run(host='0.0.0.0', port=85, debug=True)
