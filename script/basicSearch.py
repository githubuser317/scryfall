from flask import Flask,request,jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def search_api():
    query = request.args.get('query')
    api_url = "https://api.scryfall.com/cards/search?q=tiger"
    response = requests.get(api_url)
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run()
