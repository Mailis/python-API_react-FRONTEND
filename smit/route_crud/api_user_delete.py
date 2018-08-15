import json
import os,sys
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.insert(0,parent_dir)

from utilities import return_values
from models import user_doe


def delete_user_by_id(id):
    user = user_doe.User()
    isSuccess, data = user.delete_user_by_id(id)
    # print(data)
    if(isSuccess is not False and len(data) > 0):
        message = "User with id " + str(id) + " was deleted!"
        return return_values.returnResponse(True, id, message)
    else:
        message = "Error happened while trying to delete user with id " + str(id)
        return return_values.returnResponse(False, data, message)