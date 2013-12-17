import unittest
from example import EXAMPLE_SPREADSHEET
from models import Spreadsheet


class TestFormulae(unittest.TestCase):
    def setUp(self):
        pass

    def test_sum_formulae(self):
        self.spreadsheet = Spreadsheet(initial_data=EXAMPLE_SPREADSHEET)
        self.spreadsheet["F1"] = "=SUM(A2:C4)"
        self.assertEqual(self.spreadsheet["F1"], 91.88000000000001)

    def test_count_formulae(self):
        self.spreadsheet = Spreadsheet(initial_data=EXAMPLE_SPREADSHEET)
        self.spreadsheet["F1"] = "=COUNT(A2:C4)"
        self.assertEqual(self.spreadsheet["F1"], 8)

    def test_max_formulae(self):
        self.spreadsheet = Spreadsheet(initial_data=EXAMPLE_SPREADSHEET)
        self.spreadsheet["F1"] = "=MAX(A2:C4)"
        self.assertEqual(self.spreadsheet["F1"], 25.02)

    def test_min_formulae(self):
        self.spreadsheet = Spreadsheet(initial_data=EXAMPLE_SPREADSHEET)
        self.spreadsheet["F1"] = "=MIN(A2:C4)"
        self.assertEqual(self.spreadsheet["F1"], 3.15)