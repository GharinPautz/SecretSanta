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


@app.route('/assign-gifts', methods=['POST'])
def assign_gifts():
    secret_santa.assign_gifts()
    return jsonify({"message": "Gifts assigned successfully"}), 201


@app.route('/get-participant', methods=['GET'])
def get_participant():
    # Get the name parameter from the URL query
    name = request.args.get('name')
    if not name:
        return jsonify({"error": "Name parameter is missing"}), 400

    # Find the participant in the Secret Santa instance
    participant = next(
        (p for p in secret_santa.get_participants() if p.get_name() == name), None)
    if not participant:
        return jsonify({"error": "Participant not found"}), 404

    assigned_person = participant.get_assigned_person()
    if assigned_person:
        return jsonify({"assignedTo": assigned_person})
    else:
        return jsonify({"message": "Gift assignment not done yet"})


@app.route('/remove-participant', methods=['DELETE'])
def remove_participant():
    name = request.args.get('name')
    if not name:
        return jsonify({"error": "Name parameter is missing"}), 400

    # Find the participant in the Secret Santa instance
    participant = next(
        (p for p in secret_santa.get_participants() if p.get_name() == name), None)
    if not participant:
        return jsonify({"error": "Participant not found"}), 404

    secret_santa.remove_participant(participant)
    return jsonify({"message": "Participant removed"}), 200


if __name__ == '__main__':
    app.run(debug=True)
