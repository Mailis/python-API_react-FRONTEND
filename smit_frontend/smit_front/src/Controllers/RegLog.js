/*jshint esversion: 6 */
import axios from 'axios';
import * as funcs from "../utils/showFuncs.js";
import * as sessionManager from "../utils/sessionManager.js"
import apiRouteNames from "../routes/api_routes.js";
import frontRouteNames from "../routes/front_end_routes.js";

const userLoginUrl = apiRouteNames.loginRoute;
const userRegisterUrl = apiRouteNames.registerRoute;
const front_usersUrl = frontRouteNames.users;

const postDuplicateErrorET = "Selline kasutajanimi ja/või email juba on olemas.";
const postErrorET = "Registreerimne ei õnnestunud. ";
const loginErrorET = "Sisselogimine ei õnnestunud. ";


export function validateUser(user, self){//, evt){
    console.log("User RegLog validateUser login user", user);
    console.log("User RegLog validateUser login userLoginUrl", userLoginUrl);
    axios.post(userLoginUrl, user)
    .then(function (response) {
        console.log("RegLog validateUser success: " , response);
        var succ = response.data[0]
        var token = response.data[1]
        var message = response.data[2]
        if (succ && token && user.fullname){
            // store the token in session
            sessionManager.saveSession(user.fullname, token);
            funcs.showSuccess(message);
            window.location.href=front_usersUrl;
        }
        else{
            funcs.showError(message);
        }
    })
    .catch(function (err) {
        console.log("RegLog validateUser error: " , err);
        funcs.showError(err, loginErrorET);
    });
}


export function registerUser(_user, self){//, evt){
    var user = {
        "fullname" : _user.username,
        "username" : _user.password,
        "phone" : _user.phone,
    }
    console.log("-----POST user:", user);
    axios.post(userRegisterUrl, user)
    .then(function (response) {
        console.log("-----POST user SUCC:", response);
        var resp_message = response.data.message.toString()
        if (resp_message.toLowerCase().indexOf("error") < 0 && response.data.data ){
            funcs.showSuccess(response);
            window.location.href=frontRouteNames.login;
        }
        else{
            funcs.showError(resp_message);
            //window.location.href=frontRouteNames.registreeri;
        }
        
    })
    .catch(function (err) {
        console.log("-----POST user ERR:", err);
        if(err.toString().indexOf("status code 400")){
            let errmessage = postDuplicateErrorET;
            funcs.showRichError(err, postErrorET + '\n\r\n\r' + errmessage);
        }
        else{
            funcs.showRichError(err, postErrorET);
        }
    });
}

