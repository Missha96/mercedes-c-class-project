from flask import Flask, render_template, request

app = Flask(__name__)

# Дефиниране на данните за автомобила (заглавие, описание, спецификации, иновации)
@app.route('/')
def home():
    car_data = {
        "title": "The Mercedes-Benz C-Class",
        "subtitle": "A baby S-Class in every measurable way.",
        "about_title": "A New Standard, Cast in Silver",
        "description": "Unveiled at the 2014 North American International Auto Show and launched worldwide in 2015, the W205 represented Mercedes-Benz's most ambitious C-Class to date...",
        "specs": [
            {"label": "Engine Options", "value": "1.6L – 4.0L"},
            {"label": "Horsepower", "value": "156 – 510 hp"},
            {"label": "Transmission", "value": "7G-TRONIC PLUS"},
            {"label": "Fuel Economy", "value": "4.0 L / 100km"}
        ],
        "innovations": [
            {"id": "01", "title": "AGILITY SELECT", "desc": "Five drive modes reshape steering, throttle, and transmission character."},
            {"id": "02", "title": "S-Class Interior", "desc": "Cascading centre console, free-standing display, and open-pore woods."},
            {"id": "03", "title": "Lightweight Body", "desc": "Aluminium hybrid construction cuts nearly 100 kg."},
            {"id": "04", "title": "AIR BODY CONTROL", "desc": "Segment-first four-corner air suspension."}
        ]
    }
    return render_template('index.html', data=car_data)

# Обработка на контактната форма (POST заявка)
@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    return f"Thank you, {name}! Your message has been sent. We will contact you at {email}."

if __name__ == '__main__':
    app.run(debug=True)
