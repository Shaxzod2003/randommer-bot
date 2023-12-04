import requests
from randommer import Randommer

class Misc(Randommer):
    def get_cultures(self, api_key: str) -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of cultures
        '''
        endpoint="Misc/Cultures"

        url=self.get_url()+endpoint

        headers={
            "X-Api-Key":api_key
        }

        response=requests.get(url=url, headers=headers)

        return response.json()
    
    def get_random_address(self, api_key: str, number: int, culture='en') -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key
            number (str): number
            culture (str): culture

        Returns:
            list: random address
        '''
        
        endpoint="Misc/Random-Address"

        url=self.get_url()+endpoint

        headers={
            "X-Api-Key":api_key
        }
        p={
            "number":number,
            "culture":culture
        }
        response=requests.get(url=url, params=p, headers=headers )
        
        return response.json()

token="d5939e334d6743fcb137acc1f32eae08"
misc=Misc()
print(misc.get_cultures(api_key=token))
# print(misc.get_random_address(api_key=token,culture="en", number=7))