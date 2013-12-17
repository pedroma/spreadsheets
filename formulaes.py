class SUM(object):

    def calculate(self, values):
        """
        Defines the =SUM(RANGE) formulae
        """
        return sum(values)


class COUNT(object):

    def calculate(self, values):
        """
        Defines the =COUNT(RANGE) formulae
        """
        values = filter(lambda x: x._get_value() != "", values)
        return len(values)


class MAX(object):
    def calculate(self, values):
        """
        Defines the =MAX() formulae
        """
        values = filter(lambda x: x._get_value() != "", values)
        return max(values, key=lambda x: x._get_int_value())._get_int_value()


class MIN(object):
    def calculate(self, values):
        """
        Defines the =MIN(RANGE) formulae
        """
        values = filter(lambda x: x._get_value() != "", values)
        return min(values, key=lambda x: x._get_int_value())._get_int_value()


