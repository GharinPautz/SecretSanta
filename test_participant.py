import unittest
from Participant import Participant


class Test_Participant(unittest.TestCase):

    def test_init(self):
        participant1 = Participant("Ghar")
        self.assertEqual(participant1.name, "Ghar")
        self.assertIsNone(participant1.assigned_person)

    def test_set_assigned_person(self):
        participant1 = Participant("Ghar")
        participant2 = Participant("Nick")
        participant1.set_assigned_person(participant2)
        self.assertEqual(participant1.assigned_person, participant2)

    def test_get_assigned_person(self):
        participant1 = Participant("Ghar")
        participant2 = Participant("Nick")
        participant1.set_assigned_person(participant2)
        self.assertEqual(participant1.get_assigned_person(), participant2.name)

    def test_set_name(self):
        participant1 = Participant("Ghar")
        participant1.set_name("Nick")
        self.assertEqual(participant1.get_name(), "Nick")

    def test_get_name(self):
        participant1 = Participant("Ghar")
        self.assertEqual(participant1.get_name(), "Ghar")


if __name__ == "__main__":
    unittest.main()
