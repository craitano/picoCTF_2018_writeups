# hex editor
__Category:__ Forensics  
__Points:__ 150

### Problem:

This [cat](hex_editor.jpg) has a secret to teach you. You can also find the file in /problems/hex-editor_3_086632ac634f394afd301fb6a8dbadc6 on the shell server.

##### Hints:
> What is a hex editor?

> Maybe google knows.

> [xxd](http://linuxcommand.org/man_pages/xxd1.html)

> [hexedit](http://linuxcommand.org/man_pages/hexedit1.html)

> [bvi](http://manpages.ubuntu.com/manpages/natty/man1/bvi.1.html)

### Solution:

I downloaded the cat picture and opened it in a hex editor. I then searched for the string "picoCTF" which brought me right to the flag. 

### Flag:

picoCTF{and_thats_how_u_edit_hex_kittos_8BcA67a2}

