#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Classique...

import os
from random import randint

def rules():
	print("Un nombre aléatoire est choisi par le jeu, et vous devez le trouver")
	print("Faites des suppositions, et le jeu vous indique si le nombre recherché est inférieur ou supérieur")
	raw_input()
	accueil()

def startGame():
	secretNum = randint(0, 1000)
	print(secretNum)
	proposition, compteur = 0, 0
	while proposition != secretNum:
		proposition = int(raw_input("Quel nombre proposez-vous ? "))
		print("C'est plus !" if secretNum > proposition else "C'est moins !")
		compteur+=1
	print("Bravo, c'était bien {} !".format(secretNum))
	print("Vous avez trouvé en {} tentative{}.".format(compteur, "s" if compteur>1 else ""))

def accueil():
	os.system("cls" if os.name == "nt" else "clear")
	print("                Bienvenue sur le jeu des bâtonnets !\n")
	print("Choisissez une option :")
	print("1. Jouer")
	print("2. Règles du jeu")
	
	choice = int(raw_input("Alors ? "))
	
	if choice == 1:
		startGame()
	elif choice == 2:
		rules()
	else:
		accueil()

accueil()