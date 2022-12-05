import os
from random import randint

#definition der Walzen

steckbrett_front    = "RCVFIAKDTOQMUEXBPLJG"
steckbrett_back     = "CRFVAIDKOTMQEUBXLPGJ"

walze_UKW_back      = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
walze_UKW_front     = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

walze_two_back      = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
walze_two_front     = "AJDKSIRUXBLHWTMCQGZNPYFVOE"

walze_three_back    = "BCDEFGHIJKLMNOPQRSTUVWXYZA"
walze_three_front   = "DFHJLCPRTXVZNYEIWGAKMUSQOB"

walze_five_back     = "DEFGHIJKLMNOPQRSTUVWXYZABC"
walze_five_front    = "RGITYUPSDNHLXAWMJQOFECKVZB"

walze_before        = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Einlegen der Walzen in die 3 Fächer
# Gezählt von UKW zu Steckbrett
#geenau
walze_3_front   = walze_five_front
walze_3_back    = walze_five_back
walze_2_front   = walze_three_front
walze_2_back    = walze_three_back
walze_1_front   = walze_two_front
walze_1_back    = walze_two_back

def change(buchstabe, rein, raus):
    return raus[rein.index(buchstabe)]

def encrypt(msg_):
    encrypted = ""
    msg = ""
    for char in msg_:
        if char.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            msg += char

    for char in msg.upper():
        # print(char)
        if char in steckbrett_front:
            #print("in Steckbrett")
            nach_steckbrett = change(char, steckbrett_front, steckbrett_back)
        else:
            #print("nicht in steckbrett")
            nach_steckbrett = char
        #print(nach_steckbrett)
        nach_frontwalze = change(nach_steckbrett, walze_before, walze_3_front)
        #print(nach_frontwalze)
        nach_walze_3 = change(nach_frontwalze, walze_3_back, walze_2_front)
        #print(nach_walze_3)
        nach_walze_2 = change(nach_walze_3, walze_2_back, walze_1_front)
        #print(nach_walze_2)
        nach_walze_1 = change(nach_walze_2, walze_1_back, walze_UKW_front)
        #print(nach_walze_1)

        nach_UKW = change(nach_walze_1, walze_UKW_back, walze_UKW_front)
        #print(nach_UKW)
        out_walze_1 = change(nach_UKW, walze_UKW_front, walze_1_back)
        #print(out_walze_1)
        out_walze_2 = change(out_walze_1, walze_1_front, walze_2_back)
        #print(out_walze_2)
        out_walze_3 = change(out_walze_2, walze_2_front, walze_3_back)
        #print(out_walze_3)
        out_before = change(out_walze_3, walze_3_front, walze_before)
        #print(out_before)
        if out_before in steckbrett_back:
            out_steckbrett = change(out_before, steckbrett_back, steckbrett_front)
        else:
            out_steckbrett = out_before

        if len(encrypted) % 6 == 0:
            encrypted += " "

        encrypted += out_steckbrett
    return encrypted

while True:
    eingabe = input(">")
    if eingabe != "exit":
        print(encrypt(eingabe))
    else:
        print("Exit...")
        break

