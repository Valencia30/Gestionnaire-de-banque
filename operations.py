def menu():
    print("______PROGRAMME GESBANK______\n")
    print("1-Créer un compte")
    print("2-Faire un retrait")
    print("3-Faire un versement")
    print("4-Faire une consultation")
    print("5-QUITTER")
    choix=int(input("Votre opération: "))
    return choix

import random
def creer():
    print("\n______Création d'un compte______\n")
    nom=input("Entrez votre nom: ")
    prenom=input("Entrez votre prenom: ")
    mdp=input("Entrez votre code secret(4 chiffres):")
    num =str(random.randint(10**15, 10**16-1))
    fond=0
    gestion=open("gestion.txt","a")
    compte= nom +" "+ num +" "+str(mdp)+" "+str(fond)
    gestion.write(compte+"\n")
    gestion.close()
    print("FELICITATIONS",nom,prenom," votre compte a bien été crée")
    print("Votre numéro de compte est",num,"\n")
    


def retour():
    print("1-Retour")
    print("2-QUITTER")
    choix2=int(input("Votre choix: "))
    return choix2


def retrait():
    print("\n________Retrait d'argent_________\n")
    num = input("Entrez votre numéro de compte: ")
    gestion = open("gestion.txt","r")
    comptes = gestion.readlines()
    for i, compte in enumerate(comptes):
        elements = compte.split(" ")
        if str(num) in elements:
            retrait =int(input("Entrez le montant à retirer: "))
            fond=int(elements[-1])
            if retrait <= fond:
                fond -= retrait
                elements[-1] = str(fond)
                comptes[i] = " ".join(elements) + "\n"
                gestion = open("gestion.txt","w")
                gestion.writelines(comptes)
                gestion.close()
                print("Vous avez retiré", retrait)
                print("Votre nouveau solde est de", fond)
                return fond
            else:
                print("Le solde est insuffisant")
                return fond
    print("Ce numéro de compte est invalide")
        

def versement():
     print("\n________Versement d'argent_________\n")
     num=int(input("Entrez votre numéro de compte:"))
     gestion=open("gestion.txt","r")
     comptes=gestion.readlines()
     for i, compte in enumerate(comptes):
         elements = compte.split(" ")
         if str(num) in elements:
             ajout=int(input("Entrez le montant: "))
             fond=int(elements[-1])
             fond+=ajout
             elements[-1]=str(fond)
             comptes[i] = " ".join(elements) + "\n"
             gestion=open("gestion.txt","w")
             gestion.writelines(comptes)
             gestion.close()
             print("Le versement de", ajout, "a été effectué avec succès sur le compte")
             print("Votre nouveau solde est de", fond)
             return fond
     print("Ce numéro de compte est invalide")



def consultation():
    print("\n________Consultation_________\n")
    num=int(input("Entrez votre numéro de compte:"))
    gestion=open("gestion.txt","r")
    comptes=gestion.readlines()
    for i, compte in enumerate(comptes):
         elements = compte.split(" ")
         if str(num) in elements:
             fond=int(elements[-1])
             print("Votre solde est de", fond)
             return fond
    print("Ce numéro de compte est invalide")
    
    
    
     
     
    

    
   
    

    
