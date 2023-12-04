from settings import URL,API_KEY
from randomers import card,finance,misc,name,phone,social_number,texts
from send_message import send_message
from random import choice
from randomers import card
from time import sleep
import requests

def get_updates():
    endpoint="/getUpdates"
    url=URL+endpoint
    response=requests.get(url)
    if response.status_code==200:
        return response.json()["result"]
    return response.status_code

def main(url: str):
    last_update_id = -1
    
    while True:
        updates = get_updates()
        last_update =updates[-1]
        if last_update['update_id'] != last_update_id:
            user = last_update['message']['from']['id']
            text = last_update['message']['text']

            if text == '/start':
                send_message(url, user, """        Hello and welcome to Randommer Bot!

        🎉 Get ready for a diverse range of randomness with our exciting features. Here's a quick guide on how to use this bot:

        1. /start: Use this command to receive a warm welcome message and get instructions on how to interact with the bot.

        2. /card: Feeling lucky? Use this command to draw a random card and see what fortune it holds for you.

        3. /finance: Looking for some crypto randomness? Type this command to get a random crypto address.

        4. /misc: Explore the richness of various cultures! Use this command to receive information on 5 randomly selected cultures.

        5. /name: Need a name on the spot? Type this command for a completely random full name.

        6. /phone: If you're in need of phone numbers, use this command to get 5 randomly generated Uzbekistan phone numbers.

        7. /social_number: Curious about social numbers? Use this command to get a randomly generated social number.

        8. /text: Want some Lorem Ipsum text? Type this command to receive 20 words of normal Lorem Ipsum text.

        9. /busywork: Need something to keep yourself occupied? Use this command for advice on productive and engaging tasks.""")

            elif text == '/card':
                a=card.Card()
                cards=a.get_card(API_KEY)
                send_message(url, user,cards)

            elif text == '/finance':
                a=finance.Finance()
                finance1 = a.get_crypto_address_types(API_KEY)
                send_message(url, user, choice(finance1))

            elif text == "/misc":
                a=misc.Misc()
                misc1=choice([i["code"] for i in a.get_cultures(API_KEY)])
                misc2=a.get_random_address(API_KEY, 5, misc1)
                send_message(url, user, "\n".join(misc2))

            elif text == "/name":
                a = name.Name()
                name1=a.get_name(API_KEY, "fullname", 1)
                send_message(url, user, name1)
        
            elif text == "/phone":
                a=phone.Phone()
                phone1=a.generate(API_KEY, "uz", 5)

                send_message(url, user, "\n".join(phone1))

            elif text == "/social_number":
                a=social_number.SocialNumber()
                number1=a.get_SocialNumber(API_KEY)
                send_message(url, user["id"], number1)
            
            elif text == "/text":
                a= texts.Text()
                text_1 = a.generate_LoremIpsum(API_KEY, "normal", "words", 20)
                send_message(url, user, text_1)
            else:
                send_message(url, user, "Error massage")

        last_update_id = last_update['update_id']

        sleep(0.5)

main(URL)