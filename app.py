from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "2fbec50a752beb464da6742c108055d2"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")

        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            weather = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"]
            }
        else:
            error = "City not found."

    return render_template("index.html", weather=weather, error=error)

if __name__ == "__main__":
    app.run(debug=True)