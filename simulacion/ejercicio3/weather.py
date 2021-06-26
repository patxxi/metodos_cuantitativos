def run():
    random_numbers = [8, 1, 3, 7, 2, 7, 1, 6, 5, 5]
    rain_day_before = False
    for i, number in enumerate(random_numbers):
        if rain_day_before:
            if number >= 4:
                print(f"Dia {i+1}, Si llueve")
                rain_day_before = True
            else:
                print(f"Dia {i+1}, No llueve")
                rain_day_before = False

        else:
            if number >= 8:
                print(f"Dia {i+1}, Si llueve")
                rain_day_before = True
            else:
                print(f"Dia {i+1}, No llueve")
                rain_day_before = False


if __name__ == '__main__':
    run()
