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

def blank(lignes):
    """docstring for blank"""
    for i in range(lignes):
        print("")


def pause():
    """docstring for pause"""
    input()


def dectobin(value):
    digits = []
    while value > 0:
        digits.append(value % 2)
        value = value // 2
    digits.reverse()
    print("".join([str(d) for d in digits]))
    pause()
    blank(30)


def bintodec(bin_string):
    result = 0
    for i in range(len(bin_string)):
        char = int(bin_string[i])
        if char == 1:
            result += 2 ** (len(bin_string) - 1 - i)
    print("The result is : ", result)
    pause()
    blank(30)


def rot13(text):
    tableau = list(text)
    for i in range(len(text)):
        tableau[i] = ord(tableau[i])
        if ((tableau[i] >= ord("a") and tableau[i] <= ord('m')) or
                (tableau[i] >= ord("A") and tableau[i] <= ord("M"))):
            tableau[i] += 13
        elif ((tableau[i] > ord("m") and tableau[i] <= ord('z')) or
              (tableau[i] > ord('M') and tableau[i] <= ord('Z'))):
            tableau[i] -= 13
    for i in range(len(text)):
        tableau[i] = chr(tableau[i])
    print(''.join(tableau))
    pause()
    blank(30)


def tempconvert(temp):
    tableau = list(temp)
    unite = tableau[len(tableau) - 1].lower()
    del tableau[len(tableau) - 1]
    temperature = float("".join(tableau))
    if unite == "c":
        print("La température saisie est : %0.2f °C" % temperature)
        print(temperature, end='')
        print(" °C --> %0.2f °K" % (temperature + 273.15))
        print(temperature, end='')
        print(" °C --> %0.2f °F" % (temperature * 1.8000 + 32.00))

    elif unite == "k":
        print("La température saisie est : %0.2f °K" % temperature)
        print(temperature, end='')
        print(" °K --> %0.2f °F" % ((temperature - 273.15) * 1.8000 + 32.00))
        print(temperature, end='')
        print(" °K --> %0.2f °C" % (temperature - 273.15))
    elif unite == "f":
        print("La température saisie est : %0.2f °F" % temperature)
        print(temperature, end='')
        print(" °F -->", round(((temperature + 459.67) * (5 / 9)), 2), " °K")
        print(temperature, end='')
        print(" °F --> %0.2f °C" % ((temperature - 32) / 1.8000))
    pause()
    blank(30)


def currency(price):
    convert = 0.00
    tableau = list(price)
    if len(tableau) == 6:
        tableau[5] = tableau[5].lower()
        seq = [tableau[0], tableau[1], '.', tableau[3], tableau[4]]
        prix = float("".join(seq))
        if tableau[5] == "e":
            convert = prix / 0.878144
            final = str(round(convert, 2)) + ' $ (Taux de change au 03/11/2018)'
        elif tableau[5] == "d":
            convert = prix * 0.878144
            final = str(round(convert, 2)) + ' € (Taux de change au 03/11/2018)'

    print(final)
    pause()
    blank(30)

def TVA_Adder(price,type_prix,cat_tva):
    tva = 0
    if cat_tva == 1: # TVA à 5.5%
        tva = 5.5
    elif cat_tva == 2: # TVA à 10%
        tva = 10
    elif cat_tva == 3: # TVA à 20%
        tva = 20
    else:
        tva = cat_tva

    if type_prix == 1: # prix en TTC à convertir en HT
        print("Le prix entré est", round(price,2), "€ TTC, la TVA à soustraire est de", tva, "%")
        print("Le prix sans TVA est de :", round(price/(1+(tva/100)),2), "€ HT")
    elif type_prix == 2: # prix en HT à convertir en TTC
        print("Le prix entré est", round(price,2), "€ HT, la TVA à ajouter est de", tva, "%")
        print("Le prix avec TVA est de :", round(price*(1+(tva/100)), 2), "€ TTC")
    else:
        print("Erreur : Votre prix n'est pas TTC ou HT merci de réessayer.")
    pause()
    blank(30)
    return 0

while True:
    # demande à l'utilisateur le type de conversion qu'il souhaite
    print("""Le CONVERTISSEUR""")
    print("")
    choice = int(input(
        " - Tapez 1 pour convertir un nombre décimal en binaire\n - Tapez 2 pour convertir un nombre binaire vers un nombre décimal\n - Tapez 3 avoir un texte en rot13\n - Tapez 4 pour convertir des dollars en euros\n - Tapez 5 pour convertir une température\n - Tapez 6 pour convertir des prix en TTC ou HT\n\n - Tapez 0 pour quitter\n\n Faites votre choix : "))
    if choice == 1:
        value = int(input("Which number do you want to convert ?"))
        dectobin(value)
    elif choice == 2:
        bin_string = input("Which binary string do you want to convert ?")
        bintodec(bin_string)
    elif choice == 3:
        text = input("Tapez le texte à tourner de 13 charactères... : ")
        rot13(text)
    elif choice == 4:
        price = input(
            "Merci d'entrez un prix en avec la première lettre de la monaie (e ou d) à la fin du prix : 14.50e ou 08.30d : ")
        currency(price)
    elif choice == 5:
        temp = input(
            "Merci d'entrez une température décimale avec son unité (Celcius =c, kelvin = k, farenheit = f) : ")
        tempconvert(temp)
    elif choice == 6:
        price = float(input("Merci d'entrez un prix... : "))
        HT_TTC = int(input("Produit TTC tapez 1 ou produit HT tapez 2 : "))
        cat_tva = float(input("Pour une TVA à :\n - 5.5% tapez 1\n - 10% tapez 2\n - 20 % tapez 3\n Pour un autre taux tapez le ici : "))
        TVA_Adder(price, HT_TTC, cat_tva)
    elif choice == 0:
        exit("Interruption demandé par l'utilisateur")
