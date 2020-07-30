"""
5. Scrieți o funcție care sa calculeze numărul de litere și cifre din un text.

"""


def verify_length(text):
    letters = 0
    numbers = 0

    for i in text:
        if i.isalpha():
            letters += 1
        elif i.isdigit():
            numbers += 1

    print("\nNumerele sunt urmatoarele:")
    print("Litere: " + str(letters))
    print("Cifre: " + str(numbers))


text_input = input("\nIntroduceti textul spre a fi analizat:\n")

verify_length(text_input)
