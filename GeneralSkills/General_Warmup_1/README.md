# General Warmup 1
__Category:__ General Skills  
__Points:__ 50

### Problem:

If I told you your grade was 0x41 in hexadecimal, what would it be in ASCII?

##### Hints:
> Submit your answer in our competition's flag format. For example, if you answer was 'hello', you would submit 'picoCTF{hello}' as the flag.

### Solution:

Use a hex to ascii converter to get the flag or use the following bash command:

```Bash
echo 0x41 | xxd -r; echo
```

### Flag:

picoCTF{A}
