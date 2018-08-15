/*jshint esversion: 6 */
import React, { Component } from 'react';

import '../css/common.css';

import * as userController from "../Controllers/getUsers";


class User  extends React.Component {
    
    constructor() {
      super();
      this.state = {
          user:{
            username : "",
            password : "",
            phone : "",
            token : ""
          },
          all_users : []

      };
      this.display_all_users = this.display_all_users.bind(this)
    }

    componentDidMount(){
      var current_user = this.state.user
      userController.getAllUsers(current_user, this);
    }

    display_all_users(all_users){
      
      var rows = []
      rows.push(
        <div key = "head" className = "tr_item">
          <div className = "td_item_header">
            id
          </div>
          <div className = "td_item_header">
            täisnimi
          </div>
          <div className = "td_item_header">
            kasutajanimi
          </div>
          <div className = "td_item_header">
            telefon
          </div>
        </div>
      );
      
      all_users.map( (u, k) => {
        rows.push(
        <div key = {k} className = "tr_item">
          <div className = "td_item">
            {u[0]}
          </div>
          <div className = "td_item">
            {u[1]}
          </div>
          <div className = "td_item">
            {u[2]}
          </div>
          <div className = "td_item">
            {u[3]}
          </div>
        </div>
        );
      })
      return rows;
    }


    render() {
      var all_users = this.state.all_users
      console.log('all_users', all_users, typeof(all_users));
      //it may be auth error notice
      var allUsers = (typeof(all_users) == typeof(""))? all_users : this.display_all_users(all_users);
      return (
        <div className="user_rows">
            {allUsers}

            <div id="error" className="error">{this.state.error} </div>
            <div id="success" className="success">{this.state.success} </div>
        </div>
      );
    }

}

export default User;
