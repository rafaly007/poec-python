maListe=[]
print(type(maListe))
maListe=[1,2,3]
print(maListe)
maListe=[]
maListe.append(1)
print(maListe)
maListe.append("Salut")
print(maListe)

maListe=["1er","deuxieme","troisieme"]
print(maListe[1])
print(maListe[2])
maListe[1]="chargement"

#---------------

maListe=["1er","deuxieme","troisieme"]
#supprimé avec l'index
del maListe[1]
print(maListe)
#Supprimé avec la valeur
maListe.remove("troisieme")
print(maListe)
#---------------
maListe = ["1er", "deuxieme", "troisieme"]
secondeList = maListe
maListe[0] = "toto"
print(secondeList)

# Good
maListe = ["1er", "deuxieme", "troisieme"]
secondeList = maListe[:]
maListe[0] = "toto"
print(secondeList)

maListe = list(range(15))
print(maListe)
liste = list(range(10))
liste.extend(maListe)
print(liste)


# Un dictionnaire une liste avec des clés numériques.
monDico = {}
monDico["name"] = "Mehdi"
monDico["height"] = "1m90"
print(monDico)

maliste=[1,2,3,4,5,6,7,8]
print(maliste)
a=0
b=a+1
maliste[a],maliste[b]=maliste[b],maliste[a]
print(maliste)