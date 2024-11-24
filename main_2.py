from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', method=['GET', 'POST'])
def index():
    quotes = None
    if request.method == 'POST':
        city = request.form['city']
        quotes = get_random_quotes(quotes)
    return render_template("index.html", quotes=quotes )

def get_random_quotes(quote):
    api_key = "s4XrM+kxghOq/wyhcI2/AA==WUEOXpfaGbQcxWdV"
    url = f"https://api.api-ninjas.com/v1/quotes?category=happiness"
    response = requests.get(url)
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)