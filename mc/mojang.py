# -*- coding: utf-8 -*-
from ast import Pass
from msilib.schema import Error
import requests

class Mojang():
    MojangAPIURL='https://api.mojang.com'
    MojangSessionAPIURL='https://sessionserver.mojang.com'

    @classmethod
    def get_uuid(self,playername:str):
        r=requests.get('%s/users/profiles/minecraft/%s'%(self.MojangAPIURL,playername)).json()
        UUID = r['id']

        return UUID
    
    @classmethod
    def get_playername_history(self,uuid:str=None,playername:str=None):
        r=requests.get('%s/user/profiles/%s/names'%(self.MojangAPIURL,uuid)).json()
        return r
    

