import requests
from randommer import Randommer


class Name(Randommer):
    def get_name(self, api_key: str, nameType: str, quantity: int) -> list:
        '''get name

        Args:
            api_key (str): api key
            nameType (str): nameType
            quantity (str): number of names

        Returns:
            list: list of names
        '''
        endpoint="Name"

        url=self.get_url()+endpoint

        headers={
            "X-Api-Key":api_key
        }
        p={
            "nameType":nameType,
            "quantity":quantity
        }
        response=requests.get(url=url, params=p, headers=headers )
        
        return response.json()
    
    def get_name_suggestions(self, api_key: str, startingWords: str) -> list:
        '''get name suggestions

        Args:
            api_key (str): api key
            startingWords (str): startingWords

        Returns:
            list: list of name suggestions
        '''
        endpoint="Name/Suggestions"

        url=self.get_url()+endpoint

        headers = {
            "X-Api-Key": api_key
        }

        p={
            "startingWords":startingWords
        }

        response=requests.get(url=url, params=p, headers=headers)

        if response.status_code == 200:
            return response.json()
        
        return response.status_code
    
    def get_name_cultures(self, api_key: str) -> list:
        '''get available cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of names
        '''
        endpoint="Name/Cultures"

        url = self.get_url() + endpoint

        headers = {
            "X-Api-Key": api_key
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()

        return response.status_code

token="d5939e334d6743fcb137acc1f32eae08"
name=Name()
print(name.get_name(api_key=token, nameType="firstname", quantity=7))
# print(name.get_name_suggestions(api_key=token, startingWords="ma"))
# print(name.get_name_cultures(token))