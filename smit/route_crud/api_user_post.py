import json
import os,sys
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.insert(0,parent_dir)

from utilities import return_values
from models import user_doe

def insert_user(request):
    if(request.is_json):
        content = request.get_json()
        # print(content)
        user = user_doe.User()
        fullname = content['fullname']
        username = content['username']
        phone = content['phone']
        isSuccessfulPost, result = user.insert_user(fullname, username, phone)
        if(isSuccessfulPost is True):
            message = "User Inserted!"
            return(isSuccessfulPost, result, message)
        else:
            message = "User Insertion Error!"
            return(isSuccessfulPost, result, message)
        
    else:
        message = "Application content must be sent in json format."
        return(False, "", message)