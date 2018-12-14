# strings
__Category:__ General Skills  
__Points:__ 100

### Problem:

Can you find the flag in this [file](strings) without actually running it? You can also find the file in /problems/strings_2_b7404a3aee308619cb2ba79677989960 on the shell server.

##### Hints:
> [strings](https://linux.die.net/man/1/strings)

### Solution:

After downloading the file I used the strings utility to extract all of the strings then pipelined the output to grep to find the flag. The command is as follows:

```bash
strings strings | grep picoCTF
```

### Flag:

picoCTF{sTrIngS_sAVeS_Time_3f712a28}

