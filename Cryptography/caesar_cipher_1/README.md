# caesar cipher 1
__Category:__ Cryptography  
__Points:__ 150

### Problem:

This is one of the older ciphers in the books, can you decrypt the [message](ciphertext)? You can find the ciphertext in /problems/caesar-cipher-1_1_6fbf7a9ce0aac23bab1c37836cc20c3b on the shell server.

##### Hints:
> caesar cipher [tutorial](https://learncryptography.com/classical-encryption/caesar-cipher)

### Solution:

For this problem I created a python script to decrypt the message (although a caesar cipher can easily be cracked by hand too!).

The script is available at [https://github.com/craitano/Caesar-Cipher-Encryptor-Decryptor](https://github.com/craitano/Caesar-Cipher-Encryptor-Decryptor "Caesar cipher encryption/decryption tool")

Since the shift isn't given it is easiest to run it using the -a argument to see all 25 possible decryptions as follows:

```Bash
caesar.py -a
```

Enter the ciphertext "vgefmsaapaxpomqemdoubtqdxoaxypeo" and hit enter.
Look at the output to find one that spells out a message (justagoodoldcaesarcipherlcolmdsc).

### Flag:

picoCTF{justagoodoldcaesarcipherlcolmdsc}

