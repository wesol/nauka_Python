# -*- coding: utf-8  -*-

'''
#p9
a= 12
print(type(a))
a='w'
print(type(a))
a=1+1j
print(type(a))
a=None
print(a)
del(a)
#print(a)

#p12
comp = (2+5j)+(4+6j)
print(comp)

comp = 4-(4+6j)
print(comp)

#p14/15
#PRAWIE SKONCZONE WORCIC JAK BEDE WIDZIAL JAK POLACZYĆ LISTE JEDNA LICZBE W WYRAZ 
#def conv_10to8(liczba):
          #list_conv=[]
          #while liczba > 0:
                    #reszta = liczba % 8
                    #liczba = int(liczba/8)
                    #list_conv.append(reszta)
          #list_conv.reverse()
          #return list_conv

#osemkowa = conv_10to8(100)
#print(osemkowa) 
liczba= int(input('Wprowadź liczbę: '))
print(bin(liczba))
print(hex(liczba))
print(oct(liczba))
print(liczba)

#p16
print(bool( 7))
#P17 
#wszytkie puste badź równe '0' dają false: 0, None, '', "", [], {}, ()
print(bool( '      ')) #to co ciekawe, daje True

#P18
print('s '*3)  

#P19
print(type(int('8')))

#P20
print(type(str(8)))


#P21
im1 = 'Gniewomir'
im2 = 'Łukasz'
im3 = 'Bożydar'
print(im1,im2,im3)

#P24
a = 2
polekw = pow(a,2)
print(polekw)

a = 2
b = 3
c = 4
p = 0.5*(a+b+c)
poletroj = pow(p*(p-a)*(p-b)*(p-c),0.5)
print(round(poletroj,3))

r = 3
polekola = 3.14 * r**2
print(polekola)


#P25
ilH = 168
pensjaN = 5500
pensjaB = pensjaN * 1.23

print('stawka h netto:', round(pensjaN/ilH,2),'zł', '\nstawka h brutto:',round(pensjaB/ilH,2), 'zł')

#P26 prawo de morgana
p=False
q=False

if not(p and q) ==  (not p) or (not q):
          print('true')

#P28
im = 1j
multi = 17**0.5

liczba = multi * im
print(liczba)

#P29
z  = 17%7
z *= z+3
print(z)

#P30
print((str(1.2e+3+34.5)+"; ")*19+str(1.2e+3+34.5))

#P32
napis1 = input('Podaj tekst: ')
napis2 = input('Podaj tekst: ')

if napis1 > napis2:
          print(napis1)
elif napis1 < napis2:
          print(napis2)
else:
          print('podano 2 takie same wyrazy')

#P34 
print('trzy\\trzy')
print('trzy\'trzy')
print('trzy\"ntrzy')
print('trzy\antrzy')
print('trzy\bsntrzy')
print('trzy\fntrzy')
print('trzy\vtrzy')

#P35 
imie = input('Podaj imię: ')
print('Witaj '+ imie.capitalize())


#P36
imie = input('Podaj imię: ')
print((imie.capitalize()+'\n')*30)



#P37
while True:
          try:
                    podstawa = float(input('Podaj długość podstawy: '))
                    if podstawa > 0:
                              break
                    else:
                              print('Długość musi być większa niż 0')
                              continue
          except:
                    print('Nie wprowadzono liczby!')
                    continue

while True:
          try:
                    wysokosc = float(input('Podaj wysokość: '))
                    if wysokosc > 0:
                              break
                    else:
                              print('Wysokość musi być większa niż 0')
                              continue
          except:
                    print('Nie wprowadzono liczby!')
                    continue

print('Pole trójkąta wynosi:',podstawa*wysokosc*0.5)  
      

#-- -------------------------------
#Testujemy listy
lista = ['a1','b2','c3','d4','e5','f6','g7']

lista2 = lista[2::2]
print(lista2)

lista2 = lista[:2]
print(lista2)

lista2 = lista[::2]
print(lista2)
lista2 *= 2
print(lista2)

lista2 += '22'
lista2.append( '22')
print(lista2)
del lista2[]
print(lista2)

lista1 = ['a1','b2','c3','d4','e5','f6','g7']
lista2 = ['a1','b2','c3','d4','e5','f6','g7']

print(lista1[1] < lista2[2] )
print( 'a1' in lista1)
print( 'a1' not in  lista1)0
 
#P39
imiona = ['Iwonka', 'Ela', 'Ewa']
liczby  = [1,2,3]

imiona.append('Adam')
imiona.append('Ewa')
liczby.append(4)
liczby.append(5)
print(imiona)
print(liczby)

#P40
imiona = ['Iwonka', 'Ela', 'Ewa']
imie = imiona[1]
print(imie)


#P41
art = ['mąka', 'cukier', 'sol', 'cukierki', 'pieprz']
l = len(art)-1
print(art[0]+'\n'+art[l])
#print(art[0][len(art)-1])

#P42
krotki = ('Witaj', 'w', 'kursie', 'Python')
for i in krotki:
          print(i, end =' ..l.> ')

#P43
krotka = ('01','01','2018')
data = ('01','02','2013')
print('Data ważności artykulu: '+ data[0]+'-'+data[1]+'-'+data[2])
prod = ('a',krotka,'b',krotka,'c',krotka)

print(prod)
print('Data ważności artykulu: \n' + prod[0]+':', prod[1][0]+'-'+prod[1][1]+'-'+prod[1][2])

#P44
licz_opisowe ={'jeden':1, 'dwa':2, 'trzy':3, 'cztery':4, 'pięć':5}
while True:
          napis = (input('Wprowadź liczbę całkowitą z zakresu jeden - pięć słownie: '))
          if napis in licz_opisowe:
                    break
          else: 
                    print('Wprowadzono liczbę spoza zakresu')
                    continue
print(licz_opisowe[napis])

#P45
conv ={1 : 'I', 2 : 'II', 3 : 'III', 4 : 'IV', 5 : 'V', 6 : 'VI', 7 : 'VII', 8 : 'VIII', 9 : 'IX', 10 : 'X'}
while True:
          try:
                    liczba = int(input('Wprowadź liczbę całkowitą z zakresu 1 - 10: '))
                    if liczba in conv.keys():
                              break
                    else: 
                              print('Wprowadzono liczbę spoza zakresu')
                    continue
          except:
                    print('Wprowadzono niepoprawną wartość')
                    continue

print(conv[liczba])          


#P46
licz_opisowe ={1:'jeden', 2:'dwa', 3:'trzy', 4:'cztery', 5:'pięć'}
while True:
          try:
                    liczba = int(input('Wprowadź liczbę całkowitą z zakresu 1 - 5: '))
                    if liczba in range (1,6):
                              break
                    else: 
                              print('Wprowadzono liczbę spoza zakresu')
                              continue
          except:
                    print('Wprowadzono niepoprawną wartość')
                    continue
          
print(licz_opisowe[liczba])

conv ={1 : 'I', 2 : 'II', 3 : 'III', 4 : 'IV', 5 : 'V', 6 : 'VI', 7 : 'VII', 8 : 'VIII', 9 : 'IX', 10 : 'X'}
#I:1
#II:2
#III:3
#IV:4
#V:5
#VI:6
#VII:7
#VIII:8
#IX:9
#X:10
#XX:20
#XXX:30
#XL:40
#L:50
#LX:60
#LXX:70
#LXXX:80
#XC:90
#C:100
#CC:200
#CCC:300
#CD:400
#D:500
#DC:600
#DCC:700
#DCCC:800
#CM:900
#M:1000
#MD:1500
#MM:2000

#P47
#list_roman = ['I','V','X','L','C','D','M']
#conv_roman_10={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

#roman = (input('Wprowadź liczbę rzymską ')).upper()

#sprawdzenie czy to jest wogóle liczba rzymska

#roman_check = list(roman)

#for i in roman_check:
          #print(roman_check[i])
          #if roman_check[i] in conv_roman_10:
                    #print('true')
          #else:
                    #print('false')
                    

#try:
                    #roman = (input('Wprowadź liczbę rzymską '))
                    #if liczba in conv_roman_10():
                              #break
                    #else: 
                              #print('Wprowadzono liczbę spoza zakresu')
                    #continue
          #except:
                    #print('Wprowadzono niepoprawną wartość')
                    #continue

#print(roman)
#print(roman_check)  

#P48
slownik={}
slownik['nazwa']='telewizor'
slownik['ilosc']=int(input('podaj ilość: '))
slownik['cena_netto_poj']=1700.25
slownik['cena_brutto_poj']=round(slownik['cena_netto_poj']*1.23,2)
slownik['cena_netto']=round(slownik['cena_netto_poj']*slownik['ilosc'],2)
slownik['cena_brutto']=round(slownik['cena_netto']*1.23,2)
print(slownik)

#P49
from random import randint
lotto =set()
while len(lotto) <6:
          los = randint(1,50)
          lotto.add(los)
print('wylosowane liczby to:',sorted(lotto))

#P50
a = list(range(2,99,2))
print(a)

#P51
punkty = []

for y in range(0,11):
          punkty.append(('p'+str(y+1),2*y,y))
print(punkty)


#P52
plansza = []
czarne = []
biale = []
puste = []

for i in range(0,8):
        czarne.append('czarne')
        biale.append('biale')
        puste.append('puste')

for i in range(0,2):
        plansza.append(czarne)
for i in range(2,6):
        plansza.append(puste)
for i in range(6,8):
        plansza.append(biale)
          
          
for v in range(0,8):
        print(plansza[v])
print(plansza[0][1])

#P53
for i in range(0,5):
          if bool(i) == True:
                    print('bool(',i,')', '= True')
          else:
                    print('bool(',i,')', '= False')
for i in range(0,5):
          if i == True:
                    print(i, '= True')
          else:
                    print(i, '= False')

#P54
a = float(input('wprowadź liczbę: '))
if a >=0 and a <=9:
          print('ok')
else:
          print('out of range')

#P55
a = float(input('wprowadź liczbę: '))
b = [1,2,3]

if a == b[0] or a == b[1] and a > 0:
          print('ok')
else:
          print('out of range')

#P56
a = int(input('wprowadź liczbę całk.: '))
print('parzysta') if a % 2 == 0 else print('nieparzysta')

#formatowanie liczb

for x in range(5,100,10):   
          print("%-40.3f%-60i%8i" % (x,x**2,x**3))

liczby = [1,2,2,2,3,4,5]
szukana = 2
for p,x in enumerate(liczby):      
          if x != szukana:  
                    continue      
          print("Znaleziono liczbę %i na pozycji %i" % (x,p+1)) 
          break  
else:      
          print("Liczby %i nie ma na liście" % szukana)
       
#P57
sklep_prod = {'mąka': 17.20, 'chleb': 20}
prod = 'mąka'

for i, x in enumerate(sklep_prod):
          if prod == x:
                    print('%s kosztuje %2.2f zł' % (x, sklep_prod[x]))
                    break
else:
          print('nie ma takiego produktu')

#P58/59
sklep_prod = {"12":"mysz Logitech","13":"monitor HP 15\'","14":"klawiatura Logitech"}
sklep_cena = {"12":100.50,"13": 1500,"14":250.15}
sklep_stan = {"12":15,"13":10,"14":7}
zamowienie = []
suma = 0
while(True):
          print("Produkty:")
          for k in sklep_prod:
                    print(('%-10s | %-15s | cena: %-2.2f zł | ilość: %-2i szt') % (k, sklep_prod[k], sklep_cena[k], sklep_stan[k]))

          choice = input("\nPodaj kod produktu: (Q)-wyjscie: ")
          if(choice in sklep_prod.keys()):
                    ilosc = int(input("Ile zamawiasz szt: "))
                    if(ilosc > sklep_stan[choice]):
                              print("Brak towaru na stanie!")
                    else:
                              zamowienie.append(str(sklep_prod[choice])+" "+str(ilosc)+" "+str(sklep_cena[choice]*ilosc))
                              sklep_stan[choice] -= ilosc
                              suma += sklep_cena[choice]*ilosc            
          elif(choice.upper() == "Q"):
                    break
          else:
                    print("Nie ma takiego produktu na liście!")

print("Do zapłaty: %6.2f zł" % (suma))
for v in zamowienie:
          print(v)

#P60
liczby = {'0':'zero','1':'jeden', '2':'dwa', '3':'trzy', '4':'cztery', '5':'pięć', '6':'sześć', '7':'siedem', '8':'osiem', '9':'dziewięć'}

while True:
          ciag = input('Podaj ciąg cyfr: ')
          if ciag.isdigit():
                    break
          else:
                    print('coś pomyliłeś\n', end = ' ')

for i in ciag:
          print(liczby[i], end=' ')
         
n = 'kjkjfksa'
for i,p in enumerate(n):
          print(i, p)
for i in (n):
          print(i)    

#P61
for i in range(1,11):
          for x in range(1,11):
                    print (i*x, end='\t')
          print()

#P62
for i in range(3,10):
          print(("kwadrat liczby: %i to %i ") % (i,pow(i,2)))

#P63
for i in range(1,10,2):
          print(("kwadrat liczby: %i to %i ") % (10-i,pow(10-i,2)))
       
#P64
liczby = [1,2,2,2,3,4,5]
print(liczby.index(3)+1)

#P66
z = lambda:  print('nie ma takiej oceny')
          
listaO = [2,2.5,3,3.5,4,4.5,5]
i = 0
su = 0
wpr = []

while True:
          o = input('wprowadź ocenę, jeśli chcesz zakończyć wciśnij enter: ')
          if o != '':
                    try:
                              o = float(o)
                              if o in listaO:
                                        i += 1
                                        wpr.append(o)
                              else: 
                                        z()
                    except:
                              z()
          else:
                    if i == 0:
                              print('nie zostały wprowadzone żadne liczby')
                              break
                    else:
                              print('wprowadzone oceny:',wpr,'średnia podanych ocen to:',round(sum(wpr)/i,2))
                              break
 
#P69
def silnia(n):
          c = 1
          for i in range(1, n+1):
                    c *= i
          return c

print(silnia(4))

def silnia2(n):
          if n == 1:
                    return 1
          else:
                    return n*silnia2(n-1)
print( silnia2(4))
#P70
def Fib(n):
          ciag = [0,1]
          for i in range (2,n+1):
                    ciag.append(ciag[i-2]+ciag[i-1])
          print (n,'-i/y wyraz ciągu Fibonnaciego to:', str(ciag[n])+'.\nSuma wyrazów ciągu Fibonnaciego do', n, '-o wyrazu ciągu wynosi:', sum(ciag))
Fib(2)

#P72
def odl(x1,y1,x2,y2):
          return ((x2-x1)**2+(y2-y1)**2)**0.5
print(odl(1,1,2,2))

#alternatywa wywoływania
p1 = (1,1)
p2 = (2,2)
print(odl(p1[0], p1[1],p2[0], p2[1]))
print(odl(*p1,*p2))
'''
#P73