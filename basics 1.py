import random

print("V3kky's Crazy lotto Game!")
print("-----------------------\n")

hvlR = float(input("Hoeveel roosters wilt u spelen? :\n"))
prijs = hvlR*2.5

while hvlR >5:
    float(input("Sorry u kan MAX 5 roosters spelen! probeer opnieuw :"))
else:
    print("Dat komt op", + prijs, "€")

sterren = []
nummers = []
count = 0
rooster = 1

while count != hvlR:
    for i in range(1, 6):
        nr = random.randint(1, 50)

        while nr in nummers:
            nr = random.randint(1, 50)
        nummers.append(nr)

    nummers.sort()

    print("Rooster", + rooster)
    print("------------------")
    print(*nummers, "Nummers")
    count = count + 1
    rooster = rooster + 1
    nummers.clear()

    for i in range(1, 3):
        ster = random.randint(1, 12)

        while ster in sterren:
            ster = random.randint(1, 12)
        sterren.append(ster)

    sterren.sort()
    print(*sterren ,"Sterren", )
    print("-------------------")
    sterren.clear()