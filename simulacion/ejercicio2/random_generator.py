class MixedCongruentialMethod():
    def __init__(self, a, c, x, m):
        self._a = a
        self._x = x
        self._c = c
        self._m = m

    def random(self, length=1):
        results = []

        for i in range(length):
            pseudo_result = self._a * self._x + self._c
            mod = pseudo_result % self._m
            result = (mod, mod / self._m)
            results.append(result)
            self._x = mod
        return results


if __name__ == '__main__':
    random_generator = MixedCongruentialMethod(5, 7, 4, 8)
    print(random_generator.random(8))
