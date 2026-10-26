"""
Unit Tests for Grade Calculator (9 Tests covering all bug areas)
"""
import unittest
from grade_calculator import calculate_average, is_passing, assign_grade

class TestGradeCalculator(unittest.TestCase):
    # 1-3: Average calculation tests
    def test_average_regular(self):
        self.assertEqual(calculate_average([80, 90, 100]), 90.0)

    def test_average_float_precision(self):
        self.assertAlmostEqual(calculate_average([85, 90, 92]), 89.0, places=1)

    def test_average_empty_list(self):
        self.assertEqual(calculate_average([]), 0.0)

    # 4-6: Passing boundary tests
    def test_passing_exact_boundary(self):
        # Passing boundary bug fixed: score of 40 must pass
        self.assertTrue(is_passing(40))

    def test_passing_above_boundary(self):
        self.assertTrue(is_passing(75))

    def test_failing_below_boundary(self):
        self.assertFalse(is_passing(39))

    # 7-9: Grade ordering tests
    def test_grade_a(self):
        self.assertEqual(assign_grade(95), "A")

    def test_grade_b(self):
        # Grade ordering bug fixed: 85 must return B, not pass down
        self.assertEqual(assign_grade(85), "B")

    def test_grade_f(self):
        self.assertEqual(assign_grade(52), "F")

if __name__ == "__main__":
    unittest.main()
