/*jshint esversion: 6 */
import * as authHeaders from "./getHeaders.js"

export function userIsSLoggedIn(){
    var isUserLoggedIn = false;
    var headers = authHeaders.getHeaders()
    var hasTokenKey = 'X-Access-Token' in headers;
    console.log("loggedin: headers ", headers);
    console.log("loggedin: hasToken ", hasTokenKey);
    var hasTokenValue = headers['X-Access-Token'] != undefined;
    if(hasTokenKey){
        if(hasTokenValue){
            isUserLoggedIn = true;
        }
    }
    console.log("loggedin: userIsLoggedIn", isUserLoggedIn)
    console.log("loggedin: hasTokenValue ", hasTokenValue)
    return isUserLoggedIn;
}