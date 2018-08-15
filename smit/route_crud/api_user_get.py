import json
import os,sys
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.insert(0,parent_dir)


import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


from utilities import return_values
from models import user_doe

def get_all_users(request):
    user = user_doe.User()
    isSuccess, data = user.get_all_users()
    # logger.debug("get all users" + str(isSuccess) + str(data))
    if(isSuccess is True):
        return (True, data)
    else:
        return (False, data)


def get_user_by_fullname(fullname):
    user = user_doe.User()
    isSuccess, data = user.get_user_by_fullname(fullname)
    if(isSuccess is not False and len(data) > 0):
        user_id, f_name, u_name, phone = data
        return return_values.returnResponse(True, (user_id, f_name, phone))
    else:
        return return_values.returnResponse(False, data)


def get_user_by_id(id):
    user = user_doe.User()
    isSuccess, data = user.get_user_by_id(id)
    if(isSuccess is not False and len(data) > 0):
        user_id, f_name, _, phone = data
        return return_values.returnResponse(True, (user_id, f_name, phone))
    else:
        return return_values.returnResponse(False, data)