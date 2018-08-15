/*jshint esversion: 6 */
import axios from 'axios';
import * as funcs from "../utils/showFuncs.js";
import * as authHeaders from "../utils/getHeaders.js";
import apiRouteNames from "../routes/api_routes.js";
import frontRouteNames from "../routes/front_end_routes.js";
export const userLoginUrl = apiRouteNames.loginRoute;
export const userRegisterUrl = apiRouteNames.registerRoute;
export const api_usersUrl = apiRouteNames.userRoute;
export const front_usersUrl = frontRouteNames.users;



export function getAllUsers(users, self){
    console.log("-----GET ALL users:", users);
    var _headers = authHeaders.getHeaders();
    console.log("getAllUsers HEADERS", _headers);
    axios.get(api_usersUrl, {headers: _headers})
    .then(function (response) {
        console.log("-----GET ALL users SUCC:", response);
        var succ = response.data[0]
        var data = response.data[1]
        var message = response.data[2]
        if (succ){
            self.setState({all_users : data});
        }
        else{
            funcs.showError(data + ": " + message);
            //window.location.href=frontRouteNames.registreeri;
        }
        
    })
    .catch(function (err) {
        console.log("-----GET ALL users  ERR:", err.toString());
        funcs.showError(err);
    });
}

