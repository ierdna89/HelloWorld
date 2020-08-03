"""
1. Scrieți o funcție care convertește temperatura din grade celsius în fahrenheit
și invers (formula: c/5 = f-32/9)

"""

# Definim functia conversiei temperaturii din grade Farenheit in Celsius


def f_to_c():
    f = float(input("\nIntroduceti temperatura in grade Fahrenheit: "))
    c = round((f - 32) / 1.8, 2)
    print("\nTemperatura DVS in °C este: " + str(c))


# Definim functia conversiei temperaturii din grade Celsius in Farenheit


def c_to_f():
    c = float(input("\nIntroduceti temperatura in grade Celsius: "))
    f = round((c * 1.8 + 32), 2)
    print("\nTemperatura DVS in °F este: " + str(f))


while True:

    tip_conversie = int(input(
        """\n Tastati cifra: \n - \"1\" pentru a converti Fahrenheit in Celsius, \n - \"2\" pentru a converti Celsius in Fahrenheit, \n - sau oricare alta cifra pentru a iesi din program. \n"""))

    if tip_conversie == 1:
        f_to_c()

    elif tip_conversie == 2:
        c_to_f()

    else:
        break
