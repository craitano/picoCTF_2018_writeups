# General Warmup 3
__Category:__ General Skills  
__Points:__ 50

### Problem:

What is 0x3D (base 16) in decimal (base 10).

##### Hints:
> Submit your answer in our competition's flag format. For example, if you answer was '22', you would submit 'picoCTF{22}' as the flag.

### Solution:

Use a hex to decimal coverter to convert 3D to decima or use the following bash command:

```Bash
echo "ibase=16;3D" | bc
```

### Flag:

picoCTF{61}

