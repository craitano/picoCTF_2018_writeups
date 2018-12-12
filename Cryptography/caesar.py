#!/usr/bin/env python3

__author__ = "Chris Raitano"
__copyright__ = "Copyright 2018, Chris Raitano"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Chris Raitano"

'''
    A caesar cipher encryption/decryption tool
    Optional parameters:
    -a or -all
        output all possible encryptions/decryptions
'''

import sys

# encrypt or decrypt the message using the given shift
def crypt(msg, shift, enc="e"):
    out = ""
    for i in range(0, len(msg)):
        val = ord(msg[i])
        if(val > 96 and val < 123):
            if(enc == "e"):
                val = val -  97 + shift
            else:
                val = val -  97 - shift 
            val %= 26
            val += 97
        out += chr(val)
    return out


all = False
if len(sys.argv) > 1 and (sys.argv[1] == "-a" or sys.argv[1] == "-all"):
    all = True

enc = ""
if not all:
    while(enc != "e" and enc != "d"):
        enc = str(input("Enter e to encrypt, or d to decrypt: ")).lower()
    shift = ""
    while shift == "":
        try:
            shift = int(input("Shift: "))
        except:
            print("Please enter an integer value")
msg = str(input("Message: ")).lower()

if all:
    for i in range(1,26):
        print(crypt(msg, i))
else:
    print(crypt(msg, shift, enc))
