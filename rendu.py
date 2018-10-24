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
# Author : Antoine Scherrer <antoine.scherrer@lecol-ldlc.com>
# Licence : GPL
# Boucle pour permmetre à l'utilsateur de convertir plusieurs nombres
while True:
    # demande à l'utilisateur le type de conversion qu'il souhaite
    choice = int(input("What do you want to do ? 1: decimal to binary, 2: binary to decimal"))
    if choice == 1:
        value = int(input("Which number do you want to convert ?"))
        digits = []
        while value > 0:
            digits.append(value % 2)
            value = value // 2
        digits.reverse()
        print("".join([str(d) for d in digits]))
    elif choice == 2:
        bin_string = input("Which binary string do you want to convert ?")
        result = 0
        for i in range(len(bin_string)):
            char = int(bin_string[i])
            if char == 1:
                result += 2 ** (len(bin_string) - 1 - i)
        print("The result is : ", result)
