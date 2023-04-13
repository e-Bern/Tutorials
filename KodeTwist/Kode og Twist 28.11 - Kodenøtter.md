# Kode og Twist 28.11 - "Kodenøtter"



## Hjelp! _Jeg har aldri brukt Python før_



#### Oppgave 1: Start Jupyter notebooks i prodsonen

###### Steg 1: Logg inn til din "prodsone".

###### Steg 1: Åpne programmet JupyterLab

###### Steg 3: Åpne en Python  Notebook

Serveren kan ta litt tid. Når "launcheren" åpner ser du tre rader: Notebook, Console og Other.

I den første rader, "Notebook", skal du trykke på _Python 3_. 



#### Oppgave 2: Hello, World!

a) Nesten alle kurs om programmering starter med et enkelt program som skriver teksten "Hello, World!" på skjermen. Dette gjør du i Python via funksjonen `Print()`. Nå er det din tur: bruk koden nedenfor til å skrive Hello, World! Husk at du kjører programmet ved å enten trykke "play" knappen _eller_ å holde inn CTRL og ENTER samtidig

```python
print("Hello, World!")

```

b) Print teksten "Hei, SSB!".

c) Print teksten "Mitt navn er ..."



#### Oppgave 3: Pluss og Minus

Nå skal du bruke print til å regne ut enkle mattestykker ved å skrive

```python
print(1+1)
```

eller

```Python
print(1-1)
```

Du skal regne ut:

a) 1+1

b) 1-1

c) 77+33

d) 100 - 22



#### Oppgave 4: Variabler

Noen gang er det nyttig å midlertidig lagre, tall, lister, tekst etc. i variabler. Dette gjøres ved å gi variablene et navn f.eks. var eller variable. Det velger du selv. Navnet sette lik, med et erlik tegn, hva en du ønsker å lagre. Koden ser slik ut:

```python
VARIABLE = "Hello, World!"
```



a) Lag en variable som er lik teksten "Hello, World!" og så `print(variable)`

b) Lag en variable som er lik teksten "Hei, SSB!" og print variablen

c) Variabler kan også brukes til å midlertidig lagre resultatet av et mattestykke. Lag en variable som regner ut _1+1_ så printer du resultatet.



## Lett



#### Oppgave 5: Printing av desimal tall

Følgende kode vil skrive var med to desimal tall

```python
var = 3.1415
print("%.2f" % var)
```

Endre koden slik at var printes med:

a)	0 desimal tall

b)   1 desimal tall

c)    3 desimal tall



#### Oppgave 6: Lister

Du er gitt følgende liste

```python
my_list = [1, 4, 9, 6,6, 7, 2,3]
```

a)  bruk my_list.append() til å legge til tallaene : 5 og 8

b) bruk my_list.remove() til å fjerne tallet: 6

c) sorter my_list

d) kopier listen med koden my_list2 = my_list

d) bruk my_list.pop()  og print listen. Klarer du å se hva pop gjør?

​	HINT: print(my_list2) og sammenlikne resultatet med my_list



#### Oppgave 7: Funksjoner

Funksjoner kan skrives:

```python
def min_funksjon(a,b):
	#Skriv koden din her
	return resultat
```

a) Lag en funksjon som tar inn to tall, a og b, og ganger dem sammen.

b)  Kjør funksjon hvor a= 1 og b= 2

​	HINT: funksjoner kan kjøres via  min_funksjon(a,b)

c) Lag en ny funksjon som deler to tall a og b

d) Kjør funksjonen



## Middels

#### Oppgave 8: Forløkker

Lag et program som tar inn en liste med **floats** av vilkårlig lengde, n.  Finn den største og minste verdien i listen. Print disse to. Ikke bruk innebygdre funksjoner som finne maximum og minimum av lister.

#### Oppgave 9: Fibonacci

Fibonacci sekvensen er en kjent tallsekvens som går som følgene:

```python
1 1 2 3 5 8 13 21 ...
```

Sekvensen begynner med to ett tall, så påfølgende ledd er summen av de to foregående. Lag en funksjon $f(n)$ som gir det $n$-te leddet i fibonacci sekvensen. Dette gjørs ved rekursjon slik at $f(n)$ kaller på $f(n-1)$ og $f(n-2)$,
$$
f(n) = f(n-1)+f(n-2)
$$
Husk: lag en stopp kriterie for rekursjonen når $n<= 2$ hvor da $f(1) = f(2) = 1$.



#### Oppgave 10: En kortstokk

Et normalt spillkort identifiseres ved sin verdi og sort. La et kort representeres som en **tuppel** av verdien og sorten, hvor verdien skal være et heltall mellom 1 og 13, og bokstaven **H** for hjerter, **K** for kløver, **R** for ruter, og  **S** for spar. Slik at (12, 'K') vil representere dronningen av kløver.

a) Bruk _nested loops_ og lag en liste som inneholder en normal kortstokk.

b) Bruk `random.shuffle` til blande kortstokken.

c) Etter å ha blandet kortstokken trekk ut 13 kort.

d) Sorter og print kortene du har trykket ut av kortstokken slik at de er separert etter sort og rangert etter verdi.



#### Oppgave 10: Tell tegnene

Skriv en funksjon tell_tegn som tar inn en streng som input, og teller antall ganger hvert tegn vises i strengen. Bokstav størrelse skal ignoreres slik at A og a telles som samme bokstav. Funksjonen skal returnere de telte tegnene som en dictionary.

Test funksjonen din ved å bruke følgende test blokk:

```python
eksempel = "Hello, World!"
for tegn, tell in tell_tegn(eksempel).items():
    print(f'{tegn:3}{tell:10}')
```

Bruk print eksempelt  som hint og print tegne slik at de er listet i alfabetisk rekkefølge. Til slutt, print tegnene slik at de er rangert etter hvor mange ganger de er brukt.



## Avansert

#### Oppgave 11: Maksimer

Du er gitt en funksjon $f(X) = X^2$. I tillegg får du utdelt en liste med elementer. Du må velge ett element fra hver liste slik at verdien fra ligningen nedenfor maksimeres:
$$
S = (f(X_1) + f(X_2) + \cdots + f(X_k))\%M
$$

- $X_i$ er element valgt fra $i$ liste. 
- $\%$ står for modulo, **ikke** deling.

Oppgaven er å finne verdien til $S_{max}$. Merk at du kan kun velge et element fra hver liste. 

**Input format:** 

Første linje inneholde 2 separert int **K** og **M**.

De neste **K** linjene inneholde en int $N_i$ som beskriver antall elementer $i$-te listen etterfulgt av $N_i$ separerte ints som er elementene i listen. 

**Test input**

```python
3 1000
2 5 4
3 7 8 9
5 5 7 8 9 10
```

**Test output**

```python
206
```





## Slem oppgave

##### IKKE begynn på denne oppgaven dersom du ikke er komfortable med å sjekke om din versjon av Jupyter har tilgang på en .jit compiler eller sette én opp.



#### Oppgave: Optimalisering

Koden nedenfor (også sendt ut) lager et mandelbrot set. Det trenger du ikke vite hva er. Tenk komplisert bilde. Koden er naivt implementert i python og tar min Jupyter på dapla **2 min 15s**. Din oppgave er å få koden raskere, uten å bruke C/C++/Cython eller andre lavere nivå språk direkte. 



**NB!**  min løsning i dapla tok $1.82 s \pm 10.1 ms$



```python
import numpy as np
import matplotlib.pyplot as plt

def mandelbrot_pixel(c, maxiter):
    """Check wether a single pixel diverges"""
    z = 0

    for n in range(maxiter):
        z = z*z + c
        if abs(z) > 2:
            return n

    return 0

def mandelbrot_image(xmin, xmax, ymin, ymax, width, height, maxiter):
    """Render an image of the Mandelbrot set"""
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    img = np.empty((width, height))

    for i, xi in enumerate(x):
        for j, yj in enumerate(y):
            c = xi + 1j*yj
            img[i, j] = mandelbrot_pixel(c, maxiter)

    return img

def benchmark(mandelbrot):
    xmin = -0.74877
    xmax = -0.74872
    ymin = 0.065053
    ymax = 0.065103
    pixels = 1000
    maxiter = 2048
    return mandelbrot(xmin, xmax, ymin, ymax, pixels, pixels, maxiter)

```









