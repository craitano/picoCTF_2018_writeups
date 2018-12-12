# Crypto Warmup 1
__Category:__ Cryptography
__Points:__ 75

### Problem:

Crpyto can often be done by hand, here's a message you got from a friend, llkjmlmpadkkc with the key of thisisalilkey. Can you use this table to solve it?.

### Solution:

This uses a one-time pad so you can use an online one-time pad decryption tool or use the following python 3 script:

```Python
enc = ""
while(enc != "e" and enc != "d"):
    enc = str(input("Enter e to encrypt, or d to decrypt: ")).lower()
msg = str(input("Message: ")).lower()
key = str(input("Key: ")).lower()
out = ""
# encrypt/decrypt
for i in range(0, len(msg)):
    valk = ord(msg[i]) - 96
    valm = ord(key[i]) - 96
    val =  valk + valm if enc == "e" else  valk + 26 - valm
    val %= 26
    val +=  95 if enc == "e" else 97
    out += chr(val)
print(out)
```

Alternatively if you would like to use the given table, find the column for the first character of the message then find the first letter of the key within that column. The first letter of the flag will be the label for this row. Repeat this for the remaining letters in the message/key to get all of the letters in the flag.

Make sure to enter the flag in all caps. 

### Flag:

picoCTF{SECRETMESSAGE}

