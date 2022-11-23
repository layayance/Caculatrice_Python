#Écrire un script qui recopie une chaîne (dans une nouvelle variable) en l’inversant. Ainsi par exemple, « patate » deviendra « etatap ».

#chaine_A = "petate"
#chaine_B = ""


'''
utilisateur = input("Veuillez entre votre phrase svp : ")
inverse = ""

for x in utilisateur:
    inverse = x + utilisateur

print("L'inverse de chaine de caratère est : ", inverse)'''

utilisateur = input("Veuillez entre votre mot : ")
inverse = ""
for x in utilisateur:
    inverse = x + inverse

print("L'inverse du mot ", utilisateur, "est :", inverse)