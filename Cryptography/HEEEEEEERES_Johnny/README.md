# HEEEEEEERE'S Johnny!
__Category:__ Cryptography  
__Points:__ 100

### Problem:

Okay, so we found some important looking files on a linux computer. Maybe they can be used to get a password to the process. Connect with `nc 2018shell2.picoctf.com 5221`. Files can be found here: [passwd](passwd) [shadow](shadow).

##### Hints:
> If at first you don't succeed, try, try again. And again. And again.

> If you're not careful these kind of problems can really "rockyou".

### Solution:

For this problem I used John The Ripper, a popular password cracking tool for Unix/Linux. After installing it I downloaded the given shadow file and ran the comand:

```bash
john shadow
```

This revealed the password "kissme" for the root account

I then connected to 2018shell2.picoctf.com:5221 and logged in as root with this password to get the flag.

### Flag:

picoCTF{J0hn_1$_R1pp3d_289677b5}

