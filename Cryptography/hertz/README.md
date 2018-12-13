# hertz
__Category:__ Cryptography  
__Points:__ 150

### Problem:

Here's another simple cipher for you where we made a bunch of substitutions. Can you decrypt it? Connect with `nc 2018shell3.picoctf.com 48487`

##### Hints:
> NOTE: Flag is not in the usual flag format

### Solution:

Entering the given command in a terminal provided a bunch of [ciphertext](don_quixote_ciphertext). I assumed it was a substitution cipher based on the problem statement.

I solved this using a substitution cipher tool at [https://www.dcode.fr/monoalphabetic-substitution](https://www.dcode.fr/monoalphabetic-substitution) and selecting "Manual decryption." After putting in the cipher and clicking the "Decypt" button I began filling in the substitution alphabet. This method is kind of a guess and check type solution but wasn't too difficult to figure out.

I started with the one letter words 'a' and 'i', then from there was easily able to guess words such as 'is', 'an' and 'an'. From there I was pretty easily able to pick out certain words. When I had about 3/4 of the letters filled out I realized the two paragraphs that were given were the first two paragraphs of Don Quixote, by Miguel de Cervantes (apparently reading pays off). I searched for Don Quixote online and quickly filled in the rest to find the flag given at the top.

__Note 1:__ After a second solve I noticed it provided a different [ciphertext](war_and_peace_ciphertext). This one is War and Peace, by Leo Tolstoy. 
__Note 2:__ It seems to use a different alphabet for encryption each time. The alphabets I used (with _ used for unknowns) were "_GOMSUXBPYCAIT_FRENVKHWDLQ" for Don Quixote and "CJSMKL_NPGTOIR_BYVE_WDHAUF" for War and Peace. These will be different however each time a new cipher is retrieved from the server.

### Flag:

picoCTF{substitution_ciphers_are_solvable_osevnhgbri}

