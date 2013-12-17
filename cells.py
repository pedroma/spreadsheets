import re
import formulaes
from settings import FORMULAE_REGEX


class Cell(object):

    def __init__(self, value=""):
        self.value = value

    def _get_int_value(self):
        return 0

    def _get_value(self):
        return self.value

    def __add__(self, other):
        return self._get_int_value() + other

    def __radd__(self, other):
        return other + self._get_int_value()


class FormulaeCell(Cell):
    """
    Formulae Cells needs a reference to the spreadsheet so it can
    calculate its value
    """
    def __init__(self, value, spreadsheet):
        super(FormulaeCell, self).__init__(value=value)
        self._sheet = spreadsheet
        self._set_formulae_name_and_range()
        self.formulae = getattr(formulaes, self.function, None)()

    def _set_formulae_name_and_range(self):
        regex = re.compile(FORMULAE_REGEX)
        matches = regex.match(self.value)
        if matches is None:
            raise Exception("Invalid formulae {0}".format(self.value))

        self.function = matches.group("function")
        self.range_start = matches.group("range_start")
        self.range_end = matches.group("range_end")

    def _calculate_value(self):
        if self.formulae is None:
            # this formulae does not exist. A design decision needs to be
            # made to know if we want this to raise an exception or
            # treat this field as 0
            return 0
        values = self._sheet[self.range_start:self.range_end]
        return self.formulae.calculate(values)

    def _get_int_value(self):
        return self._calculate_value()

    def _get_value(self):
        return self._calculate_value()


class IntCell(Cell):

    def __init__(self, value):
        super(IntCell, self).__init__(value=value)
        if not isinstance(value, int) and not isinstance(value, float):
            raise Exception("{0} must be an integer".format(value))
        self.value = value

    def _get_int_value(self):
        return self.value

    def _get_value(self):
        return self.value