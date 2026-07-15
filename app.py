import os
import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Път до файла, където ще се пазят съобщенията на сървъра
MESSAGES_FILE = 'messages.json'


def load_messages():
    if not os.path.exists(MESSAGES_FILE):
        return []
    try:
        with open(MESSAGES_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []


def save_message(name, email, text):
    messages = load_messages()
    messages.append({
        "name": name,
        "email": email,
        "message": text
    })
    with open(MESSAGES_FILE, 'w', encoding='utf-8') as f:
        json.dump(messages, f, ensure_ascii=False, indent=4)


@app.route('/')
def home():
    car_data = {
        "title": "The Mercedes-Benz C-Class",
        "subtitle": "A baby S-Class in every measurable way.",
        "about_title": "A New Standard, Cast in Silver",
        "description": "Unveiled at the 2014 North American International Auto Show...",
        "specs": [
            {"label": "Engine Options", "value": "1.6L – 4.0L"},
            {"label": "Horsepower", "value": "156 – 510 hp"},
            {"label": "Transmission", "value": "7G-TRONIC PLUS"},
            {"label": "Fuel Economy", "value": "4.0 L / 100km"}
        ]
    }
    return render_template('index.html', data=car_data)


@app.route('/auth')
def auth():
    return render_template('auth.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


# ОБНОВЕНО: Вече записва съобщенията в JSON файл на сървъра
@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message_text = request.form.get('message')

    save_message(name, email, message_text)
    return f"Thank you, {name}! Your message has been sent. Admin will see it."


# НОВО API: Връща съобщенията от JSON файла към Админ Таблото
@app.route('/api/messages')
def get_messages():
    return jsonify(load_messages())


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
