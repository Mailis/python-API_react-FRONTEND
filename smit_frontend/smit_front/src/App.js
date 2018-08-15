/*jshint esversion: 6 */
import React, { Component } from 'react';
import { Switch, Route } from 'react-router-dom';
import './App.css';

import Header from "./Components/Header";
import LoggerIn from "./Components/LoggerIn";
import RegisterUser from './Components/RegisterUser';
import User from './Components/User';
import AddUser from './Components/AddUser';

import * as checkUserisLoggedIn from "./utils/checkUSerIsLoggedIn.js"

import frontEndPaths from "./routes/front_end_routes";


class App extends Component {
  constructor() {
    super();
    this.state = {
        userIsLoggedIn : false
    };
  }
  componentDidMount(){
    this.setState({userIsLoggedIn : checkUserisLoggedIn.userIsSLoggedIn()});
  }
  render() {
    var userIsLoggedIn = this.state.userIsLoggedIn;
    console.log('APP userIsLoggedIn', userIsLoggedIn);
    return (
      <div className="App">
        <header className="App-header">
          <Header />
        </header>
        <div className="App-intro">
          <Switch>
              <Route exact path={frontEndPaths.slash} component={LoggerIn}/> 
              <Route path={frontEndPaths.login} component={LoggerIn}/> 
              <Route path={frontEndPaths.registreeri} component={RegisterUser}/> 
              {userIsLoggedIn && 
              <Route path={frontEndPaths.add_user} component={AddUser}/> 
              }
              {userIsLoggedIn && 
              <Route path={frontEndPaths.user} component={User}/> 
              }
              <Route path={frontEndPaths.default} component={LoggerIn}/> 
          </Switch>
        </div>
      </div>
    );
  }
}

export default App;
