# absolutely relative
__Category:__ General Skills   
__Points:__ 250

### Problem:

In a filesystem, everything is relative ¯\\_(ツ)_/¯. Can you find a way to get a flag from this [program](absolutely-relative)? You can find it in /problems/absolutely-relative_3_c1a43555f1585c98aab8d5d2c7f0f9cc on the shell server. [Source](absolutely-relative.c).

##### Hints:
> Do you have to run the program in the same directory? (⊙.☉)7

> Ever used a text editor? Check out the program 'nano'

### Solution:

I started by trying to run the program on the shell server, and got a message that I don't have permission to view the flag. I then decided to look at the source.

After a quick look at the source it seems a permissions.txt file containing "yes" is required in order to get the flag. I tried creating this file here, but didn't have permission to create it since it is a shared folder.

I then navigated to my home directory, created the file, and executed teh program using the absolute filepath to get the flag.

```Bash
$ cd ~
$ echo "yes" > permission.txt           
$ /problems/absolutely-relative_3_c1a43555f1585c98aab8d5d2c7f0f9cc/absolutely-relative 
```

### Flag:

picoCTF{3v3r1ng_1$_r3l3t1v3_6193e4db}
