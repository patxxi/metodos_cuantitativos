def run():
    flips = [5, 2, 4, 9, 7]

    print("Numero aleatorio \t Resultado")
    for flip in flips:
        if flip <= 4:
            print(f"{flip} \t\t\t Cara")
        else:
            print(f"{flip} \t\t\t Cruz")


if __name__ == '__main__':
    run()
