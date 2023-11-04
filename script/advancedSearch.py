from flask import Flask,request,jsonify
import requests
from requests import get
from json import loads

app = Flask(__name__)

@app.route('/', methods=['GET'])
def search_api(card_name):
    
    api_prefix = "https://api.scryfall.com/cards/search?unique=prints&q="

    api_url = api_prefix + card_name

    card_list = []

    while True:
        paging_list = loads(get(api_url).text)

        for card in paging_list['data']:
            card_data = {
                'name': card['name'],
                'set': card['set_name'],
                'num': card['collector_number'],
                'price': card['prices']['usd']
            }

            card_list.append(card_data)

        if not paging_list['has_more']:
            break

        api_url = paging_list['next_page']
    return card_list

if __name__ == '__main__':
    app.run()



