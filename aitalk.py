import requests
import json

class AiTalk :
    def __init__(self) :
        pass

    def __del__(self) :
        pass

    def send(self, message, uid='') :
        pass


class MiiboWrapper(AiTalk) :
    def __init__(self) :
        self.__url = 'https://api-mebo.dev/api'
        self.__api_key = ''
        self.__agent_id = ''
        self.__session = requests.Session()

    def __init__(self, api_key, agent_id): 
        self.__url = 'https://api-mebo.dev/api'
        self.__api_key = api_key
        self.__agent_id = agent_id
        self.__session = requests.Session()

    def __del__(self) :
        self.__session.close()

    def send(self, message, uid='') :
        if len(message) <= 0 :
            return ''
        if len(uid) <= 0 :
            uid = 'unknown_user'
        try : 
            res = self.__session.post(
                self.__url,
                headers = {
                    'Content-Type' : 'application/json',
                    'charset' : 'UTF-8'
                },
                data = json.dumps({
                    'api_key' : self.__api_key,
                    'agent_id' : self.__agent_id,
                    'utterance' : message,
                    'uid' : uid
                })
            )
            resbody = json.loads(res.text)
            return resbody['bestResponse']['utterance']
        except Exception as e :
            return ''