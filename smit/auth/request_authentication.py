import json
import os,sys
current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.insert(0,parent_dir)

from . import token_generator
from utilities import return_values



import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def authenticate_request(request):
        # get the auth token
        logger.debug("request.headers HEADERS" + str(request.headers) )
        auth_token = request.headers.get('X-Access-Token')
        auth_fullname = request.headers.get('X-Key')
        logger.debug("request.headers X-Access-Token " + str(auth_token) )
        logger.debug("request.headers X-Key " + str(auth_fullname) )
        return token_generator.decode_auth_token_HS256(auth_token, auth_fullname)
        