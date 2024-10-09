from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

def get_number_of_people():
    total_people = 0

    next_url = 'https://swapi.dev/api/people/?page=1'

    name_yodaheight = {}

    while next_url != "null":
        response = requests.get(next_url)

        total_people = response.json()['count']
        for person in response.json()['results']:
            try:
                name_yodaheight[person['name']] = round(int(person['height']) / 66.0, 2)
            except ValueError:
                pass
        next_url = response.json()['next']
    return name_yodaheight

print(get_number_of_people())