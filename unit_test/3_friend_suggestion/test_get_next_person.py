from get_next_person import get_next_person
from evaluate import evaluate
import unittest
from unittest.mock import patch


class TestNewPerson(unittest.TestCase):
    # def test_new_person(self):
    #     # arrange
    #     user = {'people_seen': []}
    #     expected_person = 'Ali'
    #
    #     # action
    #     actual_person = get_next_person(user)
    #
    #     # assert
    #     self.assertEqual(actual_person, expected_person)

    def test_evaluate(self):
        with patch('evaluate.let_down_gently') as mock_let_down:
            # arrange
            person1 = 'Ali'
            person2 = {
                'likes': ['Bita', 'Mohammad'],
                'dislike': ['Ali']
            }

            # action
            evaluate(person1, person2)

            # assert
            self.assertEqual(mock_let_down.call_count, 1)


if __name__ == '__main__':
    unittest.main()
