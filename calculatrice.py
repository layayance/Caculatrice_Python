# Veuillez tapez un calcul : 3 + 2 
# Le resultat est : 5 

# Veuillez tapez un calcul : 5 - 2
# Le resultat est : 3 

# Vous devez creer 4 fonctions ( addition(), soustraction(), multiplication(), division() ) et faire en sorte qu’elle soit appelée au moment ou l’utilisateur ecrit son calcul.





# print("Quelle opération voulez-vous effectuer ?")
# print("1 Addition.")
# print("2 Soustration.")
# print("3 Mutiplication.")
# print("Division.")

# choice = input()

# if (choice == "1"){
    
# }




# A = input("Veuillez tape calcul 1 : ")
# B = input("Veuillez tape calcul 2 : ")
# somme = int(A) + int(B)
# print("Le résultat est : ",somme)

# A = input("Veuillez tape calcul 1 : ")
# B = input("Veuillez tape calcul 2 : ")
# somme = int(A) - int(B)
# print("Le résulat est : ", somme)

# A = input("Veuillez tape calcul 1 : ")
# B = input("Veuillez tape calcul 2 : ")
# somme = int(A) * int(B)
# print("Le résulat est : ", somme)

a = 0
b = 0

def Soustraction(a,b):
    print(a - b)

def Addition(a,b):
    print(a + b)


def Mutliplication(a,b):
    print(a * b)

def Division(a,b):
    print(a / b)


calcul = input("Qu'est ce que voulez faire comme calcul : ? ")


if operateur == "+" :
    Addition(x,y)
elif operateur == "-":
    Soustraction(x,y)
elif operateur == "*":
    Mutliplication(x,y)
else :
    Division(x,y)

