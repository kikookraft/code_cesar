import random

###### UTILITAIRES ######

# alphabet = """!#$%&'()*+,-./0123456789 :;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_abcdefghijklmnopqrstuvwxyzéàèùê£âîôûçÉÀÈÙÊÂÎÔÛÇ"""
alphabet = """À#-19âW:x=d]5ùêlIw^mL@0rz>_BKXe£%TÎqc'sÊPj<b.RûFé;È!,QDHiV+tn2JÇàÉ&Oh)Â3vZî S4Gya8ÔgE*Ù?u/$pUCkA(ôNM6Ûè[çfYo7"""

# fonction pour melanger l'alphabet (utilisé une seule fois pour l'alphabet au dessus)
def melange_alphabet():
    """Mélange l'alphabet"""
    return "".join(random.sample(alphabet,len(alphabet)))

###### FONCTIONS DE CLE ######
def pgcd(a:int,b:int):
    while b!=0:
        a,b=b,a%b
    return a

def genere_cle():
    """Génère une clé a et b pour le code affine"""
    a = random.randint(1,1000)
    b = random.randint(1,1000)
    # verifier que a est premier avec len(alphabet)
    while not verif_cle(a,len(alphabet)):
        a = random.randint(1,1000)
    # while not verif_cle(a,b):
    #     b = random.randint(1,1000)
    return a,b

def verif_cle(a:int,b:int):
    if pgcd(a,b)==1:
        return True
    else:
        return False

def prime(a:int,b:int):
    """Algorithme d'Euclide étendu afin de trouver la clé de déchiffrement"""
    r,u,v,r1,u1,v1 = a,1,0,len(alphabet),0,1
    while r1!=0:
        q = r//r1
        r,u,v,r1,u1,v1 = r1,u1,v1,r-q*r1,u-q*u1,v-q*v1
    v = -u*b%len(alphabet)
    return u,v


###### FONCTIONS ######
def crypt(msg:str):
    trad = ""
    i=len(msg)-1
    while i>-1:
        trad+=msg[i]
        i-=1
    return trad

def optimized_crypt(msg:str):
    """Crypte le message en inversant l'ordre des lettres"""
    return msg[::-1]


# chifrage par code césar avec une clé parmi l'alphabet
def cesar(msg:str, cle:int):
    """Crypte le message en utilisant le code césar"""
    trad = ""
    for i in msg:
        #changer la lettre parmis l'alphabet
        idx = alphabet.index(i) #trouver l'index de la lettre dans l'alphabet
        trad+=alphabet[(idx+cle)%len(alphabet)] #ajouter la lettre à la traduction
    return trad

def code_vigenere(msg:str, cle:str, mode:str="crypt"):
    """Crypte le message en utilisant le code vigenère
    cle est la clé de chiffrement
    msg est le message à chiffrer"""
    trad = ""
    for i in range(len(msg)):
        #changer la lettre parmis l'alphabet
        idx = alphabet.index(msg[i]) #trouver l'index de la lettre dans l'alphabet
        idx_cle = alphabet.index(cle[i%len(cle)]) #trouver l'index de la lettre dans l'alphabet
        if mode=="crypt":
            trad+=alphabet[(idx+idx_cle)%len(alphabet)] #ajouter la lettre à la traduction
        else:
            trad+=alphabet[(idx-idx_cle)%len(alphabet)]
    return trad

# code cesar affine
def affine(msg:str,a:int,b:int,mode="crypt"):
    """Crypte le message en utilisant le code affine
    a et b sont les clés de chiffrement
    mode peut prendre les valeurs "crypt" ou "decrypt" """
    #if pgcd(a,b)!=1: return #quitter si a et b ne sont pas premiers entre eux
    trad = ""
    if mode=="crypt":
        for i in msg:
            #changer la lettre parmis l'alphabet
            idx = alphabet.index(i) #trouver l'index de la lettre dans l'alphabet
            trad+=alphabet[(a*idx+b)%len(alphabet)] #ajouter la lettre à la traduction
        return trad
    elif mode=="decrypt":
        c,d = prime(a,b)
        for i in msg:
            # changer la lettre parmis l'alphabet
            idx = alphabet.index(i) #trouver l'index de la lettre dans l'alphabet
            trad+=alphabet[(c*idx+d)%len(alphabet)] #ajouter la lettre à la traduction
            
        return trad


if __name__=="__main__":
    print("Bienvenue dans le programme de cryptage\n")
    msg = input("Entrez le message : ")
    print("1 - Code Inverse")
    print("2 - Code César")
    print("3 - Code Vigenère")
    print("4 - Code César Affine")
    choix = input("Que voulez-vous faire ? \n> ")
    
    # Choix de l'utilisateur
    match choix:
        case "1":
            print(f">>> {optimized_crypt(msg)} <<<")
        case "2":
            cle = int(input("Entrez la clé : "))
            print(f">>> {cesar(msg,cle)} <<<")
        case "3":
            choix2 = input("\n1 - Chiffre\n2 - Déchiffre\nQuel est votre choix ? \n> ")
            cle = input("Entrez la clé : ")
            match choix2:
                case "1":
                    print(f">>> {code_vigenere(msg,cle)} <<<")
                case "2":
                    print(f">>> {code_vigenere(msg,cle,'decrypt')} <<<")
                case _:
                    print("Choix invalide")
                    exit()
        case "4":
            choix2 = input("\n1 - Chiffre\n2 - Déchiffre\n3 - Clé Manuelle\nQuel est votre choix ? \n> ")
            match choix2:
                case "1":
                    a,b = genere_cle()
                    print("La clé est : ", a,b)
                    print("Le message crypté est : \n>>>", affine(msg,a,b),"<<<\n")   
                case "2":
                    a = int(input("Entrez la clé a : "))
                    b = int(input("Entrez la clé b : "))
                    print("Le message décrypté est : \n>>>", affine(msg,a,b,"decrypt"),"<<<\n")    
                case "3":
                    a = int(input("Entrez la clé a : "))
                    b = int(input("Entrez la clé b : "))
                    mode = input("\n1 - Chiffre\n2 - Déchiffre\nQuel est votre choix ? \n> ")
                    match mode:
                        case "1":   
                            print("Le message est : \n>>>", affine(msg,a,b,"crypt"),"<<<\n") 
                        case "2":
                            print("Le message est : \n>>>", affine(msg,a,b,"decrypt"),"<<<\n")
                case _:
                    print("Choix invalide")
                    exit() 
        
        # Test automatique
        case "5":
            print("Test automatique affine")
            print("Taille de l'alphabet : ", len(alphabet))
            print()
            phrases = ["Bonjour","Je suis un test","Je suis un test avec des accents éàèùê£âîôûçÉÀÈÙÊÂÎÔÛÇ","Il a mangé des camions a la lavande?", "Anticonstututionnellement je sais pas quoi dire OMG!!!"]
            for i in phrases:
                print(f"Phrase : {i}")
                a,b = genere_cle()
                print("La clé : ", a,b)
                cr = affine(i,a,b)
                dcr = affine(cr,a,b,"decrypt")
                print("Le message crypté  : >>>", cr,"<<<")  
                print("Le message décrypté : >>>", dcr,"<<<")
                if i==dcr:
                    print("Test réussi ✔️")
                else:
                    print("Test échoué ❌")
                print()

        case _:
            print("Choix invalide")
            exit()       
                    

        