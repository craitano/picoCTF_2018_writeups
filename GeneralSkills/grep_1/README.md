# grep 1
__Category:__ General Skills  
__Points:__ 75

### Problem:

Can you find the flag in [file](file)? This would be really obnoxious to look through by hand, see if you can find a faster way. You can also find the file in /problems/grep-1_4_0431431e36a950543a85426d0299343e on the shell server.

##### Hints:
> grep [tutorial](https://ryanstutorials.net/linuxtutorial/grep.php)

### Solution:

I first tried the following bash command:

```bash
grep flag file
```

This returned no results. Knowing the flag format is picoCTF{<flag>} I then tried this command:

```bash
grep picoCTF file
```

This returned the flag

### Flag:

picoCTF{grep_and_you_will_find_d66382d8}

