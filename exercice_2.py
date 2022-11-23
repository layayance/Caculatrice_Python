





def nombre():
    phrase = input("Veuillez ecrire votre phrases : ")  

    compteur = 0
    for mot in phrase:
        if mot == "e":
            compteur += 1
    return compteur

print(nombre())


def compt():
	phrase = "coucou les amise cava ?"
	compteur = 0

	for x in phrase:
		if x == "e":
			compteur += 1
	return compteur
