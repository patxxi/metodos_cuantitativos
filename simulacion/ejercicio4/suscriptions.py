import random


def run():
    n = int(input("Write how many house will visite the seller: "))
    articles_woman = {
        "0.6": 1,
        "0.3": 2,
        "0.1": 3,
        "0": 4
    }

    articles_man = {
        "0.1": 1,
        "0.4": 2,
        "0.3": 3,
        "0.2": 4
    }
    benefit = 0

    for i in range(n):
        random_number = random.randint(1, 100)

        print("\n\n")
        print(
            f"---------------------------------------------------------CLIENTE NUMERO {i+1}---------------------------------------------------------")
        if random_number >= 70:
            print(
                f"Numero aleatorio {random_number}, si fue recibido el vendedor")
            random_number = random.randint(1, 100)

            if random_number <= 80:
                print(
                    f"numero aleatorio {random_number}, lo recibio un hombre")

                random_number = random.randint(1, 100)

                if random_number <= 25:
                    print(
                        f"Numero aleatorio {random_number}, se consiguio la venta")
                    random_number = round(random.random(), 2)
                    print(
                        f"Numero aleatorio {random_number}, el hombre comprara un total de {articles_man[str(random_number)]} suscripciones")
                    benefit += articles_man[str(random_number)] * 3000
                else:
                    print(
                        f"Numero aleatorio {random_number}, no se consiguio la venta")

            else:
                print(
                    f"numero aleatorio {random_number}, lo recibio una mujer")

                random_number = random.randint(1, 100)
                if random_number <= 15:

                    print(
                        f"Numero aleatorio {random_number}, se consiguio la venta")
                    random_number = round(random.random(), 2)

                    print(
                        f"Numero aleatorio{random_number}, la mujer compara un total de {articles_woman[str(random_number)]} suscripciones")

                    benefit += articles_woman[str(random_number)] * 3000
                else:
                    print(
                        f"Numero aleatorio {random_number}, no se consiguio la venta")

        else:
            print(
                f"Numero aleatorio {random_number}, no fue recibido el vendedor")


if __name__ == '__main__':
    run()
