import math
import random


class QueueingTheory():

    def __init__(self, miu, lamb):
        self._lamb = lamb
        self._miu = miu
        # Tiempo medio de un paquete permanece en el sistema
        self._w = 1 / (self._miu - self._lamb)
        # Tiempo medio de espera en la cola
        self._wq = self._w - (1 / self._miu)
        # Intensidad del trafico en el sistema
        self._roh = self._lamb / self._miu
        # Numero medio de paquetes en el sistema
        self._Ls = self._lamb * self._w
        # Numero medio de paquetes en la cola
        self._Lq = self._lamb * self._wq
        # Probabilidad de que no existan paquetes en el sistema
        self._p0 = (self._roh ** 2) / (1 - self._roh)

    def probability_packages_on_system(self, N):
        pn = (1 - (self._lamb / self._miu)) * (self._lamb / self._miu) ** N
        return pn

    def probability_income_package(self, N, time):
        return math.e ** (-self._lamb*time) * ((self._lamb*time)**N)/math.factorial(N)

    def probability_stay_time(self, time):
        return (math.e ** (-self._miu * (1-self._roh) * time))


def run():
    queue = QueueingTheory(60/60, 45/60)
    queue_probabilities = [
        queue.probability_income_package(i, 1) for i in range(6)]

    for i, probability in enumerate(queue_probabilities):
        print(
            f"Probabilidad de que hayan {i} paquetes en el sistema: {probability}")
    probabilities = []
    PERCENTAGE = 100
    clients = 0
    actual_clients = 0
    treated_clients = 0
    PROBABILITY_BEING_SERVED = queue.probability_stay_time(1)
    TIME = 60

    for i in range(len(queue_probabilities)-1, 0, -1):
        PERCENTAGE -= queue_probabilities[i] * 100
        probabilities.append(PERCENTAGE)

    probabilities.sort()

    for i in range(TIME):
        print(
            f"\n------------------------------------- Minuto {i+1} -------------------------------------")
        random_number = random.random() * 100

        prev = float()
        for i, prob in enumerate(probabilities):
            print(f"prev = {prev}, actual = {prob}")
            if random_number <= prob and random_number > prev:
                clients += i
                actual_clients += i
                print(f"Numero aleatorio generado: {random_number}")
                print(f"Han entrado {i} paquetes a la cola")

                break
            prev = prob

        random_number = random.random()
        if random_number <= PROBABILITY_BEING_SERVED:
            print("Se ha atendido a un cliente este minuto")
            treated_clients += 1
            actual_clients = (actual_clients - 1 if actual_clients > 0 else 0)
        else:
            print("No se ha atendido a un cliente este minuto")

        print(f"""
Paquetes totales recibidos hasta este minuto: {clients}
Paquetes actuales en la cola en este minuto: {actual_clients}
Paquetes atendidos hasta este minuto: {treated_clients}
                """)

    print(f"\n------------------------------------- Fin de la simulacion. Analisis de detalles-------------------------------------")
    print(f"""
Tiempo medio de espera en la cola: {queue._wq}
Tiempo medio de espera en el sistema: {queue._w}
Tiempo medio de paquetes en la cola: {queue._Lq}
Tiempo medio de paquetes en el sistema: {queue._Ls}
            """)


if __name__ == "__main__":
    run()
