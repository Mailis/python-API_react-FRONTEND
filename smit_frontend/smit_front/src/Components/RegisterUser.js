/*jshint esversion: 6 */
import React, { Component } from 'react';

import * as funcs from "../utils/showFuncs.js";
import * as userValidator from "../Controllers/RegLog.js";
import '../css/common.css';

const register = "Registreeri";


const passWordsAreNotEqual = "Salasõnad on erinevad!";
const passWordsMissing ="Salasõnad puuduvad!";

class RegisterUser  extends React.Component {
    
    constructor() {
      super();
      this.state = {
          user:{
            username : "",
            password : "",
            password_conf : "",
            phone : "",
            token : ""
          }
      };
      this.handleRegisterUser = this.handleRegisterUser.bind(this);
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
  
    handleRegisterUser(evt){
      evt.preventDefault();
      console.log('STATE', this.state.user);
      var userData = this.state.user;
      //compare equality of passwords
      if(userData.password && userData.password_conf){
        if(userData.password !== userData.password_conf){
            evt.preventDefault();
            funcs.showError(passWordsAreNotEqual)
        }
        else{
            //send user to API session
            if(userData.username && userData.phone && userData.password){
                userValidator.registerUser(userData, this);//, evt);
            }
        }
      }
      else{
        evt.preventDefault();
        funcs.showError(passWordsMissing);
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

        const name = "Sinu täisnimi:";
        const name_placeholder = "fullname";

        const phone = "Telefon:";
        const phone_placeholder = "telefon";

        const password = "Sinu kasutajanimi:";
        const password_placeholder = "kasutajanimi";
        
        const password_conf = "Korda kasutajanime:";
        const password_conf_placeholder = "kasutajanime kinnitus";
        


      return (
        <div className="relativePosition">

            <form onSubmit={this.handleRegisterUser}>
                <label className = "logreg"> 
                    <h1>{name}</h1>
                    <input 
                        placeholder={name_placeholder}
                        value = {user.username}
                        name = "username"
                        onChange = {this.handleUserDataChange}
                        className="logreg_input"
                        type="text"
                        required 
                    />
                </label>
                <label className = "logreg"> 
                    <h1>{phone}</h1>
                    <input 
                        placeholder={phone_placeholder}
                        value = {user.phone}
                        name = "phone"
                        onChange = {this.handleUserDataChange}
                        className="logreg_input"
                        type="phone"
                        min = "1"
                        required 
                    />
                </label>
                

                <label className = "logreg"> 
                    <h1>{password}</h1>
                    <input 
                        placeholder={password_placeholder}
                        value = {user.password}
                        name = "password"
                        onChange = {this.handleUserDataChange}
                        className="logreg_input"
                        type="password"
                        required 
                        />
                </label>

                <label className = "logreg"> 
                    <h1>{password_conf}</h1>
                    <input 
                        placeholder={password_conf_placeholder}
                        value = {user.password_conf}
                        name = "password_conf"
                        onChange = {this.handleUserDataChange}
                        className="logreg_input"
                        type="password"
                        required 
                    />
                </label>
                <br />
                <br />
                <button className="save_btn save_buton" 
                        onClick={this.handleRegisterUser}>
                        {register}
                </button>
            </form>

            <div id="error" className="error">{this.state.error} </div>
            <div id="success" className="success">{this.state.success} </div>
        </div>
      );
    }

}

export default RegisterUser;
