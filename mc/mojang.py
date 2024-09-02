# -*- coding: utf-8 -*-
from ast import Pass
from msilib.schema import Error
import requests

class Mojang():
    MojangAPIURL='https://api.mojang.com'
    MojangSessionAPIURL='https://sessionserver.mojang.com'

    @classmethod
    def get_uuid(self,playername:str):
        try:
            r=requests.get('%s/users/profiles/minecraft/%s'%(self.MojangAPIURL,playername))
            if r.status_code==204 or r.status_code==400:
                pass
            else:
                i=r.json
                UUID = i['id']
                return UUID
        except Exception as e:
            pass
    
    @classmethod
    def get_playername_history(self,uuid:str=None,playername:str=None):
        r=requests.get('%s/user/profiles/%s/names'%(self.MojangAPIURL,uuid)).json()
        return r
    

