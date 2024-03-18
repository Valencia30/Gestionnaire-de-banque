from operations import creer, menu, retour,retrait,versement,consultation
op=menu()
ch=0
while op!=5 and ch!=2 :
    match op:
        case 1:creer()
        case 2:retrait()
        case 3:versement()
        case 4:consultation()
        case _:print("ERREUR")
    ch=retour()
    match ch:
        case 1:op=menu()
        case _:print("ERREUR")

