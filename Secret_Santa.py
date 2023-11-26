import random


class Secret_Santa:

    def __init__(self, participants, assignments=None):
        self.participants = participants
        self.assignments = assignments or {}

    def assign_gifts(self):
        shuffled_participants = self.participants[:]
        random.shuffle(shuffled_participants)

        num_participants = len(shuffled_participants)
        for i in range(num_participants):
            gifter = shuffled_participants[i]
            # Wrap around to the start
            receiver = shuffled_participants[(i + 1) % num_participants]
            self.assignments[gifter] = receiver
            gifter.set_assigned_person(receiver)

    def __str__(self):
        if self.assignments is None:
            return "{}"

        assignment_str = ""

        for gifter, receiver in self.assignments.items():
            assignment_str += gifter.name + " -> " + receiver.name + "\n"

        return assignment_str

    def add_participant(self, participant):
        self.participants.append(participant)

    def remove_participant(self, participant):
        updated_participants = []

        for p in self.participants:
            if p is not participant:
                updated_participants.append(p)

        self.participants = updated_participants

    def get_num_participants(self):
        return len(self.participants)
