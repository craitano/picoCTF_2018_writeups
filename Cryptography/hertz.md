# hertz
__Category:__ Cryptography
__Points:__ 150

### Problem:

Here's another simple cipher for you where we made a bunch of substitutions. Can you decrypt it? Connect with `nc 2018shell3.picoctf.com 48487`

### Solution:

Entering the given command in a terminal provided a bunch of ciphertext. I assumed it was a substitution cipher based on the problem statement.

I solved this using a substitution cipher tool at [https://www.dcode.fr/monoalphabetic-substitution](https://www.dcode.fr/monoalphabetic-substitution) and selecting "Manual decryption." After putting in the cipher and clicking the "Decypt" button I began filling in the substitution alphabet. This method is kind of a guess and check type solution but wasn't too difficult to figure out.

I started with the one letter words 'a' and 'i', then from there was easily able to guess words such as 'is', 'an' and 'an'. From there I was pretty easily able to pick out certain words. When I had about 3/4 of the letters filled out I realized the 2 paragraphs that were given were the first 2 paragraphs of Don Quixote (apparently reading pays off). I searched for Don Quixote online and quickly filled in the rest to find the flag given at the top.

### Flag:

picoCTF{substitution_ciphers_are_solvable_osevnhgbri}

