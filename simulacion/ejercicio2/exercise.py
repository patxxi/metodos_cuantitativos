from random_generator import MixedCongruentialMixed


def run():
    A_generator = MixedCongruentialMixed(a=1, c=3, x=2, m=10)
    A_numbers = A_generator.random(10)

    B_generator = MixedCongruentialMixed(a=5, c=1, x=1, m=8)
    B_numbers = B_generator.random(8)

    C_generator = MixedCongruentialMixed(a=61, c=27, x=100, m=100)
    C_numbers = C_generator.random(5)

    print(A_numbers)
    print(B_numbers)
    print(C_numbers)


if __name__ == '__main__':
    run()
