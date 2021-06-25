def run():
    numbers = [5, 2, 4, 9, 7]
    print("Numero Aleatorio \t Color")
    for number in numbers:

        if number < 5:
            print(f"{number} \t\t\t Verde") if number < 4 else print(
                f"{number} \t\t\t Amarillo")

        elif number >= 5:
            print(f"{number} \t\t\t Rojo")


if __name__ == '__main__':
    run()
