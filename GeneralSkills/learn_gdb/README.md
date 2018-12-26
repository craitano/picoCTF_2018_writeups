# learn gdb
__Category:__ General Skills   
__Points:__ 300

### Problem:

Using a debugging tool will be extremely useful on your missions. Can you run this [program](run) in gdb and find the flag? You can find the file in /problems/learn-gdb_0_716957192e537ac769f0975c74b34194 on the shell server.

##### Hints:
> Try setting breakpoints in gdb

>Try and find a point in the program after the flag has been read into memory to break on

> Where is the flag being written in memory?

### Solution:

I started by running the program to see what it does then opeining it in gdb.

```Bash
$ ./run
Decrypting the Flag into global variable 'flag_buf'
.....................................
Finished Reading Flag into global variable 'flag_buf'. Exiting.
$ gdb run
```

I disassembled main to find the addres at the end and set a breakpoint there.

```Bash
(gdb) disassemble main
Dump of assembler code for function main:
   0x00000000004008c9 <+0>:     push   %rbp
   0x00000000004008ca <+1>:     mov    %rsp,%rbp
   0x00000000004008cd <+4>:     sub    $0x10,%rsp                   
   0x00000000004008d1 <+8>:     mov    %edi,-0x4(%rbp)              
   0x00000000004008d4 <+11>:    mov    %rsi,-0x10(%rbp)             
   0x00000000004008d8 <+15>:    mov    0x200af9(%rip),%rax        # 
0x6013d8 <stdout@@GLIBC_2.2.5>                                      
   0x00000000004008df <+22>:    mov    $0x0,%ecx                    
   0x00000000004008e4 <+27>:    mov    $0x2,%edx                    
   0x00000000004008e9 <+32>:    mov    $0x0,%esi                    
   0x00000000004008ee <+37>:    mov    %rax,%rdi                    
   0x00000000004008f1 <+40>:    callq  0x400650 <setvbuf@plt>       
   0x00000000004008f6 <+45>:    mov    $0x4009d0,%edi               
   0x00000000004008fb <+50>:    callq  0x400600 <puts@plt>          
   0x0000000000400900 <+55>:    mov    $0x0,%eax                    
   0x0000000000400905 <+60>:    callq  0x400786 <decrypt_flag>      
   0x000000000040090a <+65>:    mov    $0x400a08,%edi               
   0x000000000040090f <+70>:    callq  0x400600 <puts@plt>          
   0x0000000000400914 <+75>:    mov    $0x0,%eax                    
   0x0000000000400919 <+80>:    leaveq                              
   0x000000000040091a <+81>:    retq                                
End of assembler dump.                                              
(gdb) b *0x000000000040091a                                         
Breakpoint 1 at 0x40091a
```

I then ran the program and printed out flag_buf which gave me the flag.

```Bash
(gdb) x/s flag_buf
```

### Flag:

picoCTF{gDb_iS_sUp3r_u53fuL_a6c61d82}
