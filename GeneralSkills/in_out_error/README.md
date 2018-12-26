# in out error
__Category:__ General Skills   
__Points:__ 275

### Problem:

Can you utlize stdin, stdout, and stderr to get the flag from this [program](in-out-error)? You can also find it in /problems/in-out-error_0_0f875f7714b995dad5946a15be6267a7 on the shell server

##### Hints:
> Maybe you can split the stdout and stderr output?

### Solution:

I ran the program from my home directory, redirecting stdout and stderr to separeate files.

```Bash
$ /problems/in-out-error_0_0f875f7714b995dad5946a15be6267a7/in-out-error > out.txt 2> err.txt
```

THe program seemed to hang so I used ctrl+c to kill it, then viewed err.txt and out.txt. Nothing seems to have been printed to stderr, but the following was printed to stdout:

```
Hey There!
If you want the flag you have to ask nicely for it.
Enter the phrase "Please may I have the flag?" into stdin and you sh
all receive.
```

I then reran the program also echoing in "Please may I have the flag?".

__Note:__ The program crashes if run from the home directory. Make sure to run it in the problem directory and send it to a file in your home directory.

```Bash
$ echo "Please may I have the flag?" | ./in-out-error > ~/out.txt 2> ~/err.txt
```

Now stderr contains the flag (repeated a bunch of times for me, but I'm not sure if thats how it is supposed to be).

### Flag:

picoCTF{p1p1ng_1S_4_7h1ng_85f6fd2c}
