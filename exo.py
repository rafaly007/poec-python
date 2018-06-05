def exo2():
    i=0
    j=13
    while i>=0 and i<=10:
        print(i*j)
        i=i+1
# exo2()

def exo4():
    mot=input("entrer le mot")
    print(len(mot))
# exo4()

# def exo5():
#     print("entrer un nombre")
#     nbr=int(input())
#     if nbr % 2 == 1
#         print("impair")
#     else:
#         print("pair")
# exo5()




def exo9():
    val=int(input("entrer un nombre :"))
    somme=0
    for i in range(0,val+1):
        somme=i+somme
    print(somme)
# exo9()

def exo10():
    age=int(input("entrer son age"))
    if age == 6 or age ==7:
        print("poussin de 6 à 7 ans")
    elif age == 8 or age ==9:
        print("pupille de 8 à 9 ans")
    elif age == 10 or age ==11:
        print("Mimmie de 10 à 11 ans")
    elif age >=12:
        print("cadet apres 12 ans")
# exo10()

def exo11():
    pu=int(input("prix unitaire"))
    nbr=int(input("nombre d'article"))
    totalHt=pu*nbr
    totalTtc=totalHt*1.20
    print(totalHt)
    print(totalTtc)
# exo11()

def exo12():
    nbr=int(input("donner un nombre"))
    fact=1
    i=1
    while i<=nbr:
        fact=fact*i
        i=i+1
    print("factoriel de "+str(nbr)+" = "+str(fact))
# exo12()

def exo13():
    nombre=int(input("donner un nombre entier"))
    binaire= []
    while nombre:
        reste=nombre%2
        nombre=nombre//2
        binaire.append(reste)
    print(binaire)
# exo13()

def exo14():
    somme=0
    for i in range(1,1000):
        if i % 5 == 0:
            somme=i+somme
    print(somme)
# exo14()

def exo15():
    a=0
    b=1
    c=0

    nombre=int(input("entrer un nombre"))
    for x in range(0, nombre):
        print(a,b)
        c=a+b
        a=b
        b=c
    # print(a,c)
# exo15()


import random
def exo17():
    aleatoire = random.randint(1,100)
    # print("aleatoire:" + str(aleatoire))
    compt=0
    print("Trouve un chiffre entre 1 à 100")
    while True and compt<10 :
        compt = compt + 1
        # print("compteur: "+str(compt))
        val=int(input("saisi un nombre : "))
        if compt == 10:
            print("perdu!")
            break
        elif val<aleatoire:
            print("plus grand: ")
        elif val>aleatoire:
            print("plus petit: ")
        elif val==aleatoire:
            print("gagné!")
            break

exo17()