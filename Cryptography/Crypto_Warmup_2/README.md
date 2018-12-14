# Crypto Warmup 2
__Category:__ Cryptography  
__Points:__ 75

### Problem:

Cryptography doesn't have to be complicated, have you ever heard of something called rot13? `cvpbPGS{guvf_vf_pelcgb!}`

##### Hints:
> This can be solved online if you don't want to do it by hand!

### Solution:

Enter the encrypted flag in an online rot13 decryption tool or use the following python 3 script.

```Python
msg = str(input("Message: ")).lower()
out = ""

# encrypt/decrypt
for i in range(0, len(msg)):
    val = ord(msg[i])
    if(val > 96 and val < 123):
        val -= 83
        val %= 26
        val += 96
    out += chr(val)
print(out)
```

### Flag:

picoCTF{this_is_crypto!}

