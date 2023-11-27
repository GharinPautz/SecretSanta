import random


class Secret_Santa:
    """
    A class to manage the Secret Santa gift exchange process.

    Attributes
    ----------
    participants : list of Participant
        A list of participants in the Secret Santa exchange.
    assignments : dict
        A dictionary mapping each participant to the person they are gifting to.

    Methods
    -------
    assign_gifts():
        Randomly assigns participants to each other for gifting.

    __str__():
        Returns a string representation of the gift assignments.

    add_participant(participant):
        Adds a new participant to the Secret Santa exchange.

    remove_participant(participant):
        Removes a participant from the Secret Santa exchange.

    get_num_participants():
        Returns the number of participants in the Secret Santa exchange.

    set_participants(participants):
        Sets the list of participants for the Secret Santa exchange.

    get_participants():
        Returns the list of participants in the Secret Santa exchange.
    """

    def __init__(self, participants):
        """
        Initializes the Secret Santa with a list of participants.

        Parameters
        ----------
        participants : list of Participant
            A list of Participant objects participating in the Secret Santa.
        """
        self.participants = participants
        self.assignments = {}

    def assign_gifts(self):
        """
        Randomly assigns each participant a person to whom they will give a gift.
        Ensures no participant is assigned to themselves.
        """
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
        """
        String representation of the Secret Santa assignments.

        Returns
        -------
        str
            A string representation of each participant and their assigned giftee.
        """
        if self.assignments is {}:
            return "{}"

        assignment_str = ""

        for gifter, receiver in self.assignments.items():
            assignment_str += gifter.name + " -> " + receiver.name + "\n"

        return assignment_str

    def add_participant(self, participant):
        """
        Adds a new participant to the Secret Santa exchange.

        Parameters
        ----------
        participant : Participant
            The participant to be added to the exchange.
        """
        self.participants.append(participant)

    def remove_participant(self, participant):
        """
        Removes a participant from the Secret Santa exchange.

        Parameters
        ----------
        participant : Participant
            The participant to be removed from the exchange.
        """
        updated_participants = []

        for p in self.participants:
            if p is not participant:
                updated_participants.append(p)

        self.participants = updated_participants

    def get_num_participants(self):
        """
        Returns the number of participants in the Secret Santa exchange.

        Returns
        -------
        int
            The number of participants in the exchange.
        """
        return len(self.participants)

    def set_participants(self, participants):
        """
        Sets the list of participants for the Secret Santa exchange.

        Parameters
        ----------
        participants : list of Participant
            The new list of participants for the exchange.
        """
        self.participants = participants

    def get_participants(self):
        """
        Returns the list of participants in the Secret Santa exchange.

        Returns
        -------
        list of Participant
            The list of participants in the exchange.
        """
        return self.participants
