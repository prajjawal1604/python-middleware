from exceptions import InvalidPayloadException

def transformPayload(input_payload, mapping):
    transformed_payload = dict()
    for dest_field, source_field in mapping.items():
        if source_field in input_payload.keys():
            transformed_payload[dest_field] = input_payload.get(source_field)
    return transformed_payload

def coerce_value(value, dtype):
    if dtype == "float":
        return float(value)
    elif dtype == "string":
        return str(value)
    else:
        raise ValueError(f"Unsupported data type: {dtype}")

def getCoercedPayload(json_payload, dtype_mapping):
    coerced_payload = {
        key: coerce_value(value, dtype_mapping[key])
        for key, value in json_payload.items()
    }
    return coerced_payload

def validateRequest(request):
    if not isinstance(request.get_json(), dict):
        raise InvalidPayloadException("Non Json payload", 403)
    request_array = request.get_json().get("GenericCorporateAlertRequest", [])
    
    if not len(request_array) > 0:
        raise InvalidPayloadException("invalid payload", 403)
    elif not request_array[0]:
        raise InvalidPayloadException("invalid payload", 403)
    else:
        return request_array[0]

def getDomainReferenceNumber(request):
    if not isinstance(request.get_json(), dict):
        return None
    request_array = request.get_json().get("GenericCorporateAlertRequest", [])
    if len(request_array) > 0:
        return request_array[0].get("Alert Sequence No")


