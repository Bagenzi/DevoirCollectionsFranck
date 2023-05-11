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

 # Création de la tuple
 #=====================
tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Affichage des éléments de la tuple
#===================================
for element in tuple:
    print(element)
    
 # Affichage du nombre de fois que la valeur 3 apparaît dans la tuple
 #===================================================================
count_3 = tuple.count(3)
print("Le nombre de fois que la valeur 3 apparaît dans la tuple est :", count_3)

# Affichage du contenu de l'élément numéro 5
#============================================
element_5 = tuple[4]
print("Le contenu de l'élément numéro 5 est :", element_5)

# Ordonnancement de la tuple
#===========================
tuple_sorted = sorted(tuple)
print("La tuple ordonnée est :", tuple_sorted)

# Ajout d'un élément à la fin de la tuple
#=========================================
my_tuple = my_tuple + (11,)
print("La nouvelle tuple avec un élément ajouté à la fin est :", my_tuple)

    
    
    


