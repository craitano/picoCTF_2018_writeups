# assembly-1
__Category:__ Reverse Engineering   
__Points:__ 200

### Problem:

What does asm1(0x15e) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. [Source](eq_asm_rev.S) located in the directory at /problems/assembly-1_3_cfc4373d0e723e491f368e7bcc26920a

##### Hints:
> assembly [conditions](https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm)

### Solution:

This question requires a basic understanding of assembly (specifically x86 with Intel syntax) to solve.
Here is a brief description of what each line in the asm0 function does:

```Assembly
asm1:
	push	ebp                      ; put rthe base pointer on the stack
	mov	ebp,esp                  ; move the base pointer to the stack pointer
	cmp	DWORD PTR [ebp+0x8],0xdc ; compare the first parameter to 0xdc
	jg 	part_a	                 ; if it is greter than 0xdc then jump to part_a
	cmp	DWORD PTR [ebp+0x8],0x8  ; compare the first parameter to 0x8
	jne	part_b                   ; if it is not equal to 0x8 then jump to part_b
	mov	eax,DWORD PTR [ebp+0x8]  ; move the first parameter into register eax
	add	eax,0x3                  ; add 0x3 to register eax
	jmp	part_d                   ; jump to part_d
part_a:
	cmp	DWORD PTR [ebp+0x8],0x68 ; compare the first parameter to 0x68
	jne	part_c                   ; if it is not equal to 0x86 then jump to part_c
	mov	eax,DWORD PTR [ebp+0x8]  ; move the first parameter into eax
	sub	eax,0x3                  ; subtract 0x3 from eax
	jmp	part_d                   ; jump to part_d
part_b:
	mov	eax,DWORD PTR [ebp+0x8]  ; move the first parameter into register eax
	sub	eax,0x3                  ; subtract 3 from register eax
	jmp	part_d                   ; jump to part_d
  
  ;These next 5 lines will never be reached
	cmp	DWORD PTR [ebp+0x8],0xfc
	jne	part_c 
	mov	eax,DWORD PTR [ebp+0x8] 
	sub	eax,0x3 
	jmp	part_d
part_c:
	mov	eax,DWORD PTR [ebp+0x8]  ; move the first parameter into register eax
	add	eax,0x3                  ; add 0x3 to register eax
part_d:
	pop	ebp                      ; restore the base pointer
	ret                              ; return the value in register eax
```
The first cmp will result with 0x15e > 0xdc so it will jump to part_a. The cmp in part a willl then result with 0x15e not equal to 0x68 so it will jump to part_c. Part c will then add 0x3 and store the result (0x161) in eax. The program then continues into part_d and returns this value.


### Flag:
0x161
