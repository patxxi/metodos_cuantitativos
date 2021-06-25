class MixedCongruentialMethod():
    def __init__(self, a, c, x, m):
        self._a = a
        self._x = x
        self._c = c
        self._m = m

    def random(self, length=1, low=0, high=10):
        results = []

        # This range could be with start and final range or just N numbers

        for i in range(length):
            aux = True
            while(aux):

                pseudo_result = self._a * self._x + self._c
                mod = pseudo_result % self._m
                result = mod / self._m

                self._x = mod
                if result > low/10 and result <= high/10:
                    aux = False

            results.append(result)
        return results


if __name__ == '__main__':
    random_generator = MixedCongruentialMethod(5, 7, 4, 8)
    print(random_generator.random(2, 10))
