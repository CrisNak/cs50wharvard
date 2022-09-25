people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

#people.sort() se colocar apenas esta frase, o programa não ordena a lista, pq não sabe como comprar dicionários 

def f(person):
    return person["name"]
    # pode retornar por house: return person["house"]
people.sort(key=f)

#people.sort(key=lambda person: person["name"]) --- versão resumida

print(people)