import random


def run():
    number_clients = int(
        input("Insert how many potential clients you will visit"))
    random_number = random.random(1, 10)
    if random_number > 7:
        print(
            f"Numero aleatorio: {random_number}, si atendio alguien a la puerta")
        random_number = random.random(1, 10)
        if random_number <= 8:
            print(f"Numero aleatorio: {random_number}, atendio un hombre")
            random_number = random.random(1, 10)

            if random_number <= 2.5:
                print(
                    f"Numero aleatorio: {random_number}, el cliente si comprara al menos una suscripcion")
                random_number = random.random(1, 10)


            else:
                print(
                    f"Numero aleatorio: {random_number}, el cliente no comprara ninguna suscripcion")

        else:
            print(f"Numero aleatorio: {random_number}, atendio una mujer")

    else:
        print(
            f"Numero aleatorio: {random_number}, No atendio alguien a la puerta")


if __name__ == '__main__':
    run()
