# HEEEEEEERE'S Johnny!
__Category:__ Cryptography  
__Points:__ 100

### Problem:

Okay, so we found some important looking files on a linux computer. Maybe they can be used to get a password to the process. Connect with `nc 2018shell2.picoctf.com 5221`. Files can be found here: [passwd](https://2018shell3.picoctf.com/static/0cae99a3ebd7de5e0547e1ff8da980a0/passwd) [shadow](https://2018shell3.picoctf.com/static/0cae99a3ebd7de5e0547e1ff8da980a0/shadow).

### Solution:

For this problem I used John The Ripper, a popular password cracking tool for Unix/Linux. After installing it I downloaded given shadow file and ran the comand:

```bash
john shadow
```

This revealed the password "kissme" for the root account

I then connected to 2018shell2.picoctf.com:5221 and logged in as root with this password to get the flag.

### Flag:

picoCTF{J0hn_1$_R1pp3d_289677b5}

