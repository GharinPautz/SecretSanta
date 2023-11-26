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
