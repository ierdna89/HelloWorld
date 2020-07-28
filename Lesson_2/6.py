"""
6. Fie următoarea listă: a = ['a', 'b', 'c', 'd']
6.1 Ce valoare are expresia a[int(int('3' * 2) // 11] ?
6.2 Adaugati o valoare nouă în lista a pe prima poziție.
6.3 Ștergeți ultimele 2 valori din lista.
6.4 Ordonati lista a descrescator
6.5 Creați o listă nouă b care sa conțină toate elementele din lista a cu excepția primelor 2 elemente.

"""

# 6.1

a = ["a", "b", "c", "d"]

new_var = a[int(int("3" * 2) // 11)]

print(new_var)  # Afisam la ecran valoarea expresiei din variabila "new_var".


# 6.2

a.insert(0, "x")  # Adaugam o valoare nouă în lista a pe prima poziție.

print(a)    # Afisam la ecran lista "a" cu noile valori.


# 6.3

del a[-2:]  # Ștergem ultimele 2 valori din lista.

print(a)  # Afisam la ecran lista "a" cu noile valori.


# 6.4

a.sort(reverse=True)  # Ordonam lista a descrescator.

print(a)  # Afisam la ecran lista "a" cu noile valori.


# 6.5

# Cream o noua lista "b" care sa cuprinda toate elementele listei "a", cu exceptia primelor doua valori.
b = a[2:]

print(b)  # Afisam la ecran noua lista "b" cu noile valori.
