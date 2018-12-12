# Reading Between the Eyes
__Category:__ Forensics
__Points:__ 150

### Problem:

Stego-Saurus hid a message for you in this [image](https://2018shell3.picoctf.com/static/3e423171eed198e8425524a1b052869b/husky.png), can you retreive it?

Solution:

This problem uses lsb steganography with data hidden in the r, g, and b channels.
By looking at the least significant bits you can extract an ascii encoded string and convert it to text to get the flag.

I created a python 3 stegonagraphy tool to achieve this and have made it available at [https://github.com/craitano/LSB-Stegonography](https://github.com/craitano/LSB-Stegonography "LSB steganography tool")

Just place the picture in the same directory as the script and run this command: 
```Bash
./lsbsteg husky.png
```
Flag:

picoCTF{r34d1ng_b37w33n_7h3_by73s}

