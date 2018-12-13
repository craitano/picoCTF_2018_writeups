# General Warmup 2
__Category:__ General Skills  
__Points:__ 50

### Problem:

Can you convert the number 27 (base 10) to binary (base 2)?

##### Hints:
> Submit your answer in our competition's flag format. For example, if you answer was '11111', you would submit 'picoCTF{11111}' as the flag.

### Solution:

Use a decimal to binary converter to convert 27 to binary or use the following bash command:

```Bash
echo "obase=2;27" | bc
```

### Flag:

picoCTF{11011}

