import unittest
from Participant import Participant
from Secret_Santa import Secret_Santa


class Test_Assign_Gifter(unittest.TestCase):

    work_participants = [
        "Ari",
        "Lizzo",
        "Troye",
        "Abel",
        "Jesse",
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


if __name__ == "__main__":
    unittest.main()
