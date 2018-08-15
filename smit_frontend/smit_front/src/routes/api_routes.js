/*jshint esversion: 6 */

/* 
//local
var domainUrl = 'http://localhost';
var portt = '8000';
var basicUrl = domainUrl + ":" + portt;
var apiRoute = basicUrl + '/api';
 */

 
//remote
// "http://127.0.0.1:5000"
var backend_url = "http://127.0.0.1:5000" //process.env.SMIT_BACKEND_API_URL;
var apiRoute = backend_url  + '/api';
var authRoute = backend_url  + '/auth';


var apiRouteNames = {
    apiRoute : apiRoute,
    userRoute : apiRoute + '/users/',
    loginRoute : authRoute + '/login',
    registerRoute : authRoute + '/register',
    logoutRoute : authRoute + '/logout'
};


export default apiRouteNames;