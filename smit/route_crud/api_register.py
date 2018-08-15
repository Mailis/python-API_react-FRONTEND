
import json
import os,sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.insert(0,parent_dir)

from utilities import return_values
from models import user_doe
from auth import token_generator


import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def register(request):
    if(request.is_json):
        content = request.get_json()

        logger.debug("register CONTENT" + str(content))
        
        user = user_doe.User()
        fullname = content['fullname']
        username = content['username']
        phone = content['phone']
        userExists, _ = user.userExists(fullname, username, phone, False)

        logger.debug("register userExists" + str(userExists))
        
        if(userExists is not True):
            isSuccessfulPost, result = user.insert_user(fullname, username, phone)
            logger.debug("register result" + str(result))
            
            if(isSuccessfulPost is True):
                message = "Registration was sucessful!"
                response = return_values.returnResponse(isSuccessfulPost, result, message)
                # response.status_code = 201
                return response
            else:
                message = "User Registration Error!"
                response = return_values.returnResponse(isSuccessfulPost, result, message)
                # response.status_code = 400
                return response

        else:
            message = "Register error: user already exists"
            return return_values.returnResponse(userExists, "", message)
        
    else:
        message = "Application content must be sent in json format."
        return return_values.returnResponse(False, "", message)