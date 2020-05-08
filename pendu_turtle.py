# -*- coding: utf-8 -*-
import turtle
import random


def pendu():
	turtle.goto(0,0)
	print("Bienvenue au jeu du PENDU")
	print()

	mot_a_deviner = input("Saisir un mot à faire deviner : ")

	for i in range(60):
		print()

	#écriture du mot pendu
	mot_pendu = ''
	for e in mot_a_deviner :
		if e == ' ' or e == '-' or e =="'":
			mot_pendu = mot_pendu + e
		else :
			mot_pendu = mot_pendu + '.'

	#affichage
	print("Mot : ")
	print(mot_pendu)
	print()

	#initialsation variables
	nbr_vie = 12
	memoire_lettre = []
	lettre_accent = {'à':'a', 'ã':'a', 'á':'a', 'â':'a',
'é':'e', 'è':'e', 'ê':'e', 'ë':'e', 'î':'i', 'ï':'i',
'ù':'u', 'ü':'u', 'û':'u', 'ô':'o', 'ö':'o', 'ç':'c'}

	#jeux
	while nbr_vie > 0 and mot_a_deviner != mot_pendu :
		try :
			#saisie de la lettre
			lettre = input("Saisir une lettre : ")
			print()
			assert len(lettre) == 1
			assert lettre not in memoire_lettre
			assert lettre != ''

			memoire_lettre.append(lettre)

			if lettre in mot_a_deviner :
				for i in range(len(mot_a_deviner)):
					#occurence
					if lettre == mot_a_deviner[i] :
						mot_pendu = mot_pendu[:i] + lettre + mot_pendu[i+1:]
				#accent1 (s'il y a la lettre dans le mot ET la lettre accentuée)
				#(ex : énorme, il y a le 'é' et le 'e')
				for elt in lettre_accent :
					temp = mot_a_deviner
					while lettre_accent[elt] == lettre and elt in temp :
						i = temp.index(elt)
						temp = (i+1)*'§' + temp[i+1:]
						mot_pendu = mot_pendu[:i] + elt + mot_pendu[i+1:]

			#accent2 (s'il y a uniquement la lettre accentuée dans mot_a_deviner)
			#(ex: symptôme, il n'y a que le 'ô' et pas le 'o')
			elif not (lettre in mot_a_deviner) :
				for elt in lettre_accent :
					if elt in mot_a_deviner and lettre == lettre_accent[elt]:
						i = mot_a_deviner.index(elt)
						mot_pendu = mot_pendu[:i] + elt + mot_pendu[i+1:]
						nbr_vie +=1

			if not( lettre in mot_a_deviner ):
				nbr_vie -= 1
				#dessin
				turtle.hideturtle()
				if nbr_vie == 11 :
					turtle.penup()
					turtle.goto(-150,-250)
					turtle.pendown()
					turtle.fd(400)
				elif nbr_vie == 10 :
					turtle.goto(-150,-250)
					turtle.left(90)
					turtle.fd(500)
				elif nbr_vie == 9 :
					turtle.goto(-150,250)
					turtle.right(90)
					turtle.fd(250)
				elif nbr_vie == 8 :
					turtle.penup()
					turtle.goto(-150,150)
					turtle.pendown()
					turtle.left(45)
					turtle.fd(140)
				elif nbr_vie == 7 :
					turtle.penup()
					turtle.goto(100,250)
					turtle.pendown()
					turtle.right(90+45)
					turtle.fd(40)
				elif nbr_vie == 6 :
					turtle.penup()
					turtle.goto(100-30,210-30)
					turtle.pendown()
					turtle.circle(30)
				elif nbr_vie == 5 :
					turtle.penup()
					turtle.goto(100,210-60)
					turtle.pendown()
					turtle.fd(40)
				elif nbr_vie == 4 :
					turtle.penup()
					turtle.goto(100,210-60-40)
					turtle.pendown()
					turtle.left(45)
					turtle.fd(80)
				elif nbr_vie == 3 :
					turtle.penup()
					turtle.goto(100,210-60-40)
					turtle.pendown()
					turtle.right(90)
					turtle.fd(80)
				elif nbr_vie == 2 :
					turtle.penup()
					turtle.goto(100,210-60-40)
					turtle.pendown()
					turtle.left(45)
					turtle.fd(150)
				elif nbr_vie == 1 :
					turtle.penup()
					turtle.goto(100,210-60-40-150)
					turtle.pendown()
					turtle.left(45)
					turtle.fd(120)
				else :
					turtle.penup()
					turtle.goto(100,210-60-40-150)
					turtle.pendown()
					turtle.right(90)
					turtle.fd(120)

			#affichage
			print("Mot : ")
			print(mot_pendu)
			print()
			if len(memoire_lettre) >= 2 :
				print("Lettres saisies dernierement : ",memoire_lettre)
			else :
				print("Lettre saisie dernierement : ",memoire_lettre)
			print()


		except AssertionError :
				if len(lettre) > 1 :
					print("saisair un seul caractere")
				if lettre == '':
					print("Saisir un caractere")
				if lettre in memoire_lettre :
					print("La lettre a deja ete saisie")


		print("============================================")
		print()



	#affichage final (gagné ou perdu)
	print()
	if nbr_vie == 0 :
		print("Perdu, le mot était : ", mot_a_deviner)
		print()
		print("============================================")
		print()
	if mot_a_deviner == mot_pendu :
		print("Bravo")
		print()
		print("============================================")
		print()





pendu()
turtle.exitonclick()
