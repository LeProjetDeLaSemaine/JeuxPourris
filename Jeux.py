#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from random import randint

class PlusOuMoins(object):
	def __init__(self):
		print("Bienvenue sur le jeu du Plus ou Moins !\nAppuyez sur une touche pour commencer...", end="")
		input()
	
	def rules(self):
		print("Un nombre aléatoire est choisi par le jeu, et vous devez le trouver")
		print("Faites des suppositions, et le jeu vous indique si le nombre recherché est inférieur ou supérieur")
		input()
		self.jouer()

	def startGame(self):
		secretNum = randint(0, 1000)
		proposition, compteur = 0, 0
		while proposition != secretNum:
			proposition = int(input("Quel nombre proposez-vous ? "))
			print("C'est plus !" if secretNum > proposition else "C'est moins !")
			compteur+=1
		print("Bravo, c'était bien {} !".format(secretNum))
		print("Vous avez trouvé en {} tentative{}.".format(compteur, "s" if compteur>1 else ""))

	def jouer(self):
		os.system("cls" if os.name == "nt" else "clear")
		print("Choisissez une option :")
		print("1. Jouer")
		print("2. Règles du jeu")
		
		choice = int(input("Alors ? "))
		
		if choice == 1:
			self.startGame()
		elif choice == 2:
			self.rules()
		else:
			self.jouer()
			
class Batonnets(object):
	def __init__(self):
		print("Bienvenue sur le jeu des bâtonnets !\nAppuyez sur une touche pour commencer...", end="")
		input()
	
	def rules(self):
		print("Il y a 20 bâtonnets. Vous devez, à votre tour, en retirer, 1, 2, ou 3")
		print("Celui qui se voit obligé de retirer le dernier bâtonnet a perdu")
		input()
		self.jouer()

	def getPlayer(self, tour):
		if tour % 2 == 0:
			return 1
		else:
			return 2


	def itsYourTurn(self, nbr, player):
		print("[JOUEUR {}] Combien de bâtons voulez-vous prendre ?". format(player))
		a = int(input())
		if (a in range(1, 4)):
			nbr -= a
		else:
			print("Nombre invalide ! Réessayez !")
			self.itsYourTurn(nbr, player)
		return nbr

	def printBatons(self, num):
		a = str()
		for i in range(0, num):
			a += "| "
		print(a)

	def endGame(self, count):
		print("Le joueur {} a perdu !".format(self.getPlayer(count)))
		print("Appuyez sur une touche pour recommencer")
		input()
		self.jouer()

	def IAPlay(self, bat, batDiff):
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

	def startGameWithIA(self, bat):
		count = 0
		while bat > 1:
			self.printBatons(bat)
			if count % 2 == 0:
				prevBat = bat
				bat = self.itsYourTurn(bat, self.getPlayer(count))
			else:
				bat = self.IAPlay(bat, prevBat-bat)
			count += 1
		self.endGame(count)

	def startGame(self, bat):
		count = 0
		while bat > 1:
			self.printBatons(bat)
			bat = self.itsYourTurn(bat, self.getPlayer(count))
			count += 1
		self.endGame(count)

	def jouer(self):
		os.system('cls' if os.name == 'nt' else 'clear')
		print("Choisissez une option :")
		print("1. Jouer à deux")
		print("2. Jouer contre l'IA la plus puissante du mooooonde")
		print("3. Règles du jeu")

		choice = int(input("Alors ? "))

		if (choice == 3):
			self.rules()
		elif (choice == 1):
			self.startGame(20)
		elif (choice == 2):
			self.startGameWithIA(20)
		else:
			self.jouer()

class Pendu(object):
	def __init__(self):
		print("Bienvenue sur le jeu du pendu !\nAppuyez sur une touche pour commencer...", end="")
		self.mots = ["cette", "liste", "contient", "des", "mots", "simples", "comme", "bonjour", "sans", "etre", "anticonstitutionnels"]
		input()
		
	def choisirUnMot(self):
		return self.mots[randint(0, len(self.mots)-1)]
		
	def demanderUneLettre(self):
		c = input("Entrez une lettre : ")[:1].lower()
		return (c if len(c) ==1 and ord(c) in range(97, 123) else self.demanderUneLettre())
	
	def jouer(self):
		os.system('cls' if os.name == 'nt' else 'clear')
		motATrouver = self.choisirUnMot()
		motEntre = ''.join('_' for c in motATrouver)
		lettres = []
		t = 0
		while motEntre != motATrouver:
			print("Le mot est : ", motEntre)
			print("(Lettres proposées :", ", ".join(lettres), ")")
			c = self.demanderUneLettre()
			lettres.append(c)
			motEntre = ""
			for i in range(0, len(motATrouver)):
				if motATrouver[i] in lettres:
					motEntre += motATrouver[i]
				else:
					motEntre += '_'
			t+=1
		print("Bien joué ! Vous avez trouvé le mot \"" + motATrouver +"\" en", t, "tentatives")
		print("Ce qui vous fait un score de %d" % (100/(t/len(motATrouver))))
	


jeu = Batonnets() #Pendu() #PlusOuMoins()
jeu.jouer()