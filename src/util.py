
def filter_not_permited_headers(input_header):
    not_permit = ["content-encoding", "content-length"]
    response_headers = {}
    for item in input_header:
        if item.lower() not in not_permit:
            response_headers[item] = input_header[item]
    return response_headers


def cdic_to_dic(headers):
    result = {}
    for item in headers:
        result[item] = headers[item]
    return result
