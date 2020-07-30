"""
4. Calculati suma tuturor numerelor între 1000 si 2300 care se împart fără rest la 5 și 7.

"""

sum_of_numbers = 0

for i in range(1000, 2300 + 1):
    if i % 5 == 0 and i % 7 == 0:
        pass
    sum_of_numbers += i

print("Suma numerelor este: " + str(sum_of_numbers))

