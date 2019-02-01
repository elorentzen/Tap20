"""
TAP 23

def infinete_numbers():
    i = 0
    while True:
        print(i)
        i+=1

Rework the function above into a generator.
explain trough commenting your own code, why generators are great!
add new functionallity as you see fit.
"""

def gen():
#Generatorer er kjekke fordi de er funksjoner som lar en bruke for eksempel for loop som i denne koden.
#I dette eksempelet er det en simpel nummergenerator som genererer nummer opp til ønsket antall.
#Antallet blir satt i for loopen og er i dette tilfellet 1000.

#Her sier vi at tellingen skal starte på 1. Videre sier vi at når i=1 skal koden "yielde" i+1.
    i = 1
    while True:
        yield i
        i+=1

#For at generatoren skal telle lenger enn til 1 legges det inn en for loop som sier at hvis "i"
#er høyere enn 1000, skal koden brytes. Hvis ikke skal en printe teksten "Number: " i lag med tallet.

for i in gen():
    if i > 1000:
        break
    else:
        print("Number: ", i)
#Hvis en ønsker en infinite number generator kan en fjerne deler av koden slik at det blir:

#for i in gen():
#print("Number: ", i)

#Da vil ikke tellingen stoppe på 1000, men når koden manuelt stoppes i cli.
gen()
