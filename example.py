from cells import IntCell, Cell
from models import Spreadsheet

EXAMPLE_SPREADSHEET = {
    'A': [
        IntCell(10.24), IntCell(9.19), IntCell(3.5), IntCell(25.02), Cell(),
        Cell(), IntCell(0.83), Cell(), Cell(), Cell()
    ],
    'B': [
        IntCell(13.00), IntCell(6.21), IntCell(18.92), IntCell(3.15), Cell(),
        Cell(), Cell(), Cell(), Cell(), Cell()
    ],
    'C': [
        Cell(), Cell(), IntCell(21.42), IntCell(4.47), IntCell(17.9), Cell(),
        IntCell(9.00), Cell(), Cell(), Cell()
    ],
    'D': [Cell()] * 10,
    'E': [Cell()] * 10,
    'F': [Cell()] * 10,
    'G': [Cell()] * 10,
    'H': [Cell()] * 10,
}

print "Creating spreadsheet with sample data as provided in the assessment test"
s = Spreadsheet(initial_data=EXAMPLE_SPREADSHEET)

print "Putting formulae '=SUM(A2:C4)' in cell F1"
s["F1"] = "=SUM(A2:C4)"

print "Cell F1 as the value", s["F1"]