def transformPayload(input_payload, mapping):
    transformed_payload = dict()
    for dest_field, source_field in mapping.items():
        if input_payload.get(source_field):
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

