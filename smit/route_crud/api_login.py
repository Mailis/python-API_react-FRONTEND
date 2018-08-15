import json
import os,sys
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.insert(0,parent_dir)

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

from models import user_doe
from auth import token_generator


def login(request):
    if(request.is_json):
    
        content = request.get_json()
        logger.debug("api_login LOGIN request " + str(content))
        # print(content)
        user = user_doe.User()
        fullname = content['fullname']
        username = content['username']
        userExists, _ = user.userExists(fullname, username, "", False)
        
        if(userExists is True):
            message = "Login was sucessful!"
            logger.debug("api_login LOGIN message " + str(message))
            logger.debug("api_login LOGIN fullname " + fullname)
            isSuccess_enc, auth_token = token_generator.get_auth_token(fullname, 2)
            logger.debug("LOGIN auth isSuccess_enc" + str(isSuccess_enc))
            logger.debug("LOGIN auth token" + auth_token)
            if(isSuccess_enc is True):
                return (isSuccess_enc, auth_token, message)
            else:
                message = "Couldn't generate an auth token"
                logger.debug(" " + message)
                return (isSuccess_enc, "", message)
        else:
            message = "Login error: user does not exist"
            logger.debug(" " + message)
            return (userExists, "", message)
        
    else:
        message = "Application content must be sent in json format."
        logger.debug(" " + message)
        return (False, "", message)