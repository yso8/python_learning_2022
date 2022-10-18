#region Apprentissage : Découverte du langage, variables 

#------------------------------
#Print hello world dans la console. 
#------------------------------

print("hello world")

#------------------------------
#Si le nombre cinq est supérieur à deux alors je print 'pourquoi' dans la console.
#------------------------------

if 5>2:
    print("pourquoi?")

#------------------------------
#Print le type de valeur orchestré.
#------------------------------

x=str(5)
y=int(5)
z=float(5)
print(type(x),type(y),type(z))

#------------------------------
#Retourne une chaîne fondé à partir de deux variables différentes.
#------------------------------

a="Baptiste"
b='Voilà'
print(b, a)

#------------------------------
#Utilisation d'une liste de fruits, assignation des variables.
#------------------------------

Fruits = ["Banane", "Pomme", "Poire"]
x, y, z = Fruits
print(x, y, z)

#------------------------------
#Appel d'une variable externe à la fonction.
#------------------------------

x = 'Génial'
def fctPythonStatut():
   print("Python est " + x)

fctPythonStatut()

#------------------------------
#Les différents types de données. 
#------------------------------

# str = chaîne 
# numeric = int, float, complex
# x = 5 #int
# y=4.6 #float
# z=1j #complex
# print(type(x), type(y), type(z))
# sequences = list, tuple, range
# d=["fruits", "légumes"] #list 
# e=("fruits", "légumes") #tuple
# f=range(6) #range
# mapping = dict
# set types = set, frozenset
# bool = bool
# binary = bytes, bytearray, memoryview
# none type = nonetype

#------------------------------
#Conversion des données dans d'autres types de donnéees. 
#------------------------------

x=1
y=3.5
z=1j

a=float(x)
b=int(y)
c=complex(x)

print(a, b, c)

#------------------------------
#Retranscrit la chaîne de caractère telle qu'elle est crée.
#------------------------------

a = '''Salut j'aime beaucoup les noisettes,
et également aller les cueillir directement sur l'arbre'''
print(a)

#------------------------------
#Print un caractère car un string n'est autre qu'un tableau de caractère. 
#------------------------------

a="Hello, comment ça va?"
print(a[3])

#------------------------------
#Print le nombre de caractère d'une chaîne, comprennant la ponctuation et les espaces. 
#------------------------------

a="Hello, comment ça va?"
print(len(a))

#------------------------------
#Retourne un bool indiquant si le(s) caractère(s) indiqué(s) sont dans le string passé.
#------------------------------

a="Hello, comment ça va?"
print("Hello" in a)

#------------------------------
#Print un string indiquant si le(s) caractère(s) indiqué(s) sont dans le string passé.
#------------------------------

a="Hello, ça va? Moi ça va plutôt bien!"
if "ça" in a:
   print("Présent")
else:
   print("Non présent")

#------------------------------
#Print un string en utilisant les fonctions lower/upper/strip/replace.
#------------------------------

a="Hello"
print(a.upper()) #permet de mettre la chaîne en majuscules.

b="Hello"
print(b.lower()) #permet de mettre la chaîne en minuscules.

c=" Bonjour comment ça va? " 
print(c.strip()) #permet de supprimer les espaces avant/après.

d="Bonjour! Tu est très jolie"
print(d.replace("j", "d")) #permet de remplacer un/des caractère(s) par d'autre(s) caractère(s).

e="Bonjour belle journée à vous!"
print(e.split()) #permet de séparer tout les mots de la chaîne de caractères.

#------------------------------
#Print un string concaténer avec une ou plusieurs variables.
#------------------------------

age=32
age2=5
age3=age+age2
txt="Voici mon âge " + str(age) #concatène la chaîne de valeur avec une variable integer.
print(txt) 

txt="J'ai {} ans, dans {} ans j'aurais {} ans" #rempli le string avec l'ordre des variables en paramètres.
print(txt.format(age, age2, age3)) 
 
txt="J'ai {0} ans, dans {1} ans j'aurais {2} ans" #rempli le string avec les variables dans l'ordre des index. 
print(txt.format(age, age2, age3)) 

#------------------------------
#Print une occurence indiquant ou est le mot recherché.
#------------------------------

a="Bonjour, voici un exemple de phrase, et encore un exemple"
print(a.find("exemple"))

#------------------------------
#Print des opérations booléennes et tout types de test 0 ou 1.
#------------------------------

a=200
b=200

if b>a:
    print("la variable b est plus grande que la variable a")
else :
    print("la variable b n'est pas plus grande que la variable a")

print(bool("Hello"))
print(bool("15"))

x=""
y=0
print(bool(x))
print(bool(y))
 
maListe = ["Pierre", "Julien", "Anne", "Marie", "Lucien"]
print(len(maListe))
print(type(maListe))
print(maListe[1])
print(maListe[1:4])

#------------------------------
#Utilisation des listes et toutes ses fonctionnalités. 
#------------------------------

if "Julien" in maListe:
    print("Julien est bel et bien présent dans la liste.")

maListe = list(("Pierre", "Julien", "Anne", "Marie", "Lucien"))
print(maListe)

maliste1 = ["Anne", "Marie", "Julien"]
maliste2 = ["Pierre", "Lucien"]
maliste1.extend(maliste2) #permet d'étendre une liste avec une autre, les fusionnants 
maliste1.remove(maliste1[1]) #permet de remove l'index numéro un de la liste 
maliste1.remove() #permet de remove si l'objet est bien indiqué en paramètre
maliste1.pop(1) #permet d'enlever le premier objet de la liste 
print(maliste1)

maliste1 = ["Anne", "Marie", "Julien"]
for x in maliste1:  #permet de print chaque élément de la liste
    print(x)

maliste1 = ["Anne", "Marie", "Julien"]
for x in range(len(maliste1)): #permet de print chaque élément de la liste, de façon + procédurale + compliqué
    print(maliste1[x])
    
maliste1 = ["Anne", "Marie", "Julien"]
x=0
while x<len(maliste1):
    print(maliste1[x])
    x=x+1

maliste1 = ["Anne", "Marie", "Julien"]
[print(x) for x in maliste1]

fruits = ["Banane", "Pomme", "Kiwi", "Mangue"]
nouvelleliste = []
for x in fruits:
    if "a" in x:
        nouvelleliste.append(x)
print(nouvelleliste) #Récupère tout les fruits et les mets dans la liste.

fruits = ["Banane", "Pomme", "Kiwi", "Mangue"] 
nouvelleliste = [x for x in fruits if "a" in x] 
print(nouvelleliste) #Récupère tout les fruits et les mets dansla liste dans le cas ou il contient un 'a'

fruits = ["Banane", "Pomme", "Kiwi", "Mangue"]
nouvelleliste = [x for x in fruits if x != "Banane"] 
print(nouvelleliste) #Récupère tout les fruits et les mets dans la liste dans le cas ou ce n'est pas une banane

nouvelleliste = [x for x in range(20) if x<10] 
print(nouvelleliste)

fruits = ["Banane", "Pomme", "Kiwi", "Mangue"]
nouvelleliste = [x.upper() for x in fruits] 
print(nouvelleliste) #Récupère tout les fruits et les mets en majuscule dans la liste

#endregion
 
#region Exercice 1 : Bonne initialisation de variable 

#prenom="Pierre"
#majeur=True
#banque=20135,384
#amis= ["Marie", "Julien","Adrien"]
#parents=("Marc","Caroline")

#endregion

#region Exercice 2 : Bonne conversion du integer pour pouvoir le print en chaîne

#nombre=15
#print("Le nombre est " + str(nombre))

#Solution alternative
#print("Le nombre est ", nombre)

#Solution alternative 2
#print(f"Le nombre est {nombre}")

#endregion 

#region Exercice 3 : Ajouter un séparateur dans la fonction sprint

#a=2
#b=6
#c=3
#print(f"{a} + {b} + {c}")

#Solution alternative
#print(a, b, c, sep=" + ")

#endregion 

#region Exercice 4 : Erreur dans la déclaration d'une variable 

#list = range(3)
#list2 = range(5)

#print(list(list2))

#endregion 

#region Exercice 5 : Créez une fonction pour vérifier si une variable contient du texte ou non

def verif(x):
    if isinstance(x, str):
        print(True)
    else:
        print(False)

var = "Coucou"
print(verif(var))
var=0
print(verif(var))

#endregion 

#region Exercice 6 : Formatter un texte avec des variables externe

h = 8
m = 54
temps = "Pluie"
txt = "Il est {2}h{0}, et la météo est : {1}."
print(txt.format(m,temps,h))

#endregion 

#region Exercice 7 : Vérifier si une variable est d'un certain type

#var = "Pierre"
#if type(var) is str : 
#    print("La variable est une chaîne de valeur")
#    var = 0

#if isinstance(var, int):
#    print("La variable est un entier")

#Solution alternative
#def checkIfItemIsString(item) :
#    if isinstance(item, str):
#        print(item + " is a string.")

#var1 = 'Pierre';
#checkIfItemIsString(var1);
#var1 = 0;
#checkIfItemIsString(var1);

#endregion

#region Exercice 8 : Remplacer un mot par un autre 

# phrase = "Bonjour tout le monde"
# print(phrase.replace("Bonjour", "Bonsoir", 1))

#endregion 

#region Exercice 9 : Ordonner une chaine de caractère 

# var = "Pierre, Julien, Anne, Marie, Lucien"
# newVar = var.split(", ")
# newVar.sort()
# string = ", ".join(newVar)
# print(string)

#endregion 

#region Exercice 10 : Calcul de sphère 

# import math
# def calculSphere(rayon):
#     res = ((4*math.pi)/3)*(rayon**3)
#     return ("Le volume est de", "%.2f"% res)
# print(calculSphere(10))

#endregion

#region Exercice 11 : Tester si un nombre est plus grand que 10

# def plusGrandQueDix(z):
#     if z>10:
#         return "Z > 10"
#     elif z == 10:
#         return "Z = 10"
#     else: 
#         return "Z < 10"

#endregion 

#region Exercice 12 : Créer une liste de nombres de 5 à 15

def list(num, numBis):
    numList = []
    while(num <= numBis):
        numList.append(num)
        num += 1
    return numList

num=5
numBis=15
print(list(num, numBis))

#endregion