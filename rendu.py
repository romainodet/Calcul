#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
                 /
    |      /  |////:  o////  ./////    s`      y////-
    |         |       /      s-    s.  h`      h
    |         |////.  /      s-    s-  h`      d////`
    |         |       /      s-    s.  h`      h
    |////     |////:  o/::/  -o/::/o   y////.  d////-

        -mmmmm.   ymmmmmmmmmy-   ymmmm-       -ymmmmmm
        -mmmmm.   ymmmm+ohmmmm-  ymmmm-     :mmmmdo/+s
        -mmmmm.   ymmm     hmmmo ymmmm-    hmmmm:
        -mmmmm:   hmmm     mmmm/ ymmmm/    ymmmmy:
        -mmmmmmmmmmmmmmmmmmmms   ymmmmmmmm  dommmmmmmm
        -hhhhhhhhhhhhhhhhys+/    shhhhhhhhy  ./shddhh/
        
        
     file :rendu.py
     By: romain.odet <romain.odet@lecole-ldlc.com>           
     Created: 24/10/2018 15:26 by Romain ODET  
"""
# defintion des vars
text = ""

def blank(lignes):
    """docstring for blank"""
    for i in range (lignes):
        print("")

def pause():
    """docstring for pause"""
    raw_input()

def dectobin(value):

    digits = []
    while value > 0:
        digits.append(value % 2)
        value = value // 2
    digits.reverse()
    print("".join([str(d) for d in digits]))
    input()

def bintodec(bin_string):

    result = 0
    for i in range(len(bin_string)):
        char = int(bin_string[i])
        if char == 1:
            result += 2 ** (len(bin_string) - 1 - i)
    print("The result is : ", result)
    input()

def rot13(text):

    tableau = list(text)
    for i in range (len(text)):
        tableau[i] = ord(tableau[i])
        if ((tableau[i] >= ord("a") and tableau[i] <= ord('m')) or 
        (tableau[i] >= ord("A") and tableau[i] <= ord("M"))):
            tableau[i] += 13
        elif ((tableau[i] > ord("m") and tableau[i] <= ord('z')) or 
        (tableau[i] > ord('M') and tableau[i] <= ord('Z'))):
            tableau[i] -= 13
    for i in range (len(text)):
        tableau[i] = chr(tableau[i])
    print ''.join(tableau)
    input()

def fartocel(temp):
    """docstring for fartocel"""
    
def celtofar(temp):
    """docstring for celtofar"""
    
def celtokelvin(temp):
    """docstring for celtokelvin"""
    
def kelvintocel(temp):
    """docstring for kelvintocel"""
    
def currency(price):
    convert = 0.00
    tableau = list(price)
    if len(tableau) == 6:
        tableau[5] = tableau[5].lower()
        seq = [tableau[0],tableau[1],'.',tableau[3],tableau[4]]
        prix = float("".join(seq))
        if tableau[5] == "e":
            convert = prix / 0.878144
            final = str(round(convert, 2)) + ' $'
        elif tableau[5] == "d":
            convert = prix * 0.878144
            final = str(round(convert, 2)) + ' €'

    print(final)
    
# Author : Antoine Scherrer <antoine.scherrer@lecol-ldlc.com>
# Licence : GPL
# Boucle pour permetre à l'utilsateur de convertir plusieurs nombres
while True:
    # demande à l'utilisateur le type de conversion qu'il souhaite
    print ("""Le CONVERTISSEUR""")
    print("")
    choice = int(input(" - Tapez 1 pour convertir un nombre décimal en binaire\n - Tapez 2 pour convertir un nombre binaire vers un nombre décimal\n - Tapez 3 avoir un texte en rot13\n - Tapez 4 pour convertir des dollars en euros\n\n - Tapez 0 pour quitter\n\n Faites votre choix : "))
    if choice == 1:
        value = int(input("Which number do you want to convert ?"))
        dectobin(value)
    elif choice == 2:
        bin_string = input("Which binary string do you want to convert ?")
        bintodec(bin_string)
    elif choice == 3:
        text = raw_input("Tapez le texte à tourner de 13 charactères... : ")
        rot13(text)
    elif choice == 4:
        price = raw_input("Merci d'entrez un prix en avec la première lettre de la monaie (e ou d) à la fin du prix : 14.50e ou 08.30d : ")
        currency(price)
    elif choice == 0:
        exit("Interruption demandé par l'utilisateur")
