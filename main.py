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
liste.sort()
print("Liste ordonnée : ", liste)