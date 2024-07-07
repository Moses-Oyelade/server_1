from flask import Flask, request, jsonify
import requests
app = Flask(__name__)

@app.route('/api/hello', methods=["GET"])
def api_hello():
    query = request.args.get("visitor_name")
    name = query.capitalize()
    client_ip = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    
    url = f"https://ipgeolocation.abstractapi.com/v1/?api_key=5d893befd2304f53ba4809dffc95722e"
    
    response = requests.get(url)
    data = response.json()
    city = data["city"]
    
    api = f'https://api.weatherapi.com/v1/current.json?q={city}&key=50ee3c76dab44094a7b145241240507'
    responseb = requests.get(api)
    data2 = responseb.json()
    temp = data2["current"]["temp_c"]   
    
    result = {}
    result["client_ip"] = client_ip
    result["location"] = city
    result["greeting"] = f"Hello, {name}!, the temperature is {temp} degrees Celcius in {city}."
    print(result)
    return (result)

if __name__ == '__main__':
    app.run(debug=True)