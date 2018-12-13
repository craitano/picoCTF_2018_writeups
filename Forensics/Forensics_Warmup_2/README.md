# Forensics Warmup 2
__Category:__ Forensics  
__Points:__ 50

### Problem:

Hmm for some reason I can't open this [PNG](flag.png)? Any ideas?

##### Hints:
> How do operating systems know what kind of file it is? (It's not just the ending!)
> Make sure to submit the flag as picoCTF{XXXXX}

### Solution:

When I downloaded the image it was named "flag.png". Based on the hint I'd assume the download is supposed to be named "flag" without the file extension. If this is the case rename it with a .png extension. Open the image in an image viewer to see the flag.

### Flag:

picoCTF{extensions_are_a_lie}

