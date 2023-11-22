def check_food(type, saison):
    if type == 'fruits' and saison == 'hiver':
        print("orange, mandarine et kiwi")
    elif type == 'fruits' and saison == 'ete':
        print("Poire, fraise, cassis")
    elif type == 'legume' and saison == 'hiver':
        print("carotte, topinambour, endive")
    elif type == 'legume' and saison == 'ete':
        print("artichaut, aubergine,navet")
    else:
        print("Je ne sais pas")

check_food('fruits', 'hiver') 
check_food('fruits', 'ete')  
check_food('legume', 'hiver') 
check_food('legume', 'ete')
check_food('viande', 'ete')  
