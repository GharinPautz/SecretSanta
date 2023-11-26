
class Participant:

    def __init__(self, name, assigned_person=None):
        self.name = name
        self.assigned_person = assigned_person

    def assign_person(self, person):
        self.assigned_person = person

    def get_assigned_person(self):
        return self.assigned_person.name

    def __str__(self):
        return self.name + " is assigned " + self.assign_person.name
