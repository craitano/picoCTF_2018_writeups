# environ
__Category:__ General Skills  
__Points:__ 150

### Problem:

Sometimes you have to configure environment variables before executing a program. Can you find the flag we've hidden in an environment variable on the shell server?

### Solution:

First I logged in on the shell server. Then I used the printenv command to get all of the environment variables. I piped this output to grep to search for the flag as follows:

```Bash
printenv | grep picoCTF
```

### Flag:

picoCTF{eNv1r0nM3nT_v4r14Bl3_fL4g_3758492}

