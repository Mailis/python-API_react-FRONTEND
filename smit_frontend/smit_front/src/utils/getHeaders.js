/*jshint esversion: 6 */
import * as sessionManager from "./sessionManager.js"

export function getHeaders(userData = null){
    var headers = {};
    headers['Content-Type'] = "application/json";
    headers['X-Access-Token'] = sessionManager.getAuthToken();
    headers['X-Key'] = sessionManager.getFullnameFromSessionKey();
    
    return headers;
}