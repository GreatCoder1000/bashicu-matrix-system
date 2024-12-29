class QSS:
    """4-row BMS"""
    def __init__(self, array):
        if not isinstance(array, list):
            raise TypeError(f'Expected list type for QSS(), not {type(array)}')

        for i in range(len(array)):
            if not isinstance(array[i], tuple) or len(array[i]) != 4:
                raise TypeError(f'Expected tuple of length 4 for array[{i}], not {type(array[i])}')
            if not all(isinstance(x, int) for x in array[i]):
                raise TypeError(f'Expected int elements in tuple for array[{i}]')

        self.sequence = array

    def __str__(self):
        return ''.join(f'({a},{b},{c},{d})' for (a, b, c, d) in self.sequence)

    def eval(self, base=3):
        """Evaluate a QSS in a single level of recursion."""

        if not self.sequence:
            raise ValueError("Cannot evaluate an empty sequence.")

        last_group = self.sequence[-1]
        a, b, c, d = last_group

        if last_group == (0, 0, 0, 0):
            s = self.sequence[:-1]
            return QSS(s)

        # Correct expansion logic
        new_sequence = self.sequence[:-1]
        for i in range(base):
            new_sequence += [(a + i, b + i, c + i, d - 1)]
        return QSS(new_sequence)
