# Reversing Warmup 1
__Category:__ General Skills  
__Points:__ 75

### Problem:

Can you find the flag in [file](https://2018shell3.picoctf.com/static/6d526817c43e36d4c2dec2b4ea997bfe/file)? This would be really obnoxious to look through by hand, see if you can find a faster way. You can also find the file in /problems/grep-1_4_0431431e36a950543a85426d0299343e on the shell server.

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

