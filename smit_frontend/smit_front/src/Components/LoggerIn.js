/*jshint esversion: 6 */
import React, { Component } from 'react';

import * as funcs from "../utils/showFuncs.js";
import * as userValidator from "../Controllers/RegLog.js";

const logIn = "Logi sisse";

const passWordsMissing ="Kasutajanimi puudub!";
const fullnameMissing ="Täisnimi puudub!";
const somthMissing ="Kõik väljad peavad täidetud olema";

class LoggerIn  extends React.Component {
    
    constructor() {
      super();
      this.state = {
          user:{
            fullname : "",
            username : "",
            token : ""
          }
      };
      this.handleLoginUser = this.handleLoginUser.bind(this);
      this.handleUserDataChange = this.handleUserDataChange.bind(this);
    }

    componentDidMount(){
        var userData = this.state.user;
        if(userData.username && userData.role){
            this.props.takeproperties(userData);
            window.location.reload();
        }
    }

//----------------------------POST------------------------------------
  
    handleLoginUser(evt){
      evt.preventDefault();
      console.log('STATE', this.state.user);
      var userData = this.state.user;
      //compare equality of passwords
      if(userData.fullname && userData.username){
        userValidator.validateUser(userData, this);
      }
      else if(!userData.fullname){
        funcs.showError(fullnameMissing);
      }
      else if(!userData.username){
        funcs.showError(passWordsMissing);
      }
      else{
        funcs.showError(somthMissing);
      }
    }



    handleUserDataChange(evt){
        var currentUser = this.state.user;
        // console.log('STATE',currentUser);
        // console.log('evt.target.name, evt.target.value', evt.target.name, evt.target.value);
        if(evt){
            evt.preventDefault();
            let name = evt.target.name;
            let val = evt.target.value;
            console.log('name, value', name, val);
            currentUser[name] = val;
            this.setState({user : currentUser});
            // this.props.takeproperties(currentUser);
        }
    }


    render() {
        var  user = this.state.user;


      console.log('STATE user', this.state.user);

        const fullname = "Sinu täisnimi:";
        const fullname_placeholder = "täisnimi";

        
        const username = "Sinu kasutajanimi:";
        const username_placeholder = "kasutajanimi";
        


      return (
        <div className="relativePosition">
            <form onSubmit={this.handleRegisterUser}>
                <label className = "logreg"> 
                    <h1>{fullname}</h1>
                    <input 
                        placeholder={fullname_placeholder}
                        value = {user.fullname}
                        name = "fullname"
                        onChange = {this.handleUserDataChange}
                        className="logreg_input"
                        type="text"
                        required 
                    />
                </label>

                <label className = "logreg"> 
                    <h1>{username}</h1>
                    <input 
                        placeholder={username_placeholder}
                        value = {user.username}
                        name = "username"
                        onChange = {this.handleUserDataChange}
                        className="logreg_input"
                        type="password"
                        required 
                        />
                </label>

                <br />
                <br />
                <button className="save_btn save_buton" 
                        onClick={this.handleLoginUser}>
                        {logIn}
                </button>
            </form>

            <div id="error" className="error">{this.state.error} </div>
            <div id="success" className="success">{this.state.success} </div>
        </div>
      );
    }

}

export default LoggerIn;
