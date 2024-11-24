from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = 'https://api.api-ninjas.com/v1/quotes'
API_KEY = 's4XrM+kxghOq/wyhcI2/AA==WUEOXpfaGbQcxWdV'  # Замените на ваш ключ API

# Предопределенные категории (можете расширить список в соответствии с документацией API)
CATEGORIES = [
    'happiness', 'inspirational', 'life', 'love', 'success', 'wisdom', 'age', 'alone', 'art', 'car', 'business'
]

def get_quote(category):
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(f"{API_URL}?category={category}", headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]  # Берем первую цитату из ответа
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    selected_category = None
    quote = None
    if request.method == 'POST':
        selected_category = request.form.get('category')
        quote = get_quote(selected_category)
    return render_template('index.html', categories=CATEGORIES, selected_category=selected_category, quote=quote)

if __name__ == '__main__':
    app.run(debug=True)
