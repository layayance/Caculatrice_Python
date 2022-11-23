# while True:
#     calcul = input("Qu'est ce que voulez faire comme calcul : ")
#     mon_split = calcul.split()  
#     if calcul == "stop":
#         break 
#     elif len(mon_split) < 3:
#         print("Pas acces arguments : argument minimun 3")
#     else:
#         print(eval(mon_split[0] +  mon_split[1] +  mon_split[2]))
# print("Merci d'avoir utilise la calculatrice")


while True:
    try:
        calcul = input("calcul = ")
        print(eval(calcul))
        
    except NameError:
        print("attention la valeur n'est pas bonne ! ")
        calcul = input("calcul = ")
        print(eval(calcul))
    except SyntaxError:
        print("veuillez inserer des caracteres ! ")
        calcul = input("calcul = ")
        print(eval(calcul))
