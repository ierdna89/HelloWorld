"""
3. Scrieți o funcție care sa afiseze toți divizorii unui număr întreg.

"""


def divizor(input_number):
    for i in range(1, input_number + 1):
        if (input_number % i) == 0:
            print(i)


numar_intreg = int(input("Introduceti un numar intreg: "))

print(divizor(numar_intreg))
