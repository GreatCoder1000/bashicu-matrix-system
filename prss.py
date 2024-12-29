class PrSS:
    """Single-Row BMS"""
    def __init__(self, array):
        if not isinstance(array, list):
            raise TypeError(f'Expected list type for PrSS(), not {type(array)}')

        sequence = array[:]
        for i in range(len(sequence)):
            if not isinstance(sequence[i], int):
                raise TypeError(f'Expected int type for array[{i}], not {type(sequence[i])}')

        if len(sequence) == 0:
            self.sequence = sequence
            return

        last = -1
        for this in sequence:
            if this > (last + 1):
                raise ValueError(f'Invalid PrSS: {sequence}')
            last = this

        self.sequence = sequence

    def __str__(self):
        return ''.join(f'({item})' for item in self.sequence)

    def eval(self, base=3):
        """Evaluate a PrSS in a single level of recursion."""

        if not self.sequence:
            raise ValueError("Cannot evaluate an empty sequence.")

        if self.sequence[-1] == 0:
            s = self.sequence[:-1]
            return PrSS(s)

        bad = self.sequence[-1]
        s = []
        for i in range(len(self.sequence) - 2, -1, -1):
            s.insert(0, self.sequence[i])
            if self.sequence[i] < bad:
                t = self.sequence[:i]
                return PrSS(t + s * (base + 1))
        return PrSS(s * base)
