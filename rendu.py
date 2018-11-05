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
# Functions start

# Function permit to clear the screen with the number of line which are indicate in the attribute
def blank(lignes):
    for i in range(lignes): #
        print("")
    return 0

# Function reproduce the pause() function in C
def pause():
    input()
    return 0

# Function to convert the decimal numbers into binary numbers
def dectobin(value):
    digits = []  # Init the list digit, where we will store the convert number
    while value > 0:  # while the value not reached 0 do :
        digits.append(value % 2)  # Value modulo 2 into the list
        value = value // 2  # Value divide 2 int value into value
    digits.reverse()  # Reverse the order of the list
    print("".join([str(d) for d in digits]))  # Print all the digits of the list
    pause()
    blank(30)
    return 0

# Function permit to convert binary string into a decimal number
def bintodec(bin_string):
    result = 0
    for i in range(len(bin_string)):
        char = int(bin_string[i])  # var char will contain the bin string of the increment
        if char == 1: 
            result += 2 ** (len(bin_string) - 1 - i)  # If char is =1 the result will be reuslt + 2power (len of the bin string -1 -i)
    print("The result is : ", result)  # Print the resulat
    pause()
    blank(30)
    return 0

# Function which permit to make a ROT13 of a sentence
def rot13(text):
    tableau = list(text)  # Start a list with all the letters of the text into the one cell
    for i in range(len(text)):
        tableau[i] = ord(tableau[i])  # get the ascii value of the character in the i cell
        if ((tableau[i] >= ord("a") and tableau[i] <= ord('m')) or
                (tableau[i] >= ord("A") and tableau[i] <= ord("M"))):  # if the ascii ascii character is between the ascii value of A and M or a and m
            tableau[i] += 13  # Add 13 to Ascii number for example ==> M =ascii77 ==> 77+13 = 90 ==> ascii value of 90 = Z
        elif ((tableau[i] > ord("m") and tableau[i] <= ord('z')) or
        (tableau[i] > ord('M') and tableau[i] <= ord('Z'))):# Same but -13 to get the good character but between n and z or N and Z For example N = ascii78 --> 78+13 = 91 ascii91 ==> [  ==> not the good result.

            tableau[i] -= 13
    for i in range(len(text)):
        tableau[i] = chr(tableau[i]) # convert i ascii value into a character
    print(''.join(tableau)) # Join the list to have a complete list of convert characters
    pause()
    blank(30)
    return 0

# Function permit to convert a temeprature in kelvin, farenheit or celcius in the the others temperatures
def tempconvert(temp):
    tableau = list(temp)  # define a list with the attributeibuts values
    unite = tableau[len(tableau) - 1].lower() # Take the last character of the list and make this character lower and store him into the var
    del tableau[len(tableau) - 1]  # Del the last character and delete it to the list
    temperature = float("".join(tableau))  # Join all the other characters of list and make them as a float
    if unite == "c":  # If the last character is a c the temperature enter is in Celcius
        print("La température saisie est : %0.2f °C" % temperature)
        print(temperature, end='')
        print(" °C --> %0.2f °K" % (temperature + 273.15))  # print the kelvin temperature
        print(temperature, end='')
        print(" °C --> %0.2f °F" % (temperature * 1.8000 + 32.00))  # Print the farenheit temperature

    elif unite == "k":  # if the temperature is in kelvin
        print("La température saisie est : %0.2f °K" % temperature)
        print(temperature, end='')
        print(" °K --> %0.2f °F" % ((temperature - 273.15) * 1.8000 + 32.00))  # convert the temperature into farenheit
        print(temperature, end='')
        print(" °K --> %0.2f °C" % (temperature - 273.15))  # convert the température into Celcius
    elif unite == "f":  # if the temperature is in farenheit
        print("La température saisie est : %0.2f °F" % temperature)
        print(temperature, end='')
        print(" °F -->", round(((temperature + 459.67) * (5 / 9)), 2), " °K") # convert the temperature in kelvin
        print(temperature, end='')
        print(" °F --> %0.2f °C" % ((temperature - 32) / 1.8000))  # convert the temperature in Celcius
    pause()
    blank(30)
    return 0

# Function permit to convert euro to dollar or dollar to euro
def currency(price):
    convert = 0.00
    tableau = list(price)  # take the last character of the list to have the actual currency
    if len(tableau) == 6:  # if the lenght of the entry is of 6 characters we can continue
        tableau[5] = tableau[5].lower()  # Make the last character lower
        seq = [tableau[0], tableau[1], '.', tableau[3], tableau[4]]  # get the price without the currency
        prix = float("".join(seq))  # convert the price in float
        if tableau[5] == "e":  # if the actual currency is in euros :
            convert = prix / 0.878144  # convert the price in dollar with currecny change
            final = str(round(convert, 2)) + ' $ (Taux de change au 03/11/2018)'  # store the convert price
        elif tableau[5] == "d":  # if the actual money is in dollars
            convert = prix * 0.878144  # Convert the price in euros with currency change
            final = str(round(convert, 2)) + ' € (Taux de change au 03/11/2018)'  # store the new price convert

    print(final)  # print the final price
    pause()
    blank(30)
    return 0

# Function permit to add or subtract the VAT to a price
def TVA_Adder(price,type_prix,cat_tva):
    tva = 0
    # condition of the VAT rate
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
        print("Le prix sans TVA est de :", round(price/(1+(tva/100)),2), "€ HT")  # Convert the price without VAT
    elif type_prix == 2: # prix en HT à convertir en TTC
        print("Le prix entré est", round(price,2), "€ HT, la TVA à ajouter est de", tva, "%")
        print("Le prix avec TVA est de :", round(price*(1+(tva/100)), 2), "€ TTC")  # convert the price with VAT
    else:
        print("Erreur : Votre prix n'est pas TTC ou HT merci de réessayer.")  # Error message
    pause()
    blank(30)
    return 0

# Function permit to convert a RGB color into CMYK and hex color
def rgbtocmyk(R, G, B):
    C = 1 - (R / 255)  # convert the Red into cyan
    M = 1 - (G / 255)  # convert the Green into magenta
    Y = 1 - (B / 255)  # convert the blue in yellow

    var_K = 1  # init the K at 1

# Those conditions permit to define the K colors.
    if (C < var_K):
        var_K = C

    if (M < var_K):
        var_K = M

    if (Y < var_K):
        var_K = Y

    if (var_K == 1): # only black
        C = 0
        M = 0
        Y = 0

    else:
        C = ( C - var_K ) / ( 1 - var_K )
        M = ( M - var_K ) / ( 1 - var_K )
        Y = ( Y - var_K ) / ( 1 - var_K )

    K = var_K

    print ("Votre couleur RGB (", R, G, B, ") est désormais convertis en :")
    print(" - CMJN : ", round(C*100) , round(M*100) , round(Y*100) , round(K*100))  # print the CMYK color

    R_hex = str(hex(R))  # convert into string the hex value of R
    G_hex = str(hex(G))  # convert into string the hex valeu of G
    B_hex = str(hex(B))  # convert into string the hex value of B
    hexa = "#" + R_hex[2:] + G_hex[2:] + B_hex[2:]  # Print the 2 last character of the R G and B vars

    print(" - Hexadécimal : ", hexa.upper(), end="")  #print hexa color
    pause()
    blank(30)
    return 0
# Functions finish


# Start program
# Infinite while
while True:
    print("""Le CONVERTISSEUR""")
    print("")
    choice = int(input(
        " - Tapez 1 pour convertir un nombre décimal en binaire\n - Tapez 2 pour convertir un nombre binaire vers un nombre décimal\n - Tapez 3 avoir un texte en rot13\n - Tapez 4 pour convertir des dollars en euros\n - Tapez 5 pour convertir une température\n - Tapez 6 pour convertir des prix en TTC ou HT\n - Tapez 7 pour convertir une couleur RGB en CMJN et hexadécimal\n\n - Tapez 0 pour quitter\n\n Faites votre choix : "))  # get the choice of the user
    if choice == 1:  # THe dectobin
        value = int(input("Quel nombre voulez vous convertir ?"))  # enter the dec value
        dectobin(value)  # print the bin value
    elif choice == 2:  # The bintodec
        bin_string = input("Quel nombre binaire voulez vous convertir ?")  # get the bin number
        bintodec(bin_string)  # print the dec number
    elif choice == 3:  # rot13
        text = input("Tapez le texte à tourner de 13 charactères... : ")  # enter the sentence to convert in rot13
        rot13(text)  # return the rot13 valuee
    elif choice == 4:  # currency converter
        price = input(
            "Merci d'entrez un prix en avec la première lettre de la monaie (e ou d) à la fin du prix : 14.50e ou 08.30d : ")  # get the price to convert
        currency(price)  # print the convert price
    elif choice == 5:  # temeprature convert
        temp = input(
            "Merci d'entrez une température décimale avec son unité (Celcius =c, kelvin = k, farenheit = f) : ")  # get the temp
        tempconvert(temp)  # print the convert temp
    elif choice == 6:
        price = float(input("Merci d'entrez un prix... : "))  # Enter the price
        HT_TTC = int(input("Produit TTC tapez 1 ou produit HT tapez 2 : "))  # choice type of price
        cat_tva = float(input("Pour une TVA à :\n - 5.5% tapez 1\n - 10% tapez 2\n - 20 % tapez 3\n Pour un autre taux tapez le ici : "))  # choose vat rate
        TVA_Adder(price, HT_TTC, cat_tva)  # print the new price
    elif choice == 7:  # CMJN HEX RGB CONVERTER
        while True:  # Infinite while
            print("Merci d'entrez les couleurs à convertir : ")
            R = int(input("ROUGE : "))  # enter the Red
            G = int(input("VERT : "))  # enter the Green
            B = int(input("BLEU : "))  # enter the blue
            if (R > 255 or R < 0 or G > 255 or G < 0 or  B > 255 or B < 0):  # if the entered value is over 255 or under 0
                print("erreur, la valeur saisie est incorrect")  # Print errror
                pause()
            else:
                rgbtocmyk(R, G, B)  # print the convert values
                break
    elif choice == 0:
        exit("Interruption demandé par l'utilisateur")
# End of the program
