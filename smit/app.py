from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

import json
import os,sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.insert(0,parent_dir)


from utilities import return_values
from route_crud import api_register
from route_crud import api_login
from route_crud import api_user_post
from route_crud import api_user_get
from route_crud import api_user_delete

from db import init_db

from auth import request_authentication as req_auth

from i18n.eng import messages

import app_configs

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

     
# logging.getLogger('flask_cors').level = logging.DEBUG

@app.route("/")
def home():
    return jsonify({'message': messages.welcome})

@app.route("/auth/login", methods=['POST'], strict_slashes=False)
def login_user():
    # POST request
    if request.method == 'POST':
        try: 
            response = api_login.login(request)
            return jsonify(response)
        except Exception  as e:
            logger.debug("LOGIN error " + str(e))
            # response = return_values.returnResponse(False, "Error", str(e))
            return (False, "Error", str(e))


@app.route("/auth/register", methods=['POST'], strict_slashes=False)
def register_user():
    # POST request
    if request.method == 'POST':
        try: 
            response = api_register.register(request)
            return (response)
        except Exception  as e:
            return jsonify(False, "Error", str(e))
            

@app.before_request
def before_request():
    init_db.create_db_and_tables()
    allowed_user_fullname = app_configs.ALLOWED_USER_FULLNAME
    allowed_username = app_configs.ALLOWED_USERNAME
    # logger.debug("before_request: allowed_user_fullname: ---- " + allowed_user_fullname)
    # logger.debug("before_request: allowed_usename: ---- " + allowed_usename)
    # logger.debug("before_request: REQUEAST: ---- ")
    # logger.debug("before_request: REQUEAST: " + str(request))
    auhtSuccess, payload = req_auth.authenticate_request(request)
    authSuccess = (auhtSuccess is True)
    # logger.debug('authSuccess ' +  str(authSuccess))
    str_p_load = str(payload)
    hasAllowdFullname = allowed_user_fullname in str_p_load
    # logger.debug('hasAllowdFullname ' +  str(hasAllowdFullname))
    app.isAuthenticatedUser = authSuccess and hasAllowdFullname


  

@app.route("/api/users", methods=['GET', 'POST'], strict_slashes=False)
def insert_user():
    # logger.debug('/api/users ' +  str(app.isAuthenticatedUser))
    if (app.isAuthenticatedUser is True):
        # POST request
        if (request.method == 'POST'):
            try: 
                response = api_user_post.insert_user(request)
                return jsonify(response)
            except Exception  as e:
                response = return_values.returnResponse(False, "Error", str(e))
                return jsonify(response)

        # GET request
        else:
            try:
                resp = api_user_get.get_all_users(request)
                return jsonify(resp)
            except Exception  as e:
                return jsonify(False, "Error", str(e))
    else:
        return jsonify(False, "Error", messages.NO_PERMISSIONS_NOTICE)

  

@app.route("/api/user/<int:id>", methods=['GET', 'DELETE'])
def get_user_by_id(id):
    if (app.isAuthenticatedUser is True):
        # GET request
        if request.method == 'GET':
            try:
                return jsonify( api_user_get.get_user_by_id(id) )
            except Exception as e:
                return jsonify(False, "Error", str(e))

        # DELETE request
        elif request.method == 'DELETE':
            try:
                return jsonify( api_user_delete.delete_user_by_id(id) )
            except Exception as e:
                return jsonify(False, "Error", str(e))
    else:
        return jsonify(False, "Error", messages.NO_PERMISSIONS_NOTICE)       


@app.route("/api/user/<string:fullname>", methods=['GET'])
def get_user_by_fullname(fullname):
    
    if (app.isAuthenticatedUser is True):
        # GET request
        if request.method == 'GET':
            try:
                return jsonify(api_user_get.get_user_by_fullname(fullname))
            except Exception  as e:
                return jsonify(False, "Error", str(e))
    
    else:
        return jsonify(False, "Error", messages.NO_PERMISSIONS_NOTICE)


    
