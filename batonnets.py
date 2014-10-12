#!/usr/bin/env python
# Le jeu des bâtonnets de Fort Boyard
# -*- coding: utf-8 -*-

import os
from time import sleep

def rules():
	print("Il y a 20 bâtonnets. Vous devez, à votre tour, en retirer, 1, 2, ou 3")
	print("Celui qui se voit obligé de retirer le dernier bâtonnet a perdu")
	raw_input()
	accueil()

def getPlayer(tour):
	if tour % 2 == 0:
		return 1
	else:
		return 2


def itsYourTurn(nbr, player):
	print("[JOUEUR {}] Combien de bâtons voulez-vous prendre ?". format(player))
	a = int(raw_input())
	if (a in range(1, 4)):
		nbr -= a
	else:
		print("Nombre invalide ! Réessayez !")
		itsYourTurn(nbr, player)
	return nbr

def printBatons(num):
	a = str()
	for i in range(0, num):
		a += "| "
	print a

def endGame(count):
	print("Le joueur {} a perdu !".format(getPlayer(count)))
	print("Appuyez sur une touche pour recommencer")
	raw_input()
	accueil()

def IAPlay(bat, batDiff):
	if bat - 5 in range(1, 3):
		numToTake = bat - 5
	elif bat - 9 in range(1, 3):
		numToTake = bat - 9
	elif bat - 13 in range(1, 3):
		numToTake = bat - 13
	else:
		numToTake = 4 - batDiff
	print("Le joueur 2 prend ", numToTake, "bâtonnet(s)")
	return bat - numToTake

def startGameWithIA(bat):
	count = 0
	while bat > 1:
		printBatons(bat)
		if count % 2 == 0:
			prevBat = bat
			bat = itsYourTurn(bat, getPlayer(count))
		else:
			bat = IAPlay(bat, prevBat-bat)
		count += 1
	endGame(count)

def startGame(bat):
	count = 0
	while bat > 1:
		printBatons(bat)
		bat = itsYourTurn(bat, getPlayer(count))
		count += 1
	endGame(count)

def accueil():
	os.system('cls' if os.name == 'nt' else 'clear')
	print("                Bienvenue sur le jeu des bâtonnets !\n")
	print("Choisissez une option :")
	print("1. Jouer à deux")
	print("2. Jouer contre l'IA la plus puissante du mooooonde")
	print("3. Règles du jeu")

	choice = int(raw_input("Alors ? "))

	if (choice == 3):
		rules()
	elif (choice == 1):
		startGame(20)
	elif (choice == 2):
		startGameWithIA(20)
	else:
		accueil()

accueil()