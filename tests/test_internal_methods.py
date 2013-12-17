import unittest
from example import EXAMPLE_SPREADSHEET
from models import Spreadsheet


class TestInternalMethods(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_rows_columns(self):
        """
        row here is 1 because we want the list index
        """
        self.spreadsheet = Spreadsheet()
        row, column = self.spreadsheet._get_row_column("A2")
        self.assertEqual(column, "A")
        self.assertEqual(row, 1)

    def test_keys(self):
        self.spreadsheet = Spreadsheet()
        keys = self.spreadsheet._keys
        self.assertEqual(keys, ["A", "B", "C", "D", "E", "F", "G", "H"])

    def test_get_raw_value(self):
        self.spreadsheet = Spreadsheet(initial_data=EXAMPLE_SPREADSHEET)
        self.spreadsheet["F1"] = "=SUM(A2:C4)"
        self.assertEqual(self.spreadsheet._get_raw_value("F1").value, "=SUM(A2:C4)")
