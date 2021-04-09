import random


personaj = "George"
dirt="Pamant"
stone="Piatra"
iron="Fier"
gold="Aur"
Smarald = "Smarald"
Lava = "Lava"

check=True
minereuri = [dirt, stone, iron, gold, Smarald, Lava]

while check:    
    minereul_de_sub_el = random.choices(minereuri, weights=[40,30,20,10,5,15])
    print(personaj, " a minat", minereul_de_sub_el)
    if minereul_de_sub_el[0]==gold:
        aur_optiuni = random.randint(0,1)
        if aur_optiuni==0:
            print(personaj, " a decis sa continue si spera sa gaseasca mai multe lucruri valoroase.")
        else:
            print(personaj, " este mandru de ce a gasit si vrea sa se intoarca acasa.\nBye George")
            check=False
            exit
    if minereul_de_sub_el[0] == Smarald:
        print(personaj, "A gasit smaraldul pleaca fericit acasa.")
        check = False
        exit
    if minereul_de_sub_el[0] == Lava:
        print(personaj, "A cazut in lava, e mort.")
        check = False
        exit
        
