import unittest
from cells import IntCell, Cell
from models import Spreadsheet


class TestSpreadsheet(unittest.TestCase):
    def setUp(self):
        pass

    #### test class initialization
    def test_initialize_with_data(self):
        self.spreadsheet = Spreadsheet(initial_data={'A': []})
        self.assertEqual(self.spreadsheet._sheet, {'A': []})

    #### test getter, setter and slice
    def test_get_row(self):
        self.spreadsheet = Spreadsheet()
        row = self.spreadsheet["A"]
        self.assertEqual(len(row), 10)

    def test_get_value(self):
        self.spreadsheet = Spreadsheet()
        self.spreadsheet["A1"] = 2
        self.spreadsheet["A2"] = 3
        self.spreadsheet["A3"] = "=SUM(A1:A2)"
        # the cell A3 resolves to 5 and sums to itself, return 10 as the final
        # result
        self.assertEqual(self.spreadsheet.sum("A1", "A3"), 10)

    def test_set_row(self):
        self.spreadsheet = Spreadsheet()
        self.spreadsheet["A"] = 10
        row = self.spreadsheet["A"]
        self.assertEqual(len(row), 10)

    def test_access(self):
        self.spreadsheet = Spreadsheet()
        self.assertEqual(self.spreadsheet["A2"], "")

    def test_access_data(self):
        self.spreadsheet = Spreadsheet()
        self.spreadsheet["A2"] = 3
        self.assertEqual(self.spreadsheet["A2"], 3)

    def test_slice(self):
        self.spreadsheet = Spreadsheet()
        values = self.spreadsheet["A2":"B3"]
        self.assertEqual(len(values), 4)

    #### test exceptions
    def test_slice_exception(self):
        self.spreadsheet = Spreadsheet()
        # make sure that when we use the step operator an exception is raised
        self.assertRaises(
            Exception, self.spreadsheet.__getitem__, slice("A2", "A4", 2)
        )

    def test_slice_exception2(self):
        self.spreadsheet = Spreadsheet()
        # make sure that when we use the step operator an exception is raised
        self.assertRaises(
            Exception, self.spreadsheet.__getitem__, slice("A", "A4")
        )

if __name__ == '__main__':
    unittest.main()
