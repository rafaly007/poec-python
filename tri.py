maListe=[4, 8, 415, 1, 25, 75, 6]
a=0
b=a+1
compteur=0
while compteur<len(maListe)
    if maListe[a]>maListe[b]
        maListe[a],maListe[b]=maListe[b],maListe[a]
    compteur+=1
print(maListe)