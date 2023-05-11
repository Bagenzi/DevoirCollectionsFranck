print("=====================QUESTION 1===============================\n\n")

# Création une liste de 10 éléments de type chaîne de caractères
#_______________________________________________________________
liste = ["bagenzi", "ciza", "muco", "nkingi", "keza", "gakiza", "iranzi", "ishimwe", "ndaganje", "irankunda"]

# Affichage des éléments de la liste
#-----------------------------------
print("Liste initiale : ", liste)

# Changement du contenu de l'élément numéro 5
#------------------------------------------
liste[4] = "kenny"
print("Liste après modification de l'élément numéro 5 : ", liste)

# Création d'une nouvelle liste en la remplissant avec les éléments de la liste précédente contenant la lettre "a"
#-----------------------------------------------------------------------------------------------------------------
nouvelle_liste = [element for element in liste if "a" in element]
print("Nouvelle liste contenant la lettre 'a' : ", nouvelle_liste)

# Ajout d'un élément à la fin de la liste
#----------------------------------------
liste.append("franck")
print("Liste après ajout d'un élément à la fin : ", liste)

# Ajout d'un élément à l’index numéro 2
#--------------------------------------
liste.insert(1, "pierre")
print("Liste après ajout d'un élément à l'index numéro 2 : ", liste)

# Suppression de l'élément numéro 3
#----------------------------------
del liste[2]
print("Liste après suppression de l'élément numéro 3 : ", liste)

# Suppression de l'élément à l’index numéro 2
#--------------------------------------------
liste.pop(2)
print("Liste après suppression de l'élément à l'index numéro 2 : ", liste)

# Ordre dans la liste
#--------------------
liste.sort()
print("Liste ordonnée : ", liste)

# Affichage de la liste au sens inverse
#--------------------------------------
liste_inverse = liste[::-1]
print("Liste au sens inverse : ", liste_inverse)

# Vider la liste
#---------------
liste.clear()
print("Liste vidée : ", liste)

# Suppression de la liste
#------------------------
del liste

print("\n\n=========================QUESTION 2===============================\n\n")

 # Création de la Tuple
 #=====================
Tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Affichage des éléments de la Tuple
#===================================
for element in Tuple:
    print(element)
    
 # Affichage du nombre de fois que la valeur 3 apparaît dans la Tuple
 #===================================================================
count_3 = Tuple.count(3)
print("Le nombre de fois que la valeur 3 apparaît dans la Tuple est :", count_3)

# Affichage du contenu de l'élément numéro 5
#============================================
element_5 = Tuple[4]
print("Le contenu de l'élément numéro 5 est :", element_5)

# Ordonnancement de la Tuple
#===========================
Tuple_sorted = sorted(Tuple)
print("La Tuple ordonnée est :", Tuple_sorted)

# Ajout d'un élément à la fin de la Tuple
#=========================================
Tuple = Tuple + (11,)
print("La nouvelle Tuple avec un élément ajouté à la fin est :", Tuple)

# Ajout d'un élément à l'index numéro 3
#======================================
my_list = list(Tuple)
my_list.insert(3, 15)
Tuple = tuple(my_list)
print("La nouvelle Tuple avec un élément ajouté à l'index numéro 3 est :", Tuple)



print("\n\n=========================QUESTION 3===============================\n\n")


# Création d'un ensemble de 10 éléments de type chaîne de caractères
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
my_set = set(["un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix"])

# Affichage du set
#+++++++++++++++++
print("Ensemble initial : ", my_set)

# Ajout d'un élément à l'ensemble
#+++++++++++++++++++++++++++++++++
my_set.add("vingt")
print("Ensemble après ajout : ", my_set)

# Suppression d'un élément de l'ensemble
#+++++++++++++++++++++++++++++++++++++++
my_set.remove("trois")
print("Ensemble après suppression : ", my_set)

# Suppression de l'ensemble (la totalite)
#++++++++++++++++++++++++++
my_set.clear()
print("Ensemble après suppression totale : ", my_set)


print("\n\n=========================QUESTION 4===============================\n\n")



# Création d'un dictionnaire de 10 éléments
#******************************************
dictionnaire = {
    "cle1": "one",
    "cle2": "two",
    "cle3": "three",
    "cle4": "four",
    "cle5": "five",
    "cle6": "six",
    "cle7": "seven",
    "cle8": "eight",
    "cle9": "nine",
    "cle10": "ten"
}

# Affichage du dictionnaire
#**************************
print("Dictionnaire :")
print(dictionnaire)

# Affichage des clés
#*******************
print("\nClés :")
for cle in dictionnaire.keys():
    print(cle)

# Affichage des valeurs
#**********************
print("\nValeurs :")
for valeur in dictionnaire.values():
    print(valeur)




