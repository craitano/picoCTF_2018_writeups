# be-quick-or-be-dead-1
__Category:__ Reverse Engineering   
__Points:__ 200

### Problem:

You find [this](https://www.youtube.com/watch?v=CTt1vk9nM9c) when searching for some music, which leads you to [be-quick-or-be-dead-1](be-quick-or-be-dead-1). Can you run it fast enough? You can also find the executable in /problems/be-quick-or-be-dead-1_2_83a2a5193f0340b364675a2f0cc4d71e.

##### Hints:
> What will the key finally be?

### Solution:

I started off by executing the program and got the following output:

```bash
$./be-quick-or-be-dead-1 
Be Quick Or Be Dead 1
=====================

Calculating key...
You need a faster machine. Bye bye.
```
Since the source was not provided I then decided to disassemble the executable using objdump.

```bash
objdump -d be-quick-or-be-dead-1
```
I started by looking at the main function. I have added comments here to describe the program functionality. Also notice this uses AT&T syntax for x86, while some of the other picoCTF problems use intel syntax.

```Assembly
0000000000400827 <main>:
  # Set up
  400827:	55                   	push   %rbp
  400828:	48 89 e5             	mov    %rsp,%rbp
  
  40082b:	48 83 ec 10          	sub    $0x10,%rsp          # move the stack pointer up 16 bytes
  40082f:	89 7d fc             	mov    %edi,-0x4(%rbp)     # copy the contents of register edi onto the stack 4 bytes above the base
  400832:	48 89 75 f0          	mov    %rsi,-0x10(%rbp)    # copy the contents of register rsi ont the stack 16 bytes above the base (this is where rsp points currently)
  400836:	b8 00 00 00 00       	mov    $0x0,%eax           # set eax to 0
  40083b:	e8 a9 ff ff ff       	callq  4007e9 <header>     # call header()
  400840:	b8 00 00 00 00       	mov    $0x0,%eax           # set eax to 0
  400845:	e8 f8 fe ff ff       	callq  400742 <set_timer>  # call set_timer()
  40084a:	b8 00 00 00 00       	mov    $0x0,%eax           # set eax to 0
  40084f:	e8 42 ff ff ff       	callq  400796 <get_key>    # call get_key()
  400854:	b8 00 00 00 00       	mov    $0x0,%eax           # set eax to 0
  400859:	e8 63 ff ff ff       	callq  4007c1 <print_flag> # call print_flag()
  
  # Clean up
  40085e:	b8 00 00 00 00       	mov    $0x0,%eax
  400863:	c9                   	leaveq 
  400864:	c3                   	retq   
  400865:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
  40086c:	00 00 00 
  40086f:	90                   	nop
```

The calls to get_key() and print_flag() seem important so I looked at those next.

```Assembly
0000000000400796 <get_key>:
  # Set up
  400796:	55                   	push   %rbp
  400797:	48 89 e5             	mov    %rsp,%rbp
  
  40079a:	bf 88 09 40 00       	mov    $0x400988,%edi         # set edi to 0x400988
  40079f:	e8 8c fd ff ff       	callq  400530 <puts@plt>      # Call puts()
  4007a4:	b8 00 00 00 00       	mov    $0x0,%eax              # set eax to 0
  4007a9:	e8 58 ff ff ff       	callq  400706 <calculate_key> # call calculate_key()
  4007ae:	89 05 0c 09 20 00    	mov    %eax,0x20090c(%rip)    # 6010c0 <__TMC_END__> -- store the output of calculate_key in __TMC_END__
  4007b4:	bf 9b 09 40 00       	mov    $0x40099b,%edi         # set edi to 0x40099b
  4007b9:	e8 72 fd ff ff       	callq  400530 <puts@plt>      # call puts()
  
  # Clean up and return
  4007be:	90                   	nop
  4007bf:	5d                   	pop    %rbp
  4007c0:	c3                   	retq   


00000000004007c1 <print_flag>:
  # Set up
  4007c1:	55                   	push   %rbp
  4007c2:	48 89 e5             	mov    %rsp,%rbp
  
  4007c5:	bf b0 09 40 00       	mov    $0x4009b0,%edi        # set edi to 0x4009b0
  4007ca:	e8 61 fd ff ff       	callq  400530 <puts@plt>     # call puts()
  4007cf:	8b 05 eb 08 20 00    	mov    0x2008eb(%rip),%eax   # 6010c0 <__TMC_END__>  -- copy __TMC_END__ into eax
  4007d5:	89 c7                	mov    %eax,%edi             # copy eax into edi
  4007d7:	e8 ba fe ff ff       	callq  400696 <decrypt_flag> # call decrypt_flag()
  4007dc:	bf 80 10 60 00       	mov    $0x601080,%edi        # set edi to 0x601080
  4007e1:	e8 4a fd ff ff       	callq  400530 <puts@plt>     # call puts()
  
  # Clean up and return
  4007e6:	90                   	nop
  4007e7:	5d                   	pop    %rbp
  4007e8:	c3                   	retq 
```

After looking at these, calculate_key() and decrypt_flag() both look important. I only looked at calculate_key() however since I realized this was enough to get the flag..

```Assembly
0000000000400706 <calculate_key>:
  #Set up
  400706:	55                   	push   %rbp
  400707:	48 89 e5             	mov    %rsp,%rbp
  
  40070a:	c7 45 fc 11 91 fe 72 	movl   $0x72fe9111,-0x4(%rbp)     # put 0x72fe9111 onto the stack 4 bytes above the base pointer
  400711:	83 45 fc 01          	addl   $0x1,-0x4(%rbp)            # add 1 to the value on the stack 4 bytes above rbp
  400715:	81 7d fc 22 22 fd e5 	cmpl   $0xe5fd2222,-0x4(%rbp)     # compare 0xe5fd2222 to the value on the stack 4 bytes above the base pointer
  40071c:	75 f3                	jne    400711 <calculate_key+0xb> # Loop (up 2 lines) until they are equal
  40071e:	8b 45 fc             	mov    -0x4(%rbp),%eax            # Store the result in eax
  
  # Clean up and return
  400721:	5d                   	pop    %rbp
  400722:	c3                   	retq 
  
```
So calculate key starts with the number 0x72fe9111 and repeatedly increments it by 1 until it is equal to 0xe5fd2222. There is absolutely no point to this except to make the program run slow.

I then opened the program in a hex editor and searched for the constant 0x72fe9111 (11 91 FE 72 since it is Little Endian) and changed it to 21 22 FD E5 so the loop only runs once.

I ran the [fixed program](be-quick-or-be-dead-1_fixed) and got the flag.

### Flag:

picoCTF{why_bother_doing_unnecessary_computation_d0c6aace}
