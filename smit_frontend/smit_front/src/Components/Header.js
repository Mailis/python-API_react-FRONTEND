/*jshint esversion: 6 */
import React, { Component } from 'react';
import { Link } from 'react-router-dom';

import frontRouteNames from "../routes/front_end_routes.js";
import * as checkUserisLoggedIn from "../utils/checkUSerIsLoggedIn.js"

var users_url  = frontRouteNames.users;
var add_user_url  = frontRouteNames.add_user;
var registreeri_url  = frontRouteNames.registreeri;
var login_url  = frontRouteNames.login;
var logout_url  = frontRouteNames.logout;

class Headaer  extends React.Component {
    
    constructor() {
      super();
      this.state = {
          userIsLoggedIn : false
      };
    }

    componentDidMount(){
        this.setState({userIsLoggedIn : checkUserisLoggedIn.userIsSLoggedIn()});
    }

    logout(evt){
        window.sessionStorage.clear();
        this.setState({userIsLoggedIn : false})
        window.location.href = login_url;
    }

    displyLinks = () =>{
        var links = {
            'registreeri'  : registreeri_url,
            'kõik kasutajad' : users_url,
            'lisa kasuaja'  : add_user_url
        }
        var login_links = {
            'login_url'  : login_url,
            'logout_url'  : logout_url
        }

        var linkitems = []
        var userIsLoggedIn = this.state.userIsLoggedIn;
        userIsLoggedIn? 
                linkitems.push(<Link to ={login_links['logout_url']}  
                                    onClick ={(evt) => this.logout(evt)}>
                                    logi välja
                                </Link>)
                :
                linkitems.push(<Link to ={login_links['login_url']}>logi sisse</Link>)

        for (var key in links) {
            if (links.hasOwnProperty(key)) {       
                linkitems.push(
                <Link to ={links[key]}>{key}</Link>
                );
            }
        }
        
        return linkitems;
    }

    render() {
        var dlinks = this.displyLinks();


      return (
        <div className="relativePosition">
            <div className="App-title">salajased kasutajad</div>
            <ul id="horizontal-list">
                
            {dlinks.map((link, idx) => (
                <li key = {idx}>
                    {link}
                </li>
            ))}
            
            </ul>
        </div>
      );
    }

}

export default Headaer;
