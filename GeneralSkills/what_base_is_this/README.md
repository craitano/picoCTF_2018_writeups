# what base is this?
__Category:__ General Skills   
__Points:__ 200

### Problem:

To be successful on your mission, you must be able read data represented in different ways, such as hexadecimal or binary. Can you get the flag from this program to prove you are ready? Connect with nc 2018shell3.picoctf.com 64706.

##### Hints:
> I hear python is a good means (among many) to convert things.

> It might help to have multiple windows open

### Solution:

For this I created a python script which takes the numbers as command line arguments and attempts to convert them to asscii interpreting them as each binary, octal, decimal and hexidecimal.

```Python
#!/usr/bin/env python3

import sys

def to_ascii(data, base, num_chars):
  word = ""
  try:
    while(len(data) % num_chars > 0):
      data = '0' + data
    for i in range(int(len(data) / num_chars)):
      word += chr(int(data[i*num_chars:(i+1)*num_chars], base))
    return word
  except:
    return ""

bin_word = ""
oct_word = ""
dec_word = ""
hex_word = ""
for i, arg in enumerate(sys.argv):
  if i > 0:
    bin_word += to_ascii(arg, 2, 8)
    oct_word += to_ascii(arg, 8, 3)
    dec_word += to_ascii(arg, 10, 3)
    hex_word += to_ascii(arg, 16, 2)
print("binary: " +  bin_word) 
print("octal: " + oct_word)
print("decimal: " + dec_word)
print("hexidecimal: " + hex_word)

```

I saved this file as [2ascii](2ascii) and ran it on each sequence of numbers given.

```bash 
./2ascii 01100111 01101001 01101101 01110000
binary: gimp
octal: @IAAAH
decimal: doeeen
hexidecimal: 
$./2ascii 646f63746f72
binary: 
octal: 
decimal: 
hexidecimal: doctor
$./2ascii 160 150 157 156 145
binary: 
octal: phone
decimal:  
hexidecimal: `PWVE
```

It should be obvious which base is correct (first is binary, second is hex, third is octal). Answering all three correctly gives the flag.
### Flag:

picoCTF{delusions_about_finding_values_5b21aa05}
