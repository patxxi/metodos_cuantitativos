class MixedCongruentialMethod():
    def __init__(self, a, c, x, m):
        self._a = a
        self._x = x
        self._c = c
        self._m = m

    def random(self, start=1, final=0):
        results = []

        # This range could be with start and final range or just N numbers

        for i in (range(start, final) if final != 0 else range(start)):
            pseudo_result = self._a * self._x + self._c
            mod = pseudo_result % self._m
            result = (mod, mod / self._m)
            results.append(result)
            self._x = mod
        return results


if __name__ == '__main__':
    random_generator = MixedCongruentialMethod(5, 7, 4, 8)
    print(random_generator.random(2, 10))
