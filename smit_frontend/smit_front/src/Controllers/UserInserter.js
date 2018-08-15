/*jshint esversion: 6 */
import axios from 'axios';
import * as funcs from "../utils/showFuncs.js";
import * as authHeaders from "../utils/getHeaders.js";
import apiRouteNames from "../routes/api_routes.js";
export const postUserUrl = apiRouteNames.userRoute;



const postDuplicateErrorET = "Selline kasutajanimi ja/või email juba on olemas.";
const postErrorET = "Registreerimne ei õnnestunud. ";


export function addUser(_user, self){//, evt){
    var user = {
        "fullname" : _user.username,
        "username" : _user.password,
        "phone" : _user.phone,
    }
    console.log("-----POST user:", user);
    var _headers = authHeaders.getHeaders();
    axios.post(postUserUrl, user, {headers: _headers})
    .then(function (response) {
        console.log("-----POST user SUCC:", response);
        var data = response.data[1]
        var message = response.data[2]
        
        self.setState({users : data});
        funcs.showError(data + " " + message);
        
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

