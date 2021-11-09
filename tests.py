import unittest
from phase10 import evaluate_hand, get_largest_run

class TestPhase10(unittest.TestCase):
    def test_hand_duplicate_nums_in_run(self):
        self.assertEqual(evaluate_hand([1,1,1,1,1,2,2,2,3,4]), [1,2,3,9,10])
    
    def test_hand_multiple_run_set_combos(self):
        self.assertEqual(evaluate_hand([1,1,1,1,2,2,2,2,3,4]), [1,2,7])
        
    def test_hand_all_run_phases(self):
        self.assertEqual(evaluate_hand([3,4,5,6,1,7,8,9,10,11]), [4,5,6])
            
    def test_largest_run_comes_after_gap(self):
        self.assertEqual(get_largest_run([7,12,10,2,3,8,6,5,9,7]), [5,6,7,8,9,10])

    def test_largest_run_after_run_of_one(self):
        self.assertEqual(get_largest_run([1,3,4,5]), [3,4,5])

    def test_largest_run_after_two_gaps(self):
        self.assertEqual(get_largest_run([1,3,5,6,7,8,9,10,11,12]), [5,6,7,8,9,10,11,12])

        
if __name__ == "__main__":
    unittest.main()
    