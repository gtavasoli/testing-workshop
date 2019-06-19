from get_next_person import get_next_person
import unittest


class TestNewPerson(unittest.TestCase):
    def test_new_person(self):
        # arrange
        user = {'people_seen': []}
        expected_person = 'Ali'

        # action
        actual_person = get_next_person(user)

        # assert
        self.assertEqual(actual_person, expected_person)


if __name__ == '__main__':
    unittest.main()
