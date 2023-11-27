class Participant:
    """
    Represents a participant in a Secret Santa activity.

    Attributes
    ----------
    name : str
        The name of the participant.
    assigned_person : Participant
        The participant to whom this participant is assigned to give a gift.

    Methods
    -------
    set_assigned_person(person):
        Assign a participant to whom this participant will give a gift.

    get_assigned_person():
        Return the name of the assigned participant.

    __str__():
        Return a string representation of the participant.

    get_name():
        Return the name of the participant.

    set_name(name):
        Set the name of the participant.
    """

    def __init__(self, name, assigned_person=None):
        """
        Constructs all the necessary attributes for the participant object.

        Parameters
        ----------
        name : str
            The name of the participant.
        assigned_person : Participant, optional
            The participant to whom this participant is assigned to give a gift (default is None).
        """
        self.name = name
        self.assigned_person = assigned_person

    def set_assigned_person(self, person):
        """
        Sets the assigned person for this participant.

        Parameters
        ----------
        person : Participant
            The participant to whom this participant is assigned to give a gift.
        """
        self.assigned_person = person

    def get_assigned_person(self):
        """
        Returns the name of the participant to whom this participant is assigned.

        Returns
        -------
        str
            The name of the assigned participant.
        """
        return self.assigned_person.name

    def __str__(self):
        """
        String representation of the Participant object.

        Returns
        -------
        str
            A string stating who the participant is assigned to.
        """
        return self.name + " is assigned " + self.assigned_person.name

    def get_name(self):
        """
        Returns the name of the participant.

        Returns
        -------
        str
            The name of the participant.
        """
        return self.name

    def set_name(self, name):
        """
        Sets the name of the participant.

        Parameters
        ----------
        name : str
            The new name of the participant.
        """
        self.name = name
