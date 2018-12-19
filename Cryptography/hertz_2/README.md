# hertz 2
__Category:__ Cryptography   
__Points:__ 200

### Problem:

This flag has been encrypted with some kind of cipher, can you decrypt it? Connect with nc 2018shell3.picoctf.com 12521

##### Hints:
> These kinds of problems are solved with a frequency that merits some analysis.

### Solution:

I connected to the given port to get the [ciphertext](ciphertext). I guessed this might have used a substitution cipher (and it did).
I used an [online](https://www.guballa.de/substitution-solver) decoder to get the [plaintext](message) which contained the flag. 

### Flag:

picoCTF{substitution_ciphers_are_too_easy_uwhufbnnyu}
