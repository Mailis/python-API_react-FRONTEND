import json

def returnResponse(status, data, message=""):
    return json.dumps({'status': status, 'data': data, 'message': message})