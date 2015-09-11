#!/usr/bin/python
import requests
import json
user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
login_url="http://app.comunia.me/api/v1/auth/login"
session_url="http://app.comunia.me/api/v1/session"
home_url="http://app.comunia.me/api/v1/home?teamValue=true"
class ComuniaMe:
    def __init__(self,username,password):
        self.credentials = {
            "email" : username,
            "password" : password
        }
        self.session = requests.session()
    def login(self):
        headers = {
            "User-Agent" : user_agent,
            "Content-Type" : "application/json;charset=UTF-8",
            "Accept" : "application/json, text/plain, */*"
        }
        res = self.session.post(login_url,data=json.dumps(self.credentials),headers=headers).text
        token = json.loads(res)
        self.authorization = "Bearer " + token["token"]
    def get_session_data(self):
        headers = {
            "User-Agent" : user_agent,
            "Accept" : "application/json, text/plain, */*",
            "Authorization" : self.authorization
        }
        res = self.session.get(session_url,headers=headers).text
        self.data = json.loads(res)
    def get_league_info(self):
        headers = {
            "User-Agent" : user_agent,
            "Accept" : "application/json, text/plain, */*",
            "X-League" : self.data["data"]["leagues"][0]["id"]
        }
        res = self.session.get(home_url,headers=headers).text
        self.league_info = json.loads(res)
