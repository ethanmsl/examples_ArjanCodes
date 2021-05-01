import unittest
from hand import *
from rules import *

class DieTestCase(unittest.TestCase):

    def test_sides_per_die(self):
        die = Die(None, 1)
        for _ in range(50):
            self.assertEqual(die.roll(), 1)

    def test_set_face(self):
        die = Die(3)
        self.assertEqual(die.get_face(), 3)

    def test_to_string(self):
        die = Die()
        self.assertEqual(str(die.get_face()), str(die))


class HandTestCase(unittest.TestCase):

    def test_hand_number_of_dice(self):
        hand = Hand(15, 6)
        self.assertEqual(len(hand.hand), 15)

    def test_hand_sides_per_die(self):
        hand = Hand(5, 18)
        for i in hand.hand:
            self.assertEqual(i.sides, 18)


class RulesTestCase(unittest.TestCase):

    def test_aces(self):
        hand = Hand()
        hand.set_faces([1] * 5)
        self.assertEqual(Aces().points(hand), 5)

    def test_three_of_a_kind(self):
        hand = Hand()
        hand.set_faces([1, 1, 1, 2, 2])
        self.assertEqual(ThreeOfAKind().points(hand), 7)

    def test_four_of_a_kind(self):
        hand = Hand()
        for i in range(4):
            hand.hand[i]._Die__face = 1
        for i in range(4, 5):
            hand.hand[i]._Die__face = 2
        self.assertEqual(FourOfAKind().points(hand), 6)

    def test_full_house(self):
        hand = Hand()
        for i in range(1):
            hand.hand[i]._Die__face = 2
        for i in range(1, 3):
            hand.hand[i]._Die__face = 2
        for i in range(3, 5):
            hand.hand[i]._Die__face = 3
        self.assertEqual(FullHouse().points(hand), 25)

    def test_no_full_house(self):
        hand = Hand()
        for i in range(1):
            hand.hand[i]._Die__face = 2
        for i in range(1, 3):
            hand.hand[i]._Die__face = 4
        for i in range(3, 5):
            hand.hand[i]._Die__face = 3
        self.assertEqual(FullHouse().points(hand), 0)

    def test_small_straight(self):
        hand = Hand()
        hand.hand[0]._Die__face = 4
        hand.hand[1]._Die__face = 3
        hand.hand[2]._Die__face = 5
        hand.hand[3]._Die__face = 2
        hand.hand[4]._Die__face = 5
        self.assertEqual(SmallStraight().points(hand), 30)

    def test_large_straight(self):
        hand = Hand()
        hand.hand[0]._Die__face = 4
        hand.hand[1]._Die__face = 3
        hand.hand[2]._Die__face = 5
        hand.hand[3]._Die__face = 2
        hand.hand[4]._Die__face = 1
        self.assertEqual(LargeStraight().points(hand), 40)

    def test_yahtzee(self):
        hand = Hand()
        for i in hand.hand:
            i._Die__face = 3
        self.assertEqual(Yahtzee().points(hand), 50)

    def test_chance(self):
        hand = Hand()
        for i in range(5):
            hand.hand[i]._Die__face = i + 1
        self.assertEqual(Chance().points(hand), 15)


if __name__ == '__main__':
    unittest.main()