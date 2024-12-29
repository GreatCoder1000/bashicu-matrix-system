class PSS:
    """Pair-Row BMS"""
    def __init__(self, array):
        if not isinstance(array, list):
            raise TypeError(f'Expected list type for PSS(), not {type(array)}')

        for i in range(len(array)):
            if not isinstance(array[i], tuple) or len(array[i]) != 2:
                raise TypeError(f'Expected tuple of length 2 for array[{i}], not {type(array[i])}')
            if not all(isinstance(x, int) for x in array[i]):
                raise TypeError(f'Expected int elements in tuple for array[{i}]')

        self.sequence = array

    def __str__(self):
        return ''.join(f'({a},{b})' for (a, b) in self.sequence)

    def eval(self, base=3):
        """Evaluate a PSS in a single level of recursion."""

        if not self.sequence:
            raise ValueError("Cannot evaluate an empty sequence.")

        last_pair = self.sequence[-1]
        a, b = last_pair

        if last_pair == (0, 0):
            s = self.sequence[:-1]
            return PSS(s)

        # Correct expansion logic
        new_sequence = self.sequence[:-1]
        for i in range(base):
            new_sequence += [(a + i, b - 1)]
        return PSS(new_sequence)
