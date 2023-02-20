#Second Cours du 21 Octobre 2022 avec M. Artz Vincent

#region Apprentissage : Découverte du langage, liste et tuple

#------------------------------
#Tri une liste de fruits par ordre alphabétique.
#------------------------------

# laliste = ["Pomme", "Abricot", "Poire", "Banane"]
# laliste.sort() #Tri la liste par ordre alphabétique
# print(laliste)

#------------------------------
#Tri une liste de nombres par ordre croissant.
#------------------------------

# laliste = [1, 62, 3, 94, 5, 66, 74, 28, 9, 10]
# laliste.sort() #Tri la liste par ordre croissant
# print(laliste)

#------------------------------
#Tri une liste de nombres par ordre décroissant.
#------------------------------

# laliste = [1, 62, 3, 94, 5, 66, 74, 28, 9, 10]
# laliste.sort(reverse=True) #Tri la liste par ordre décroissant
# print(laliste)

#------------------------------
#Tri une liste de nombres par rapport à sa différence avec un nombre donné. (valeur absolue)) 
#------------------------------

# def myfunc(x):
#     return abs(x-50) #Retourne la valeur absolue de x-50

# laliste = [100, 50, 65, 82, 23]
# laliste.sort(key=myfunc) #Tri la liste par ordre croissant en fonction de la fonction myfunc
# print(laliste)

#------------------------------
#Copie une liste dans une autre liste.
#------------------------------

# laliste = [100, 50, 65, 82, 23]
# lalistecopy = laliste.copy() #Copie la liste laliste2 dans lalistecopy
# print(lalistecopy)

#------------------------------
#Concaténation de deux listes. 
#------------------------------

# liste1 = ["x", "y", "z"]
# liste2 = [1, 2, 3]
# liste3 = liste1 + liste2 #Concatène les deux listes
# print(liste3)

# liste1 = ["x", "y", "z"]
# liste2 = [1, 2, 3]
# liste1.extend(liste2) #Concatène les deux listes
# print(liste1)

#------------------------------
#Ajoute les éléments d'une liste dans une autre liste.
#------------------------------

# liste1 = ["x", "y", "z"]
# liste2 = [1, 2, 3]
# for x in liste2:
#     liste1.append(x) #Ajoute les éléments de la liste2 à la liste1
# print(liste1)

#------------------------------
#Vide une liste. 
#------------------------------

# liste1 = ["x", "y", "z"]
# liste1.clear() #Vide la liste1
# print(liste1)

#------------------------------
#Affiche le type de données d'une liste et sa longueur. 
#------------------------------

# montuple = ("Pomme", "Abricot", "Poire", "Banane") #Tuple
# print(montuple) #Affiche le tuple
# print(type(montuple)) #Affiche le type de la variable montuple
# print(len(montuple)) #Affiche la longueur du tuple

#------------------------------
#Affiche le type de données d'un tuple dans le cas ou il est bien instancié.
#------------------------------

# #Créer un tuple avec un objet
# monobjet = ("Pomme",) #Si on ne met pas la virgule, Python ne reconnaîtra pas le tuple comme tel
# print(type(monobjet)) #Affiche le type de la variable monobjet

#------------------------------
#Affiche le type de données d'un tuple dans le cas ou il est mal instancié.
#------------------------------

# #Créer un objet sans tuple
# monobjet = ("Pomme") #Si on ne met pas la virgule, Python ne reconnaîtra pas le tuple comme tel
# print(type(monobjet)) #Affiche le type de la variable monobjet

#------------------------------
#Affiche les éléments d'un tuple dans un intervalle d'index ou pour un index donné.
#------------------------------

# montuple = ("Pomme", "Abricot", "Poire", "Banane") #Tuple
# print(montuple[1]) #Affiche l'élément à l'index 1 du tuple
# print(montuple[-1]) #Affiche l'élément à l'index -1 du tuple

# montuple = ("Pomme", "Abricot", "Poire", "Banane", "Citron", "Fraise", "Melon") #Tuple
# print(montuple[2:5]) #Affiche les éléments à partir de l'index 2 jusqu'à l'index 5 du tuple

# montuple = ("Pomme", "Abricot", "Poire", "Banane", "Citron", "Fraise", "Melon") #Tuple
# print(montuple[:4]) #Affiche les éléments à partir de l'index 0 jusqu'à l'index 4 du tuple

# montuple = ("Pomme", "Abricot", "Poire", "Banane", "Citron", "Fraise", "Melon") #Tuple
# print(montuple[2:]) #Affiche les éléments à partir de l'index 2 jusqu'à la fin du tuple

# montuple = ("Pomme", "Abricot", "Poire", "Banane", "Citron", "Fraise", "Melon") #Tuple
# print(montuple[-4:-1]) #Affiche les éléments à partir de l'index -4 jusqu'à l'index -1 du tuple

#------------------------------
#Vérifie si un élément est présent dans un tuple.
#------------------------------

# montuple = ("Pomme", "Abricot", "Poire", "Banane", "Citron", "Fraise", "Melon") #Tuple
# if "Melon" in montuple: #Vérifie si l'élément est dans le tuple
#     print("Oui, 'Melon' est dans le tuple")

#------------------------------
#Modifie un tuple en le convertissant en liste, en modifiant l'élément à l'index donné.
#------------------------------

# montuple = ("Pomme", "Abricot", "Poire", "Banane", "Citron", "Fraise", "Melon") #Tuple
# unelist = list(montuple) #Copie le tuple dans la liste
# unelist[6] = "Pêche" #Modifie l'élément à l'index 1 de la liste
# print(unelist) #Affiche la liste

#------------------------------
#Ajoute un élément à un tuple en le convertissant en liste. 
#------------------------------

# montuple = ("Pomme", "Abricot", "Poire", "Banane", "Citron", "Fraise", "Melon") #Tuple
# unelist = list(montuple) #Copie le tuple dans la liste
# unelist.append("Pêche") #Ajoute l'élément à la fin de la liste
# print(unelist) #Affiche la liste

#------------------------------
#Concatènation de deux tuples.
#------------------------------

# montuple = ("Pomme", "Abricot", "Poire", "Banane", "Citron", "Fraise", "Melon") #Tuple
# montuple2 = ("Pêche", "Kiwi", "Ananas") #Tuple
# montuple += montuple2 #Concatène les deux tuples
# print(montuple) #Affiche le tuple

# montuple = ("Pomme", "Abricot", "Poire", "Banane", "Citron", "Fraise", "Melon") #Tuple
# montuple2 = ("Pêche", "Kiwi", "Ananas") #Tuple
# montuple3 = montuple + montuple2 #Concatène les deux tuples
# print(montuple3) #Affiche le tuple

#------------------------------
#Modifie un tuple en le convertissant en liste, en supprimant l'élément à l'index donné.
#------------------------------

# montuple = ("Pomme", "Abricot", "Poire", "Banane", "Citron", "Fraise", "Melon") #Tuple
# maliste = list(montuple) #Copie le tuple dans la liste
# maliste.remove("Melon") #Supprime l'élément "Melon" de la liste
# montuple = tuple(maliste) #Copie la liste dans le tuple
# print(montuple) #Affiche le tuple

#------------------------------
#Supprime un élément d'un tuple et essaye de le donné.
#------------------------------

# montuple = ("Pomme", "Abricot", "Poire", "Banane", "Citron", "Fraise", "Melon") #Tuple
# del montuple #Supprime le tuple
# try:
#     print(montuple) #Affiche le tuple
# except:
#     print("Le tuple n'existe plus") #Affiche le message d'erreur

#------------------------------
#Décompose les éléments d'un tuple dans des variables. 
#------------------------------

# montuple = ("Pomme", "Abricot", "Poire", "Banane", "Citron", "Fraise", "Melon") #Tuple
# (a, b, c, d, e, f, g) = montuple #Décompose le tuple dans les variables
# print(a, b, c, d, e, f, g) #Affiche les variables

#------------------------------
#Décompose les éléments d'un tuple dans des variables et une liste reprennant tout les autres éléments. (*c) 
#------------------------------

# montuple = ("Pomme", "Abricot", "Poire", "Banane", "Citron", "Fraise", "Melon") #Tuple
# (a, b, *c) = montuple #Décompose le tuple dans les variables
# print(a, b, c) #Affiche les variables

#------------------------------
#Parcourt le tuple et affiche tout les élements un par un.  
#------------------------------

# montuple = ("Pomme", "Abricot", "Poire", "Banane", "Citron", "Fraise", "Melon") #Tuple
# for x in montuple: #Parcourt le tuple
#     print(x) #Affiche l'élément du tuple

# montuple = ("Pomme", "Abricot", "Poire", "Banane", "Citron", "Fraise", "Melon") #Tuple
# for x in range(len(montuple)): #Parcourt le tuple
#     print(montuple[x]) #Affiche l'élément du tuple

# montuple = ("Pomme", "Abricot", "Poire", "Banane", "Citron", "Fraise", "Melon") #Tuple
# i = 0 #Initialise la variable i
# while i < len(montuple): #Tant que i est inférieur à la longueur du tuple
#     i += 1 #Incrémente la variable i
#     print(montuple[i]) #Affiche l'élément du tuple

#------------------------------
#Concatène deux tuples, même si les types de données sont différentes, et répéte un tuple plusieurs fois avec le symbole *.
#------------------------------

# montuple = ("Pomme", "Abricot", "Poire") #Tuple
# montuple2 = (4, 19, 10) #Tuple
# montuple3 = montuple + montuple2 #Concatène les deux tuples
# print(montuple3) #Affiche le tuple
# montuple4 = montuple * 2 #Répète le tuple 2 fois
# print(montuple4) #Affiche le tuple

#endregion

#region Exercice 13 : Créer une liste des nombres pairs de 1 à 100

# uneliste = [] #Création d'une liste vide
# for x in range(1, 101): #Parcourt les nombres de 1 à 100
#     if x % 2 == 0: #Si le nombre est pair
#         uneliste.append(x) #Ajoute le nombre à la liste
# print(uneliste) #Affiche la liste

#endregion 

#region Exercice 14 : Génère un nombre de lancé de dés demandé à l'utilisateur et affiche le résultat de chaque lancé + la moyenne des lancés

# import random
# print("Rentré le nombre de lancé de dés à lancer") #Demande le nombre de lancé de dés à lancer
# x = int(input()) #Récupère le nombre de lancé de dés à lancer
# y = int() #Initialise la variable y
# listnombre = [] #Initialise la liste des nombres
# print("--------------------") #Affiche un séparateur
# while x > 0: #Tant que x est supérieur à 0
#     y = random.randint(1, 6) #Génère un nombre aléatoire entre 1 et 6
#     listnombre.append(y) #Ajoute le nombre généré à la liste
#     print(y) #Affiche le nombre généré
#     x = x - 1 #Décrémente la variable x
# print(sum(listnombre)/len(listnombre)) #Moyenne des lancés

#endregion

#region Exercice 15 : Compter le nombre d'occurence de chaque lettre dans une phrase

# maphrase = "Bonjour, je m'appelle Baptiste et j'ai 20 ans." #Phrase
# maphrase = maphrase.lower() #Met la phrase en minuscule
# for x in range(97, 123): #Parcourt les lettres de l'alphabet
#     print(chr(x), ":", maphrase.count(chr(x))) #Affiche la lettre et le nombre d'occurence

#endregion