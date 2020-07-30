"""
2. Scrieți o funcție determina dacă un text este palindrom (caiac, capac, minim) 

"""


def palindrom():
    text_input = input(
        "\nIntroduceti cuvantul spre a fi verificat daca este sau nu palindrom.\n")

    text_reversed = text_input[::-1]

    if text_input == text_reversed:
        print("\nCuvantul introdus ESTE un palindrom.")

    else:
        print("\nCuvantul introdus NU este un palindrom.")


while True:

    palindrom()

    iesire = input(
        "\nPentru a iesi din program tastati \"exit\" pentru a continua tastati orice alt caracter\n")

    if iesire == "exit":
        break
