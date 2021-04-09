import random


personaj = "George"
dirt="Pamant"
stone="Piatra"
iron="Fier"
gold="Aur"
check=True
minereuri = [dirt, stone, iron, gold]

while check:    
    minereul_de_sub_el = random.choices(minereuri, weights=[40,30,20,10])
    print(personaj, " a minat", minereul_de_sub_el)
    if minereul_de_sub_el[0]==gold:
        aur_optiuni = random.randint(0,1)
        if aur_optiuni==0:
            print(personaj, " a decis sa continue si spera sa gaseasca mai multe lucruri valoroase.")
        else:
            print(personaj, " este mandru de ce a gasit si vrea sa se intoarca acasa.\nBye George")
            check=False
            exit
