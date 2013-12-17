from cells import FormulaeCell, IntCell, Cell


class Spreadsheet(object):
    """
    The representation of a spreadsheet object. You can get the values for each
    cell by doing:
    $ spread = Spreadsheet()
    $ spread["A2"]
    ""

    To get a list of values from a RANGE of cells do:
    $ spread["A2":"A5"]
    ["", "", "", ""]
    """

    # internal representation of the Spreadsheet
    _sheet = {}

    def __init__(self, initial_data=None):
        # if initial_data was provided populate spreadsheet with it instead
        # of generating one
        if initial_data is not None:
            self._sheet = initial_data
        else:
            self._sheet = {
                'A': [Cell()] * 10, 'B': [Cell()] * 10, 'C': [Cell()] * 10,
                'D': [Cell()] * 10, 'E': [Cell()] * 10, 'F': [Cell()] * 10,
                'G': [Cell()] * 10, 'H': [Cell()] * 10,
            }

    def __getitem__(self, key):
        # overriding this method allows us to do things like spreadsheet["A4"]
        if isinstance(key, slice):
            # key is a slice operator, return list of values in slice
            if key.step is not None:
                # we don't allow slices like spread["A2":"A4":"A9"]
                raise Exception("Step in slice operator is not allowed")
            row_start, column_start = self._get_row_column(key.start)
            row_end, column_end = self._get_row_column(key.stop)
            if row_start is None or row_end is None:
                # if slice was done without a row specified (ex: spread["A"])
                # don't allow it
                raise Exception("To slice you must specify a start cell and "
                                "end cell. Full columns are not allowed.")

            index_of_start = self._keys.index(column_start)
            index_of_end = self._keys.index(column_end)
            columns = self._keys[index_of_start:index_of_end + 1]
            values = []
            for column in columns:
                values.extend(self._sheet[column][row_start:row_end + 1])
            return values

        row, column = self._get_row_column(key)
        if row is not None:
            return self._sheet[column][row]._get_value()

        return self._sheet[column]

    def __setitem__(self, key, value):
        row, column = self._get_row_column(key)
        if isinstance(value, str) and value.startswith("="):
            # this is a formulae
            cell = FormulaeCell(value, self)
        elif isinstance(value, int) or isinstance(value, float):
            cell = IntCell(value)
        else:
            cell = Cell()

        if row is None:
            # if you are assigning a column this will make the whole column
            # have the same value
            self._sheet[key] = [cell] * 10
        else:
            self._sheet[column][row] = cell

    def _get_row_column(self, key):
        if len(key) > 2:
            raise Exception("Key can only be of length 2 (ex: 'A2')")
        column = key[0]
        try:
            row = int(key[1]) - 1
        except IndexError:
            row = None

        return row, column

    def _get_raw_value(self, key):
        """
        Return the raw value of a cell
        """
        row, column = self._get_row_column(key)
        if row is None:
            raise Exception("This function only accepts a cell, not a whole row")
        return self._sheet[column][row]

    @property
    def _keys(self):
        """
        Get keys sorted alphabetically
        """
        return sorted(self._sheet.keys())

    def _get_clean_values(self, start, end):
        """
        remove from list the values that are 0 and empty list
        """
        def remove_value(value):
            if value == "":
                return False
            return True
        return filter(remove_value, self[start:end])

    def sum(self, start, end):
        values = self._get_clean_values(start, end)
        return sum(values)
