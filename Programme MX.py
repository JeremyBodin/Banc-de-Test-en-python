#################################################################################################
#################################################################################################
############################ Programme Test Faisceau MX #########################################
#################################################################################################
#################################################################################################


#################################################################################################
############################# Introduction pour expliquer le programme ##########################
#################################################################################################

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Un expert est une personne qui a fait toutes les erreurs qui peuvent être faites,
dans un domaine étroit... (Niels Bohr) """
            

"""
    1- Date de création du Programme : Le 22/05/2017
    2- Société                       : NP Capelec
    3- Auteur                        : BODIN Jérémy
    4- Langage utilisé               : Python (version 3.6)
    5- Titre                         : Programme MX
"""
 
"""

Ceci est un programme permettant d'exécuter un test de continuité sur des faisceaux de type
MX de références différentes. Le but de cette application est de remplacer la routine de
test des opérations manuelles (appuies sur bouton poussoir) effectuées auparavant par l'opérateur
(trice), leurs but était de vérifier l'état de chaque brin de faisceau par un ou des appuies sur
boutons poussoirs et avec un affichage de LED correspondantes à notre opération de routine exé
cutée.

Ce programme va donc permettre de remplacer ces actions manuelles(6 au totales) par un appui
seulement sur un bouton de l'interface graphique qui va lancer la fonction du programme correspondante.
On va donc créer une interface graphique grâce à tkinter afin de créer différents widgets pour :
afficher de l'information, prévenir en cas d'erreur, lancer les différents test en fonctions des
références de faisceaux.

Le test concernant la continuité va définir des entrées comme étant à un état BAS ou HAUT,
si ces entrées ne sont pas à leur état correpondant lorsqu'on appuie sur le bouton correspondant
on peut dire qu'il y a coupure dans un ou plusieurs brins du faisceau testé

"""

"""
Premièrement, étant donné que nous travaillons avec un Raspberry Pi, il va falloir importer
la ligne de code permettant de communiquer et d'utiliser les ports GPIOs du Raspberry. Pour ce
faire, il faut taper dans un terminal de commande :

sudo apt-get install python-RPi.GPIO.

Si vous voulez télécharger python sous windows aller sur ce lien :

http://www.python.org/getit/windows/

Sélectionnez la version de python souhaitée. Un tutoriel sur la plateforme youtube existe aussi
si vous narrivez pas à l'installer:

https://youtu.be/sMHbW9nXmgY'
"""
#################################################################################################
################################### Programme ###################################################
#################################################################################################

import RPi.GPIO as GPIO           	    #Pour simplifier la syntaxe on importe les entrées RPi.GPIO comme étant GPIO (plus rapide à l'écriture).
import tkinter.ttk                	    #On importre la classe tkinter.ttk.             
import time                       	    #On importe le fonction time.
from tkinter import *             	    #On importe la classe tkinter et toutes ses fonctions pour notre interface graphique.
from time import sleep            	    #De la classe time on importe la fonction sleep, permettant de créer un délai de temps(secondes).
from tkinter.messagebox import *  	    #Ici on importe les fonctions de la classe tkinter.messagebox afin de créer de l'affichage informatique: Message d'Erreur, d'informations.
from tkinter.font import*         	    #On implante la fonction permettant de modifier la police des caractères : taille du caractère, souligner ou surligner, mettre en gras...etc.

#Les ports du Raspberry Pi sont tous numérotés de façon différentes selon le mode d'utilisation BCM(BroadCom) ou BOARD.
#On a choisi le type BOARD

GPIO.setmode(GPIO.BOARD)#On a choisi le type BOARD
GPIO.setwarnings(False)#Ici on désactive les messages d'erreurs.


#On définit les sorties.
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

#On définit les entrées avec une résistace de tirage vers le bas.
GPIO.setup(35, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)





def Routine_1():

    GPIO.output(22,1)
    GPIO.output(31,1)
    GPIO.output(29,1)
    GPIO.output(33,1)
    GPIO.output(37,1)
    GPIO.output(32,0)
    GPIO.output(15,0)

    time.sleep(0.2)

    
    if (GPIO.input(24) == 1):
        print("routine 1.1 ok")
        if (GPIO.input(40) == 0):
            print("routine 1.2 ok")
            if (GPIO.input(35) == 0):
                print("routine 1.3 ok")
                if (GPIO.input(38) == 0):
                    print("routine 1.4 ok")
                    if (GPIO.input(36) == 0):
                        canvas2.create_text(255,237, anchor=W, font="Roboto", text="Routine 1 ok.\n")
                        print ("Routine 1 ok")
                    else:
                        canvas2.create_text(80,237, anchor=W, font="Roboto", text="Erreur!!! Routine 1 nn fonctionne pas.\n")
                        print("routine 1.5 nulle")
                else:
                    canvas2.create_text(80,237, anchor=W, font="Roboto", text="Erreur!!! La Routine 1 ne fonctionne pas.\n")
                    print("routine 1.4 nulle")
            else:
                canvas2.create_text(80,237, anchor=W, font="Roboto", text="Erreur!!! La Routine 1 ne fonctionne pas.\n")
                print("routine 1.3 nulle")               
        else:
            canvas2.create_text(80,237, anchor=W, font="Roboto", text="Erreur!!! La Routine 1 ne fonctionne pas.\n")
            print("routine 1.2 nulle")
    else:
        canvas2.create_text(80,237, anchor=W, font="Roboto", text="Erreur!!! La Routine 1 ne fonctionne pas.\n")
        print("routine 1.1 nulle")

def Routine_2():

    GPIO.output(31,0)
    GPIO.output(29,1)
    GPIO.output(33,1)
    GPIO.output(37,1)
    GPIO.output(32,0)
    GPIO.output(15,0)

    time.sleep(0.2)

    
    if (GPIO.input(24) == 1):
        print("routine 2.1 ok")
        if (GPIO.input(40) == 1):
            print("routine 2.2 ok")
            if (GPIO.input(35) == 0):
                print("routine 2.3 ok")
                if (GPIO.input(38) == 0):
                    print("routine 2.4 ok")
                    if (GPIO.input(36) == 0):
                        canvas2.create_text(255,254, anchor=W, font="Roboto", text="Routine 2 ok.\n")
                        print ("Routine 2 ok")
                    else:
                        canvas2.create_text(80,254, anchor=W, font="Roboto", text="Erreur!!! La Routine 2 ne fonctionne pas.\n")
                        print("routine 2.5 nulle")
                else:
                    canvas2.create_text(80,254, anchor=W, font="Roboto", text="Erreur!!! La Routine 2 ne fonctionne pas.\n")
                    print("routine 2.4 nulle")
            else:
                canvas2.create_text(80,254, anchor=W, font="Roboto", text="Erreur!!! La Routine 2 ne fonctionne pas.\n")
                print("routine 2.3 nulle")               
        else:
            canvas2.create_text(80,254, anchor=W, font="Roboto", text="Erreur!!! La Routine 2 ne fonctionne pas.\n")
            print("routine 2.2 nulle")
    else:
        canvas2.create_text(80,254, anchor=W, font="Roboto", text="Erreur!!! La Routine 2 ne fonctionne pas.\n")
        print("routine 2.1 nulle")

        
def Routine_3():

    GPIO.output(31,1)
    GPIO.output(29,0)
    GPIO.output(33,1)
    GPIO.output(37,1)
    GPIO.output(32,0)
    GPIO.output(15,0)

    time.sleep(0.2)

    
    if (GPIO.input(24) == 1):
        print("routine 3.1 ok")
        if (GPIO.input(40) == 1):
            print("routine 3.2 ok")
            if (GPIO.input(35) == 1):
                print("routine 3.3 ok")
                if (GPIO.input(38) == 0):
                    print("routine 3.4 ok")
                    if (GPIO.input(36) == 0):
                        canvas2.create_text(255,271, anchor=W, font="Roboto", text="Routine 3 ok.\n")
                        print ("Routine 3 ok")
                    else:
                        canvas2.create_text(80,271, anchor=W, font="Roboto", text="Erreur!!! La Routine 3 ne fonctionne pas.\n")
                        print("routine 3.5 nulle")
                else:
                    canvas2.create_text(80,271, anchor=W, font="Roboto", text="Erreur!!! La Routine 3 ne fonctionne pas.\n")
                    print("routine 3.4 nulle")
            else:
                canvas2.create_text(80,271, anchor=W, font="Roboto", text="Erreur!!! La Routine 3 ne fonctionne pas.\n")
                print("routine 3.3 nulle")               
        else:
            canvas2.create_text(80,271, anchor=W, font="Roboto", text="Erreur!!! La Routine 3 ne fonctionne pas.\n")
            print("routine 3.2 nulle")
    else:
        canvas2.create_text(80,271, anchor=W, font="Roboto", text="Erreur!!! La Routine 3 ne fonctionne pas.\n")
        print("routine 3.1 nulle")

    
def Routine_4():

    GPIO.output(31,1)
    GPIO.output(29,1)
    GPIO.output(33,0)
    GPIO.output(37,1)
    GPIO.output(32,0)
    GPIO.output(15,0)

    time.sleep(0.2)

    
    if (GPIO.input(24) == 1):
        print("routine 4.1 ok")
        if (GPIO.input(40) == 0):
            print("routine 4.2 ok")
            if (GPIO.input(35) == 0):
                print("routine 4.3 ok")
                if (GPIO.input(38) == 0):
                    print("routine 4.4 ok")
                    if (GPIO.input(36) == 0):
                        canvas2.create_text(255,288, anchor=W, font="Roboto", text="Routine 4 ok.\n")
                        print ("Routine 4 ok")
                    else:
                        canvas2.create_text(80,288, anchor=W, font="Roboto", text="Erreur!!! La Routine 4 ne fonctionne pas.\n")
                        print("routine 4.5 nulle")
                else:
                    canvas2.create_text(80,288, anchor=W, font="Roboto", text="Erreur!!! La Routine 4 ne fonctionne pas.\n")
                    print("routine 4.4 nulle")
            else:
                canvas2.create_text(80,288, anchor=W, font="Roboto", text="Erreur!!! La Routine 4 ne fonctionne pas.\n")
                print("routine 4.3 nulle")               
        else:
            canvas2.create_text(80,288, anchor=W, font="Roboto", text="Erreur!!! La Routine 4 ne fonctionne pas.\n")
            print("routine 4.2 nulle")
    else:
        canvas2.create_text(80,288, anchor=W, font="Roboto", text="Erreur!!! La Routine 4 ne fonctionne pas.\n")
        print("routine 4.1 nulle")

def Routine_5():

    GPIO.output(31,0)
    GPIO.output(29,1)
    GPIO.output(33,0)
    GPIO.output(37,1)
    GPIO.output(32,0)
    GPIO.output(15,0)

    time.sleep(0.2)

    
    if (GPIO.input(24) == 1):
        print("routine 5.1 ok")
        if (GPIO.input(40) == 1):
            print("routine 5.2 ok")
            if (GPIO.input(38) == 1):
                print("routine 5.3 ok")
                if (GPIO.input(35) == 0):
                    print("routine 5.4 ok")
                    if (GPIO.input(36) == 0):
                        canvas2.create_text(255,305, anchor=W, font="Roboto", text="Routine 5 ok.\n")
                        print ("Routine 5 ok")
                    else:
                        canvas2.create_text(80,305, anchor=W, font="Roboto", text="Erreur!!! La Routine 5 ne fonctionne pas.\n")
                        print("routine 5.5 nulle")
                else:
                    canvas2.create_text(80,305, anchor=W, font="Roboto", text="Erreur!!! La Routine 5 ne fonctionne pas.\n")
                    print("routine 5.4 nulle")
            else:
                canvas2.create_text(80,305, anchor=W, font="Roboto", text="Erreur!!! La Routine 5 ne fonctionne pas.\n")
                print("routine 5.3 nulle")               
        else:
            canvas2.create_text(80,305, anchor=W, font="Roboto", text="Erreur!!! La Routine 5 ne fonctionne pas.\n")
            print("routine 5.2 nulle")
    else:
        canvas2.create_text(80,305, anchor=W, font="Roboto", text="Erreur!!! La Routine 5 ne fonctionne pas.\n")
        print("routine 5.1 nulle")



def Routine_6():

    GPIO.output(31,1)
    GPIO.output(29,1)
    GPIO.output(33,1)
    GPIO.output(37,0)
    GPIO.output(32,0)
    GPIO.output(15,0)

    time.sleep(0.2)
    
    
    if (GPIO.input(24) == 1):
        print("routine 6.1 ok")
        if (GPIO.input(36) == 1):
            print("routine 6.2 ok")
            if (GPIO.input(35) == 0):
                print("routine 6.3 ok")
                if (GPIO.input(38) == 0):
                    print("routine 6.4 ok")
                    if (GPIO.input(40) == 0):
                        canvas2.create_text(255,322, anchor=W, font="Roboto", text="Routine 6 ok.\n")
                        print ("Routine 6 ok")
                    else:
                        canvas2.create_text(80,322, anchor=W, font="Roboto", text="Erreur!!! La Routine 6 ne fonctionne pas.\n")
                        print("routine 6.5 nulle")
                else:
                    canvas2.create_text(80,322, anchor=W, font="Roboto", text="Erreur!!! La Routine 6 ne fonctionne pas.\n")
                    print("routine 6.4 nulle")
            else:
                canvas2.create_text(80,322, anchor=W, font="Roboto", text="Erreur!!! La Routine 6 ne fonctionne pas.\n")
                print("routine 6.3 nulle")               
        else:
            canvas2.create_text(80,322, anchor=W, font="Roboto", text="Erreur!!! La Routine 6 ne fonctionne pas.\n")
            print("routine 6.2 nulle")
    else:
        canvas2.create_text(80,322, anchor=W, font="Roboto", text="Erreur!!! La Routine 6 ne fonctionne pas.\n")
        print("routine 6.1 nulle\n\n")

    GPIO.output(31,1)
    GPIO.output(29,1)
    GPIO.output(33,1)
    GPIO.output(37,1)
    GPIO.output(32,1)
    GPIO.output(15,1)
    GPIO.output(22,1)


def Inversion():

    GPIO.output(31,1)
    GPIO.output(29,1)
    GPIO.output(33,1)
    GPIO.output(37,1)
    GPIO.output(32,0)
    GPIO.output(15,0)
    GPIO.output(22,0)
    
    time.sleep(0.2)

    
    if (GPIO.input(24) == 0):
        print("routine 0.1 ok")
        if (GPIO.input(40) == 0):
            print("routine 0.2 ok")
            if (GPIO.input(35) == 0):
                print("routine 0.3 ok")
                if (GPIO.input(38) == 0):
                    print("routine 0.4 ok")
                    if (GPIO.input(36) == 0):
                        canvas2.create_text(450,220, anchor=W, font="Roboto", text=" Inversion ok.\n")
                        print ("Inversion ok")
                    else:
                        canvas2.create_text(30,220, anchor=W, font="Roboto", text=" Erreur!!! L'Inversion ne fonctionne pas.\n")
                        print("routine 0.5 nulle")
                else:
                    canvas2.create_text(30,220, anchor=W, font="Roboto", text=" Erreur!!! L'Inversion ne fonctionne pas.\n")
                    print("routine 0.4 nulle")
            else:
                canvas2.create_text(30,220, anchor=W, font="Roboto", text=" Erreur!!! L'Inversion ne fonctionne pas.\n")
                print("routine 0.3 nulle")               
        else:
            canvas2.create_text(30,220, anchor=W, font="Roboto", text=" Erreur!!! L'Inversion ne fonctionne pas.\n")
            print("routine 0.2 nulle")
    else:
        canvas2.create_text(30,220, anchor=W, font="Roboto", text=" Erreur!!! L'Inversion ne fonctionne pas.\n")
        print("routine 0.1 nulle")                         


def Routine_7():

    GPIO.output(22,1)
    GPIO.output(31,1)
    GPIO.output(29,1)
    GPIO.output(33,1)
    GPIO.output(37,1)
    GPIO.output(32,0)
    GPIO.output(15,0)

    time.sleep(0.2)

    
    if (GPIO.input(24) == 1):
        print("routine 1.1 ok")
        if (GPIO.input(40) == 0):
            print("routine 1.2 ok")
            if (GPIO.input(35) == 0):
                print("routine 1.3 ok")
                if (GPIO.input(38) == 0):
                    print("routine 1.4 ok")
                    if (GPIO.input(36) == 0):
                        canvas2.create_text(450,237, anchor=W, font="Roboto", text=" Routine 1 ok.\n")
                        print ("Routine 1 ok")
                    else:
                        canvas2.create_text(450,237, anchor=W, font="Roboto", text=" Erreur!!! La Routine 1 ne fonctionne pas.\n")
                        print("routine 1.5 nulle")
                else:
                    canvas2.create_text(450,237, anchor=W, font="Roboto", text=" Erreur!!! La Routine 1 ne fonctionne pas.\n")
                    print("routine 1.4 nulle")
            else:
                canvas2.create_text(450,237, anchor=W, font="Roboto", text=" Erreur!!! La Routine 1 ne fonctionne pas.\n")
                print("routine 1.3 nulle")               
        else:
            canvas2.create_text(450,237, anchor=W, font="Roboto", text=" Erreur!!! La Routine 1 ne fonctionne pas.\n")
            print("routine 1.2 nulle")
    else:
        canvas2.create_text(450,237, anchor=W, font="Roboto", text=" Erreur!!! La Routine 1 ne fonctionne pas.\n")
        print("routine 1.1 nulle")

def Routine_8():

    GPIO.output(31,0)
    GPIO.output(29,1)
    GPIO.output(33,1)
    GPIO.output(37,1)
    GPIO.output(32,0)
    GPIO.output(15,0)

    time.sleep(0.2)

    
    if (GPIO.input(24) == 1):
        print("routine 2.1 ok")
        if (GPIO.input(40) == 1):
            print("routine 2.2 ok")
            if (GPIO.input(35) == 0):
                print("routine 2.3 ok")
                if (GPIO.input(38) == 0):
                    print("routine 2.4 ok")
                    if (GPIO.input(36) == 0):
                        canvas2.create_text(450,254, anchor=W, font="Roboto", text=" Routine 2 ok.\n")
                        print ("Routine 2 ok")
                    else:
                        canvas2.create_text(450,254, anchor=W, font="Roboto", text=" Erreur!!! La Routine 2 ne fonctionne pas.\n")
                        print("routine 2.5 nulle")
                else:
                    canvas2.create_text(450,254, anchor=W, font="Roboto", text=" Erreur!!! La Routine 2 ne fonctionne pas.\n")
                    print("routine 2.4 nulle")
            else:
                canvas2.create_text(450,254, anchor=W, font="Roboto", text=" Erreur!!! La Routine 2 ne fonctionne pas.\n")
                print("routine 2.3 nulle")               
        else:
            canvas2.create_text(450,254, anchor=W, font="Roboto", text=" Erreur!!! La Routine 2 ne fonctionne pas.\n")
            print("routine 2.2 nulle")
    else:
        canvas2.create_text(450,254, anchor=W, font="Roboto", text=" Erreur!!! La Routine 2 ne fonctionne pas.\n")
        print("routine 2.1 nulle")

        
def Routine_9():

    GPIO.output(31,1)
    GPIO.output(29,0)
    GPIO.output(33,1)
    GPIO.output(37,1)
    GPIO.output(32,0)
    GPIO.output(15,0)

    time.sleep(0.2)

    
    if (GPIO.input(24) == 1):
        print("routine 3.1 ok")
        if (GPIO.input(40) == 1):
            print("routine 3.2 ok")
            if (GPIO.input(35) == 1):
                print("routine 3.3 ok")
                if (GPIO.input(38) == 0):
                    print("routine 3.4 ok")
                    if (GPIO.input(36) == 0):
                        canvas2.create_text(450,271, anchor=W, font="Roboto", text=" Routine 3 ok.\n")
                        print ("Routine 3 ok")
                    else:
                        canvas2.create_text(450,271, anchor=W, font="Roboto", text=" Erreur!!! La Routine 3 ne fonctionne pas.\n")
                        print("routine 3.5 nulle")
                else:
                    canvas2.create_text(450,271, anchor=W, font="Roboto", text=" Erreur!!! La Routine 3 ne fonctionne pas.\n")
                    print("routine 3.4 nulle")
            else:
                canvas2.create_text(450,271, anchor=W, font="Roboto", text=" Erreur!!! La Routine 3 ne fonctionne pas.\n")
                print("routine 3.3 nulle")               
        else:
            canvas2.create_text(450,271, anchor=W, font="Roboto", text=" Erreur!!! La Routine 3 ne fonctionne pas.\n")
            print("routine 3.2 nulle")
    else:
        canvas2.create_text(450,271, anchor=W, font="Roboto", text=" Erreur!!! La Routine 3 ne fonctionne pas.\n")
        print("routine 3.1 nulle")

    
def Routine_10():

    GPIO.output(31,1)
    GPIO.output(29,1)
    GPIO.output(33,0)
    GPIO.output(37,1)
    GPIO.output(32,0)
    GPIO.output(15,0)

    time.sleep(0.2)

    
    if (GPIO.input(24) == 1):
        print("routine 4.1 ok")
        if (GPIO.input(40) == 0):
            print("routine 4.2 ok")
            if (GPIO.input(35) == 0):
                print("routine 4.3 ok")
                if (GPIO.input(38) == 0):
                    print("routine 4.4 ok")
                    if (GPIO.input(36) == 0):
                        canvas2.create_text(450,288, anchor=W, font="Roboto", text=" Routine 4 ok.\n")
                        print ("Routine 4 ok")
                    else:
                        canvas2.create_text(450,288, anchor=W, font="Roboto", text=" Erreur!!! La Routine 4 ne fonctionne pas.\n")
                        print("routine 4.5 nulle")
                else:
                    canvas2.create_text(450,288, anchor=W, font="Roboto", text=" Erreur!!! La Routine 4 ne fonctionne pas.\n")
                    print("routine 4.4 nulle")
            else:
                canvas2.create_text(450,288, anchor=W, font="Roboto", text=" Erreur!!! La Routine 4 ne fonctionne pas.\n")
                print("routine 4.3 nulle")               
        else:
            canvas2.create_text(450,288, anchor=W, font="Roboto", text=" Erreur!!! La Routine 4 ne fonctionne pas.\n")
            print("routine 4.2 nulle")
    else:
        canvas2.create_text(450,288, anchor=W, font="Roboto", text=" Erreur!!! La Routine 4 ne fonctionne pas.\n")
        print("routine 4.1 nulle")

def Routine_11():

    GPIO.output(31,0)
    GPIO.output(29,1)
    GPIO.output(33,0)
    GPIO.output(37,1)
    GPIO.output(32,0)
    GPIO.output(15,0)

    time.sleep(0.2)

    
    if (GPIO.input(24) == 1):
        print("routine 5.1 ok")
        if (GPIO.input(40) == 1):
            print("routine 5.2 ok")
            if (GPIO.input(38) == 1):
                print("routine 5.3 ok")
                if (GPIO.input(35) == 0):
                    print("routine 5.4 ok")
                    if (GPIO.input(36) == 0):
                        canvas2.create_text(450,305, anchor=W, font="Roboto", text=" Routine 5 ok.\n")
                        print ("Routine 5 ok")
                    else:
                        canvas2.create_text(450,305, anchor=W, font="Roboto", text=" Erreur!!! La Routine 5 ne fonctionne pas.\n")
                        print("routine 5.5 nulle")
                else:
                    canvas2.create_text(450,305, anchor=W, font="Roboto", text=" Erreur!!! La Routine 5 ne fonctionne pas.\n")
                    print("routine 5.4 nulle")
            else:
                canvas2.create_text(450,305, anchor=W, font="Roboto", text=" Erreur!!! La Routine 5 ne fonctionne pas.\n")
                print("routine 5.3 nulle")               
        else:
            canvas2.create_text(450,305, anchor=W, font="Roboto", text=" Erreur!!! La Routine 5 ne fonctionne pas.\n")
            print("routine 5.2 nulle")
    else:
        canvas2.create_text(450,305, anchor=W, font="Roboto", text=" Erreur!!! La Routine 5 ne fonctionne pas.\n")
        print("routine 5.1 nulle")



def Routine_12():

    GPIO.output(31,1)
    GPIO.output(29,1)
    GPIO.output(33,1)
    GPIO.output(37,0)
    GPIO.output(32,0)
    GPIO.output(15,0)

    time.sleep(0.2)
    
    
    if (GPIO.input(24) == 1):
        print("routine 6.1 ok")
        if (GPIO.input(36) == 1):
            print("routine 6.2 ok")
            if (GPIO.input(35) == 0):
                print("routine 6.3 ok")
                if (GPIO.input(38) == 0):
                    print("routine 6.4 ok")
                    if (GPIO.input(40) == 0):
                        canvas2.create_text(450,322, anchor=W, font="Roboto", text=" Routine 6 ok.\n")
                        print ("Routine 6 ok")
                    else:
                        canvas2.create_text(450,322, anchor=W, font="Roboto", text=" Erreur!!! La Routine 6 ne fonctionne pas.\n")
                        print("routine 6.5 nulle")
                else:
                    canvas2.create_text(450,322, anchor=W, font="Roboto", text=" Erreur!!! La Routine 6 ne fonctionne pas.\n")
                    print("routine 6.4 nulle")
            else:
                canvas2.create_text(450,322, anchor=W, font="Roboto", text=" Erreur!!! La Routine 6 ne fonctionne pas.\n")
                print("routine 6.3 nulle")               
        else:
            canvas2.create_text(450,322, anchor=W, font="Roboto", text=" Erreur!!! La Routine 6 ne fonctionne pas.\n")
            print("routine 6.2 nulle")
    else:
        canvas2.create_text(450,322, anchor=W, font="Roboto", text=" Erreur!!! La Routine 6 ne fonctionne pas.\n")
        print("routine 6.1 nulle\n\n")

    GPIO.output(31,1)
    GPIO.output(29,1)
    GPIO.output(33,1)
    GPIO.output(37,1)
    GPIO.output(32,1)
    GPIO.output(15,1)
    GPIO.output(22,1)

def Message_info():                                                                                                                                 #Cette défintion s'appelle "Message_info". Elle a comme paramètre "ok".
    showinfo('Fin test', "Le test est terminé.")                                                     #Une fenêtre "Quitter le programme" s'affichera avec écrit "Êtes-vous sûr de vouloir quitter l'interface graphique?".
    return                                                                                                                                  #Si la réponse est oui, la fenêtre se fermera.



def Exit_Program():                                                                                                                                 #Cette définition s'appelle "Exit_Program".
    if askyesno('Quitter le Programme', "Êtes-vous sûr de vouloir quitter l'interface graphique?"):                                                     #Une fenêtre "Quitter le programme" s'affichera avec écrit "Êtes-vous sûr de vouloir quitter l'interface graphique?".
        quit(fenetre)                                                                                                                                   #Si la réponse est oui, la fenêtre se fermera.
    else:                                                                                                                                               #Autrement
        while 1:
            break                                                                                                                                        #On stop la boucle avec la fonction break.



def Fonction_principale():  #Cette définition s'appelle "Fonction-principale", c'est elle qui fait tourner le programme en faisant successisement et dans l'ordre ci-dessous les définitions vu précedemment.
    Routine_1()
    Routine_2()
    Routine_3()
    Routine_4()
    Routine_5()
    Routine_6()
    Inversion()
    Routine_7()
    Routine_8()
    Routine_9()
    Routine_10()
    Routine_11()
    Routine_12()    
    Message_info()
    canvas2.delete(ALL)
    return

#################################################################################################
###################################### Création de l'interface ##################################
#################################################################################################

fenetre = Tk()
fenetre.title("TEST FAISCEAU MX")
fenetre.geometry("800x480")
fenetre['bg']='bisque'

menubar = Menu(fenetre, bg='light grey', fg='black', borderwidth=1, cursor='tcross', relief=RAISED)

fenetre.config(menu=menubar)

myFont1 = Font(family='Roboto', size=13)

canvas1 = Canvas(fenetre,width=787,height=300,bg='light grey',highlightcolor='silver', borderwidth=4, relief=SUNKEN)
canvas1.grid(row=1, column=1,rowspan=1,columnspan=1, sticky='n',pady=0, padx=0)

canvas2 = Canvas(fenetre,width=787,height=321,bg='white',highlightcolor='silver', borderwidth=4, relief=SUNKEN)
canvas2.grid(row=1, column=1,rowspan=1,columnspan=1, sticky='n',pady=89, padx=0)

Frame1 = Frame(canvas1, borderwidth=15, relief=FLAT, bg='light grey')
Frame1.grid(column=1, row=1, rowspan=20, sticky='n', pady=5, padx=20)

Button_Fonction_principale = Button(Frame1, text='Commencer le test', font=myFont1 , highlightthickness=2, borderwidth=5, highlightbackground='white', cursor='tcross',command=Fonction_principale, bg='sky blue', activebackground='bisque4', activeforeground='sky blue')
Button_Fonction_principale.grid(column=1, row=1,sticky='n',pady=1,padx=114)

Button_Exit = Button(Frame1, text='Quitter', font=myFont1 , highlightthickness=2, borderwidth=5, highlightbackground='white', cursor='tcross',command=Exit_Program, bg='red', activebackground='bisque4', activeforeground='sky blue')
Button_Exit.grid(column=2, row=1,sticky='n',pady=1,padx=113)
