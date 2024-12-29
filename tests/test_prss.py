import unittest
from prss import PrSS

class TestPrSS(unittest.TestCase):
    def test_init_valid(self):
        # Test valid PrSS initialization
        valid_sequences = [
            [], [0], [0, 1], [0, 1, 1], [0, 1, 2, 3, 4, 5]
        ]
        for seq in valid_sequences:
            prss = PrSS(seq)
            self.assertEqual(prss.sequence, seq)

    def test_init_invalid_type(self):
        # Test invalid type for initialization
        with self.assertRaises(TypeError):
            PrSS(123)
        with self.assertRaises(TypeError):
            PrSS(["a", "b", "c"])

    def test_init_invalid_value(self):
        # Test invalid value for initialization
        invalid_sequences = [
            [1], [0, 2], [0, 1, 3]
        ]
        for seq in invalid_sequences:
            with self.assertRaises(ValueError):
                PrSS(seq)

    def test_str(self):
        # Test string representation
        prss = PrSS([0, 1, 2])
        self.assertEqual("(0)(1)(2)", str(prss))

    def test_eval(self):
        # Test evaluation method
        prss = PrSS([0, 1, 2, 3])
        self.assertEqual([0, 1, 2, 2, 2, 2], prss.eval().sequence)

        prss = PrSS([0, 1])
        self.assertEqual([0, 0, 0, 0], prss.eval().sequence)

    def test_eval_empty_sequence(self):
        # Test evaluation with empty sequence
        prss = PrSS([])
        with self.assertRaises(ValueError):
            prss.eval()

# Run the tests
if __name__ == '__main__':
    unittest.main()
