# blaise's cipher
__Category:__ Cryptography   
__Points:__ 200

### Problem:

My buddy Blaise told me he learned about this cool cipher invented by a guy also named Blaise! Can you figure out what it says? Connect with nc 2018shell3.picoctf.com 11281.

##### Hints:
> There are tools that make this easy.

> This cipher was NOT invented by Pascal

### Solution:

I started with a quick google search for "Blaise cipher." This came up with a bunh of results for the vignère cipher (invented by Blaise de Vigenère).
I then connected to the given port to get the [ciphertext](ciphertext).
I used a online [vignere decoder](https://www.dcode.fr/vigenere-cipher) and selected the "try to decrypt automatically (statisttical analysis)". 
The first option that came up looked correct with the key "FLAG". I then used this key to decrypt the ciphertext and found the flag in the [text](message).

### Flag:

picoCTF{v1gn3r3_c1ph3rs_ar3n7_bad_5352bf72}
