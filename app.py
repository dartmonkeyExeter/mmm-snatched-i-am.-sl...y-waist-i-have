from flask import Flask, render_template, jsonify, url_for, redirect
import requests, random

def get_number_of_people():
    total_people = 0

    next_url = 'https://swapi.dev/api/people/?page=1'

    name_yodaheight = {}

    while True:
        try:
            response = requests.get(next_url)
        except:
            break

        total_people = response.json()['count']
        for person in response.json()['results']:
            try:
                print(person['name'], person['height'])
                name_yodaheight[person['name']] = round(int(person['height']) / 66.0, 2)
                
            except ValueError:
                pass
        next_url = response.json()['next']

    return name_yodaheight

name_yodaheight = get_number_of_people()

app = Flask(__name__)

@app.route('/character/<int:id>')
def character(id):
    char_name = list(name_yodaheight.items())[id][0]
    yoda_meters = int(str(name_yodaheight[char_name]).split(".")[0])
    yoda_centis = int(str(name_yodaheight[char_name]).split(".")[1])
    return render_template('index.html', char_name=char_name, yoda_meters=yoda_meters, yoda_centis=yoda_centis)

@app.route('/')
def index():
    return redirect(url_for('character', id=random.randint(0, len(name_yodaheight) - 1)))

if __name__ == '__main__':
    app.run(debug=True)