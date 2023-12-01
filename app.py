from flask import Flask, jsonify, request
from Participant import Participant
from Secret_Santa import Secret_Santa

app = Flask(__name__)
secret_santa = Secret_Santa([])


@app.route('/')
def index():
    return "Welcome to the Secret Santa API!"


@app.route('/add-participant', methods=['POST'])
def add_participant():
    data = request.json
    new_participant = Participant(data['name'])
    secret_santa.add_participant(new_participant)
    return jsonify({"message": "Participant added", "participant": data['name']}), 201


@app.route('/participants', methods=['GET'])
def get_participants():
    participants = secret_santa.get_participants()
    participants_data = [{'name': participant.get_name()}
                         for participant in participants]
    return jsonify(participants_data), 200


if __name__ == '__main__':
    app.run(debug=True)
