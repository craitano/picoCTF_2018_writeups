# assembly-0
__Category:__ Reverse Engineering  
__Points:__ 150

### Problem:

What does asm0(0xd8,0x7a) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](https://2018shell3.picoctf.com/static/05434007b9c46274206db32fa32a3595/intro_asm_rev.S) located in the directory at /problems/assembly-0_1_fc43dbf0079fd5aab87236bf3bf4ac63.

Solution:

This question requires a basic understanding of assembly (specifically x86 with Intel syntax) to solve.
Here is a brief description of what each line in the asm0 function does:

```Assembly
push ebp                    ; Store the base pointer on the stack so it can be restored at the end of the function
mov ebp, esp                ; Set the base pointer address to the top of the stack. This is the bottom of the stack frame for this function
mov eax,DWORD PTR[ebp+0x8]  ; Store the first parameter in register eax
mov ebx, DWORD PTR[ebp+0xc] ; Store the second parameter in register ebx
mov eax,ebx                 ; Move the value stored in register ebx into register eax
mov esp,ebp                 ; Restore the stack pointer, esp
pop ebp                     ; Restore the base pointer, ebp
ret                         ; Return from the function
```

As a convention, the return value of a function is whatever eax contains when the function returns. In this case eax contains the value of the second parameter, 0x7a


Flag:

0x7a

