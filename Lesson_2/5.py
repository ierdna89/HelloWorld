"""

5. Scrieti un program care primeste la input numele fisierului 
(text.txt, program.java) si intoarce extesia lui (txt, java). 
Puteti sa folositi functia split() 

"""

nume_fisier = input("Introduceti denumirea fisierului si extesia acestuia: ")

lista = nume_fisier.split(".", 1)

print("Extensia fisierului DVS este: " + lista[1])
