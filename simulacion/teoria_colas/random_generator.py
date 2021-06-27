class MixedCongruentialMethod():
    def __init__(self, a, c, x, m):
        """"Class to create a generator of random numbers
        Using the Mixed Congruential Method, this needs
        a, c, x, m in order"""
        self._a = a
        self._x = x
        self._c = c
        self._m = m

    def random(self, length=1):
        """Function to create N random numbers."""
        results = []

        for i in range(length):
            pseudo_result = self._a * self._x + self._c
            mod = pseudo_result % self._m
            result = (mod, mod / self._m)
            results.append(result)
            self._x = mod
        return results


if __name__ == '__main__':
    pass
