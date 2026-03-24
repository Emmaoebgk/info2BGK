import random
'''
a = 1
b = 2.5
c = "szöveg" # \n \t
c2= " más"
d = True
ab = a + b
cc2= c + c2

print(a + b, type(cc2), end= "Minta")

# tömb nem táltoztatható
tomb = (" hétfő", "kedd", "szerda"," csütörtök", "péntek", " szombat", "vasárnap" )

# listák  modnsithtóak, hivatkozás átadása
lista = [" alma", "körte", "banán", 7, 10, 4.5, True]

lista.append() -> hozzáadás
lista.remove() -> adott elem eltávolitád
lista.pop () -> adott helyiértékű elem eltávolitás
lista.insert() -> adott helyiérték elem beillesztése
lista.copy() - > másolat készit a listáról
indexelés- > lista[2] iagazából a lista 3. eleme indexrlés 0.tól
indexelés string változóknál, listánál, tömbökknél müködik 
len() lista vagy több hossza
szótárak {"_kulcs-key_":_érték- value_,"_kulcs-key_":"_érték- value_} -> 


szotar= {" elsőelem": 1, "Másodikelem": True, "harmadikelem": "három"}

szotar.items()
szotar.values()
szotar.keys() 

if _feltétel_:
elif _feltétel_:
else:

while_ feltétel_:
előltesztelő ciklus futattás előtt feltétél addig megy amig a feltétel hamis nem lesz
ha while true break szokott lenni
 
for _adott-elem_ in _lista/range/ több_elem:

random
range() -> megadott felső határ nincs benne - > range (0, 10) == [0.....9]
'''

kifli=[]
kakoscsiga=[]
brios=[]

for i in range(0,30):
    kifli.append(random.randint(1,50))
    kakoscsiga.append(random.randint(1,50))
    brios.append(random.randint(1,50))

print("Napi eladások")

print("Nap\tKifli\tKakaóscsiga\tBriós")

for i in range(0,30):

    print(f"{i + 1}. nap\t{kifli[i]}\t{kakoscsiga[i]}\t{brios[i]}")

kszam= 0
kcsszam= 0
bszam= 0
osszes = 0
for i in range(30):
  osszes= osszes + kifli[i]+ kakoscsiga[i]+ brios[i]
  kszam= kszam + kifli[i]
  kcsszam= kcsszam + kakoscsiga[i]
  bszam= bszam + brios[i]

print()

print(f"Összesen {osszes} terméket adtak el a pékségben")
print(f"{kszam} eladott kifli, {kcsszam} eladott kakaóscsiga, {bszam} eladott briós")

kmin= kifli[0]
kmax= kifli[0]
kcsmin= kakoscsiga[0]
kcsmax= kakoscsiga[0]
bmin= brios[0]
bmax= brios[0]

for i in kifli:
    if i < kmin:
        kmin= i
    if i > kmax:
        kmax= i

for i in kakoscsiga:
    if i < kcsmin:
        kcsmin= i
    if i > kcsmax:
        kcsmax= i

for i in brios:
    if i < bmin:
        bmin= i
    if i > bmax:
        bmax= i

print("Kifli")
print(kmin,kmax)
print("kakaóscsiga")
print(kcsmin,kcsmax)
print("Birós")
print(bmin,bmax)
print()

e = 0

while e < len(kifli):
    if kifli[e] == kmax:
        print(f" A legtöbb kakóscsigát elsőnke {e+1}. napon adták el")
        break
    e = e+ 1

e = 0
while e < len(kakoscsiga):
    if kakoscsiga[e] == kcsmax:
        print(f" A legtöbb kakóscsigát elsőnke {e+1}. napon adták el")
        break
    e= e+ 1

e = 0

while e < len(brios):
    if brios[e] == bmax:
        print(f" A legtöbb kakóscsigát elsőnek {e+1}. napon adták el")
        break
    e= e+ 1








