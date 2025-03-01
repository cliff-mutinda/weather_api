from flask import *
import requests

app = Flask (__name__)

@app.route("/weather", methods=["GET"])
def weather():
    # the api is from www.weatherapi.com
    apikey = "823cff7b32e24417b25161600252702"
    base_url = "http://api.weatherapi.com/v1"

    city= request.args.get("city")
    
    url = f"{base_url}/current.json?key={apikey}&q={city}"
    result = requests.get(url)

    # return data
    return jsonify(result.json())

if __name__ == "__main__":
    app.run()
