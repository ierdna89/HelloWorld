"""
Scrieți un program care o sa creeze un joc pentru ghicirea capitalei unei țări, cu 4 opțiuni de răspuns.
Citiți conținutul fișierului countries.txt. (https://bit.ly/3fd4EFz)
Utilizați funcția random pentru a alege țara și capitala ei, folosiți aceeași metodă pentru a găsi alte
3 opțiuni de răspuns.
Creați întrebarea folosind 4 opțiuni de răspuns.
Captați răspunsul utilizatorului  folosind funcția input() și afișați răspunsul corect.

"""
import random

countries = {}

with open("countries.txt", "r") as f:
    for line in f:
        country, capital = line.split(",")
        countries[country] = capital.replace("\n", "")

quit_input = ""

while quit_input != "quit":

    capital = list(countries.values())

    country_capital = country_question, capital_question = random.choice(
        list(countries.items()))

    three_capitals = random.sample(capital, 3)

    capital_1, capital_2, capital_3 = three_capitals

    if country_capital[1] not in three_capitals:
        print(
            f"Care este capitala tarii {country_question}? \nAlegeti din variantele de mai jos.")
        print(
            f"1. {capital_1} \n2. {capital_2} \n3. {capital_question} \n4. {capital_3}")

        try:
            response = int(input("Introduceti numarul: "))

            if response == int(3):
                print("Felicitari! Ati ales varianta corecta!\n")
                quit_input = input(
                    "Tastati \"quit\" daca doriti sa iesiti din program sau orice altceva pentru a continua.\n")

            else:
                print("Gresit! \nMai incercati data viitoare.")
                quit_input = input(
                    "Tastati \"quit\" daca doriti sa iesiti din program sau orice altceva pentru a continua.\n")

        except ValueError:
            print("Nu ati introdus o cifra!\n")

    else:
        pass
