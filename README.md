Spreadsheet
===========

Defining a new spreadsheet:

    $ from spreadsheet.models import Spreadsheet
    $ from spreadsheet.example import EXAMPLE_SPREADSHEET
    $ spread = Spreadsheet(initial_data=EXAMPLE_SPREADSHEET)

Setting example values:

    $ spread["F5"] = 45.8

Summing a range of cells:

    $ spread.sum("A2", "C4")
    91.88000000000001

If we want to use formulae:

    $ spread["F1"] = "=SUM(A2:C4)"
    $ spread["F1"]
    91.88000000000001

We can also get the raw value of `F1` by doing:

    $ spread._get_raw_value("F1")
    "=SUM(A2:C4)"

Running the tests
=================

To run the test just cd inside the spreadsheet folder:
    $ cd ~/spreadsheet/
    $ python -m unittest tests


Trying out the spreadsheet
==========================

To try out the spreadsheet run the following commands:
    $ cd ~/spreadsheet
    $ python -i example.py

Global overview of architecture solution
========================================

There are 3 main modules for this package:
 * models.py   - main module with the Spreadsheet class definition
 * cells.py    - cell objects defining the different type of cells
 * formulae.py - simple classes created to delegate calculation

With this approach the Spreadsheet class is simpler and focuses on its own
attributes delegating any calculation or logic to the cells implementation.
