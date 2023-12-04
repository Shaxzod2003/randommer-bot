import requests
from randommer import Randommer


class Phone(Randommer):
    def generate(self, api_key: str, CountryCode: str, Quantity: int) -> list:
        '''get bulk telephone numbers for a country

        Args:
            api_key (str): api key
            CountryCode (str): CountryCode ex: 'uz'
            Quantity (str): Quantity

        Returns:
            list: list of phone numbers
        '''
        endpoint="Phone/Generate"

        url=self.get_url()+endpoint

        headers = {
            "X-Api-Key": api_key
        }

        p={
            "CountryCode":CountryCode,
            "Quantity":Quantity
        }

        response=requests.get(url=url, params=p, headers=headers)

        if response.status_code == 200:
            return response.json()
        
        return response.status_code
    
    def get_IMEI(self, api_key: str, Quantity: int) -> list:
        '''get bulk imei

        Args:
            api_key (str): api key
            Quantity (str): Quantity

        Returns:
            list: list of phone numbers
        '''
        endpoint="Phone/IMEI"

        url=self.get_url()+endpoint

        headers={
            "X-Api-Key":api_key
        }
        p={
            "quantity":Quantity
        }
        response=requests.get(url=url, params=p, headers=headers )
        
        if response.status_code == 200:
            return response.json()

        return response.status_code
    
    def is_valid(self, api_key: str, telephone: str, CountryCode: str) -> bool:
        '''get bulk imei

        Args:
            api_key (str): api key
            telephone (str): phone number
            CountryCode (str): CountryCode ex: 'uz'

        Returns:
            bool: is valid
        '''
        endpoint="Phone/Validata"

        url=self.get_url()+endpoint

        headers={
            "X-Api-Key":api_key
        }
        p={
            "telephone":telephone,
            "CountryCode":CountryCode
        }
        response=requests.get(url=url, params=p, headers=headers )
        
        if response.status_code == 200:
            return response.json()

        return response.status_code
    
    def get_countries(self, api_key: str) -> list:
        '''get countries

        Args:
            api_key (str): api key

        Returns:
            list: lsit of countries
        '''
        endpoint="Phone/Countries"

        url = self.get_url() + endpoint

        headers = {
            "X-Api-Key": api_key
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()

        return response.status_code
token="d5939e334d6743fcb137acc1f32eae08"
phone = Phone()
# print(phone.generate(token, "LI", 7))
# print(phone.get_IMEI(token, 3))
# print(phone.is_valid(token, "+998990235051", "LI" ))
print(phone.get_countries(token))