"""
7. Scrieți un program care afișează toate elementele din un invetar si calculează suma lor.
Ex, {‘scanue’: 33, ‘,mese’: 22}
Items:  ‘scaune’, ‘mese’
total : 55

"""

inventar = dict(scaune=33, mese=22)

# Afisam toate elementele din inventar.
print("Items: ", ", ".join(inventar))

# Calculam si afisam la ecran suma elementelor din inventar.
print("total: " + str(sum(inventar.values())))
