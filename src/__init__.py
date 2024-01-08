# Question 1
a, b, c = 2, 4, 3
print('1 - Quel est le résultat du code suivant :', (a * b) + c)

# Question 2
a = 1
while a < 7:
  a+= 1
print('2 - Quel est le résultat du code suivant :', a)

# Question 3
a = {'A': 1, 'B': 2, 'C': 3}
print('3 - Quel est le résultat du code suivant :', a.values())

# Question 4
print('4 - Pour définir une fonction (function) on utilise : def out lambda')

# Question 5
a = '4*5'
print('5 - Quel est le résultat du code suivant :', a)

# Question 6
class ZZ:
  def __init__(self):
    self.e = 'Hello'
  
  def __init__(self, e):
    self.e = 'Hello'

try:
  zz = ZZ()
  print('6 - Quel est le résultat du code suivant :', zz.e)
except:
  print('6 - Quel est le résultat du code suivant : Erreur de compilation')

# Question 7
resultat = 200
print('7 - Quel est le résultat du code suivant :', type(resultat))

# Question 8
var_a = '26'
var_b = '10'
print('8 - Quel est le résultat du code suivant :', len(var_a + var_b))

# Question 9
try:
  a, b = 5, 0
  print('9 - Quel est le résultat du code suivant :', a / b)
except:
  print('9 - Quel est le résultat du code suivant : Erreur de compilation')
# except ZeroDivisionError:
#   print('9 - Quel est le résultat du code suivant : Division par zero')

# Question 10
a = 12
if (a := 20):
  print('10 - Quel est le résultat du code suivant : a < 20')
if (a == 12):
  print('10 - Quel est le résultat du code suivant : a = 12')

# Question 11
a = 12
variable_6 = {'protide' : 'protéine'}
print('11 - Quel est le résultat du code suivant :', type(variable_6))

# Question 12
print('12 - L\'argument **kwargs dans les définitions de fonctions permet de transmettre : Use liste d\'arguments de longuer variable')

# Question 13
a = 10
def bonjour(a):
  a = 5
  return a
print('13 - Quel est le résultat du code suivant :', a)

# Question 14
a = 13, 4
b = 10
try:
  print('14 - Quel est le résultat du code suivant :', a + b)
except:
  print('14 - Quel est le résultat du code suivant : Erreur de compilation')

# Question 15
a = 3
b = '2'
a = str(a)
print('15 - Quel est le résultat du code suivant :', a + b)

# Question 16
print('16 - Les ensembles sont de structures de données : Modifiable + Non Ordonnée + Non Répétable')

# Question 17
ma_liste = ['protide', 'protéine', 'Covid', 'virus']
print('17 - Quel est le résultat du code suivant :', ma_liste[1:3])

# Question 18
def func(n):
  if n == 0:
    return 1
  else:
    return n * func(n-1)
print('18 - Quel est le résultat du code suivant :', func(3))

# Question 19
print('19 - On peut définir les conditions en utilisant : match + case + ...')

# Question 20
tmp = []
for i in range(1, 3):
  x = i * 2
  tmp.append(str(x))
print('20 - Quel est le résultat du code suivant :', ' '.join(tmp))

# Question 21
class TA:
  a = 'AA'
ta = TA()
print('21 - Quel est le résultat du code suivant :', ta.a)

# Question 22
a = {'A': 1, 'B': 2, 'C': 2}
print('22 - Quel est le résultat du code suivant :', a.values())

# Question 23
print('23 - Pour vider une liste on utilise la méthode : clear()')

# Question 24
print('24 - Pour la gestion des exceptions, on utilise : try + except + else + finally')

# Question 25
a = 'BONJOUR'
print('25 - Quel est le résultat du code suivant :', a[2: 5])

# Question 26
def bonjour(a):
  res = a ** 2
print('26 - Quel est le résultat du code suivant :', bonjour(3))

# Question 27
ma_liste = [1, 2, 3, 4]
f = lambda x : x <= 2
res = map(f, ma_liste)
print('27 - Quel est le résultat du code suivant :', list(res))

# Question 28
class VL:
  def __init__(self, a):
    self.vl.__a = a
try:
  vl = VL(3)
  print('28 - Quel est le résultat du code suivant :', vl.__a)
except:
  print('28 - Quel est le résultat du code suivant : Erreur de compilation')

# Querstion 29
tmp = []
def bonjour():
  a = 5
  tmp.append(str(a))
a = 10
tmp.append(str(a))
bonjour()
print('29 - Quel est le résultat du code suivant :', ' '.join(tmp))

# Querstion 30
tmp = []
a, b, c = 2, 4, 3
print('30 - Quel est le résultat du code suivant :', a * b + c)

# Querstion 31
tmp = []
for i in range(1, 5):
  tmp.append(str(i))
print('31 - Quel est le résultat du code suivant :', ''.join(tmp))

# Querstion 32
print('32 - Pour les modes d\'ouverture d\'un fichier (file), on a : a + r + w')

# Querstion 33
try:
  print('33 - Quel est le résultat du code suivant : Résultat : ', 5 / 0)
except:
  print('33 - Quel est le résultat du code suivant : Erreur')

# Querstion 34
print('34 - Les listes sont des structures de données : Modifiable + ordonnée + Les clés sont not répétable')