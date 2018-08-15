/*jshint esversion: 6 */

var tokenKey = 'token'
var userKey = 'name'


export function generateSessionKey(fullname){
    return tokenKey + ':' + fullname;
}


export function getFullnameFromSessionKey(){
    return window.sessionStorage.getItem(userKey);
}


export function getAuthToken(){
    var fullname = getFullnameFromSessionKey();
    var authKey = generateSessionKey(fullname);
    return window.sessionStorage.getItem(authKey);
}


export function saveSession(fullname, token){
    var authKey = generateSessionKey(fullname);
    window.sessionStorage.setItem(authKey, token);
    window.sessionStorage.setItem(userKey, fullname);
}