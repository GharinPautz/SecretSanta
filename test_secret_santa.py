import unittest
from Participant import Participant
from Secret_Santa import Secret_Santa


class Test_Assign_Gifter(unittest.TestCase):

    work_participants = [
        "Ari",
        "Lizzo",
        "Troye",
        "Abel",
        "Jessie",
        "Shawn",
        "Justin",
        "Harry",
        "Nicki",
        "Taylor",
        "Beyonce",
        "Gracie",
        "Olivia",
        "Kim"
    ]

    def test_init(self):
        participants = []
        for participant in self.work_participants:
            participants.append(Participant(participant))

        secret_santa = Secret_Santa(participants)

        for i in range(0, len(self.work_participants)):
            self.assertEqual(
                self.work_participants[i], secret_santa.participants[i].name)

        self.assertEqual(secret_santa.assignments, {})

    def test_assign_gifts(self):
        participants = []
        for participant in self.work_participants:
            participants.append(Participant(participant))

        secret_santa = Secret_Santa(participants)
        secret_santa.assign_gifts()

        gifters, receivers = [], []
        for gifter, receiver in secret_santa.assignments.items():
            # Check that no participant is assigned to themself
            self.assertNotEqual(gifter.name, receiver.name)
            gifters.append(gifter)
            receivers.append(receiver)

        # Check that all participants are included as gifters
        self.assertEqual(set(gifters), set(participants))

        # Check that all participants are included as receivers
        self.assertEqual(set(receivers), set(participants))

    def test_get_num_participants(self):
        participant1 = Participant("Nicki")
        particpant2 = Participant("Taylor")
        participant3 = Participant("Brandon")

        participants = [participant1, particpant2, participant3]
        secret_santa = Secret_Santa(participants)

        self.assertEqual(secret_santa.get_num_participants(), 3)

    def test_add_participant(self):
        participant1 = Participant("Nicki")
        particpant2 = Participant("Taylor")
        participant3 = Participant("Brandon")

        participants = [participant1, particpant2, participant3]
        secret_santa = Secret_Santa(participants)

        participant4 = Participant("Justin")
        secret_santa.add_participant(participant4)

        self.assertEqual(secret_santa.get_num_participants(), 4)

    def test_remove_participant(self):
        participant1 = Participant("Nicki")
        particpant2 = Participant("Taylor")
        participant3 = Participant("Brandon")

        participants = [participant1, particpant2, participant3]
        secret_santa = Secret_Santa(participants)

        self.assertEqual(secret_santa.get_num_participants(), 3)

        self.assertEqual(secret_santa.participants[-1].name, "Brandon")

        secret_santa.remove_participant(participant3)
        self.assertEqual(secret_santa.get_num_participants(), 2)

        self.assertNotEqual(secret_santa.participants[-1].name, "Brandon")

    def test_set_participants(self):
        participant1 = Participant("Nicki")
        particpant2 = Participant("Taylor")
        participant3 = Participant("Brandon")

        participants = [participant1, particpant2, participant3]
        secret_santa = Secret_Santa(participants)

        new_participants = []
        for participant in self.work_participants:
            new_participants.append(Participant(participant))

        secret_santa.set_participants(new_participants)

        self.assertEqual(secret_santa.get_num_participants(), 14)
        self.assertEqual(secret_santa.get_participants()[-1].get_name(), "Kim")

    def test_get_participant(self):
        participant1 = Participant("Nicki")
        particpant2 = Participant("Taylor")
        participant3 = Participant("Brandon")

        participants = [participant1, particpant2, participant3]
        secret_santa = Secret_Santa(participants)

        self.assertEqual(secret_santa.get_participants()
                         [-1].get_name(), "Brandon")


if __name__ == "__main__":
    unittest.main()
