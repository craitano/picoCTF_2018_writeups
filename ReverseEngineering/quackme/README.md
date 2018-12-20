# quackme
__Category:__ Reversing   
__Points:__ 200

### Problem:

Can you deal with the Duck Web? Get us the flag from this [program](main). You can also find the program in /problems/quackme_3_9a15a74731538ce2076cd6590cf9e6ca

##### Hints:
> Objdump or something similar is probably a good place to start.

### Solution:

I began by running the program to see what it does. I then used an objdump to view the assembly code.

```bash
objdump -d main
```

I first looked at the main method an have commented the functionality here.

```Assembly
08048715 <main>:
 8048715:	8d 4c 24 04          	lea    0x4(%esp),%ecx        # add 4 to the stck pointer and store in ecx
 8048719:	83 e4 f0             	and    $0xfffffff0,%esp      # clear the last 4 bits of the stack pointer
 804871c:	ff 71 fc             	pushl  -0x4(%ecx)            # push the old stack pointer onto the stack
 804871f:	55                   	push   %ebp                  # store ebp on the stack
 8048720:	89 e5                	mov    %esp,%ebp             # store the stack pointer in ebp
 8048722:	51                   	push   %ecx                  # store ecx on the stack
 8048723:	83 ec 04             	sub    $0x4,%esp             # subtract 4 from the stack pointer
 8048726:	a1 44 a0 04 08       	mov    0x804a044,%eax        # store memory at 0x804a044 in eax
 804872b:	6a 00                	push   $0x0                  # store  0 on the stack
 804872d:	6a 02                	push   $0x2                  # store 2 on the stack
 804872f:	6a 00                	push   $0x0                  # store 0 on te stack
 8048731:	50                   	push   %eax                  # store eax on the stack
 8048732:	e8 79 fd ff ff       	call   80484b0 <setvbuf@plt> # call setvbuf()
 8048737:	83 c4 10             	add    $0x10,%esp            # move the stack pointer down 16
 804873a:	83 ec 0c             	sub    $0xc,%esp             # move the stack pointer up 12
 804873d:	68 f0 87 04 08       	push   $0x80487f0            # store 0x80487f0 on the stack
 8048742:	e8 29 fd ff ff       	call   8048470 <puts@plt>    # call puts()
 8048747:	83 c4 10             	add    $0x10,%esp            # move the stack down 16
 804874a:	e8 f3 fe ff ff       	call   8048642 <do_magic>    # call do_magic()
 804874f:	83 ec 0c             	sub    $0xc,%esp             # move the stack pointer up 12
 8048752:	68 bb 88 04 08       	push   $0x80488bb            # store 0x8048470 on the stack
 8048757:	e8 14 fd ff ff       	call   8048470 <puts@plt>    # call puts()
 804875c:	83 c4 10             	add    $0x10,%esp            # move the stack pointer down 16
 804875f:	b8 00 00 00 00       	mov    $0x0,%eax             # clear eax
 8048764:	8b 4d fc             	mov    -0x4(%ebp),%ecx       # store the address 4 below the base pointer in ecx
 # clean up and exit
 8048767:	c9                   	leave                        
 8048768:	8d 61 fc             	lea    -0x4(%ecx),%esp
 804876b:	c3                   	ret    
 804876c:	66 90                	xchg   %ax,%ax
 804876e:	66 90                	xchg   %ax,%ax
```

THe do_magic function looks important so I looked at it next

```Assembly
08048642 <do_magic>:
 # Set up
 8048642:	55                   	push   %ebp
 8048643:	89 e5                	mov    %esp,%ebp

 8048645:	83 ec 28             	sub    $0x28,%esp              # Move the stack pointer up 28
 8048648:	e8 8e ff ff ff       	call   80485db <read_input>    # Call read_input()
 804864d:	89 45 ec             	mov    %eax,-0x14(%ebp)        # put eax on the stack 20 above the base pointer 
 8048650:	83 ec 0c             	sub    $0xc,%esp               # move the stack pointer down 12
 8048653:	ff 75 ec             	pushl  -0x14(%ebp)             # store the address 20 above the base pointer on the stack
 8048656:	e8 35 fe ff ff       	call   8048490 <strlen@plt>    # call strlen()
 804865b:	83 c4 10             	add    $0x10,%esp              # move the stack pointer down 16
 804865e:	89 45 f0             	mov    %eax,-0x10(%ebp)        # put eax on the stack 16 above the base pointer
 8048661:	8b 45 f0             	mov    -0x10(%ebp),%eax        # store the address 16 above the base pointer ineax
 8048664:	83 c0 01             	add    $0x1,%eax               # add 1 to eax
 8048667:	83 ec 0c             	sub    $0xc,%esp               # move the stack pointer up 12 
 804866a:	50                   	push   %eax                    # store eax on the stack
 804866b:	e8 f0 fd ff ff       	call   8048460 <malloc@plt>    # call malloc()
 8048670:	83 c4 10             	add    $0x10,%esp              # move the stack pointer down 16
 8048673:	89 45 f4             	mov    %eax,-0xc(%ebp)         # put eax on the stack 12 above the base pointer
 8048676:	83 7d f4 00          	cmpl   $0x0,-0xc(%ebp)         # compare this value to 0
 804867a:	75 1a                	jne    8048696 <do_magic+0x54> # if not 0 skip the next 8 lines
 804867c:	83 ec 0c             	sub    $0xc,%esp               # move the stack pointer up 12
 804867f:	68 84 88 04 08       	push   $0x8048884              # store 0x8048884 on the stack
 8048684:	e8 e7 fd ff ff       	call   8048470 <puts@plt>      # call puts()
 8048689:	83 c4 10             	add    $0x10,%esp              # move the stack pointer down 16
 804868c:	83 ec 0c             	sub    $0xc,%esp               # move the stack pointer up 12
 804868f:	6a ff                	push   $0xffffffff             # store 0xffffffff on the stack
 8048691:	e8 ea fd ff ff       	call   8048480 <exit@plt>      # call exit()
 8048696:	8b 45 f0             	mov    -0x10(%ebp),%eax        # store the value on the stack 10 above the base pointer in eax
 8048699:	83 c0 01             	add    $0x1,%eax               # increment eax
 804869c:	83 ec 04             	sub    $0x4,%esp               # move the stack pointer down 4
 804869f:	50                   	push   %eax                    # store eac on the stack
 80486a0:	6a 00                	push   $0x0                    # store 0 on the stack
 80486a2:	ff 75 f4             	pushl  -0xc(%ebp)              # store the value 12 above the base pointer on teh stack
 80486a5:	e8 16 fe ff ff       	call   80484c0 <memset@plt>    # call memset()
 80486aa:	83 c4 10             	add    $0x10,%esp              # move the stack pointer down 16
 80486ad:	c7 45 e4 00 00 00 00 	movl   $0x0,-0x1c(%ebp)        # store 0 on the stack 28 above the base pointer 
 80486b4:	c7 45 e8 00 00 00 00 	movl   $0x0,-0x18(%ebp)        # store 0 on the stack 24 above the base pointer
 80486bb:	eb 4e                	jmp    804870b <do_magic+0xc9> # skip over the next 24 lines
 80486bd:	8b 45 e8             	mov    -0x18(%ebp),%eax        # store the value 24 above the base pointer in eax
 80486c0:	05 58 88 04 08       	add    $0x8048858,%eax         # add 0x8048858 to eax
 80486c5:	0f b6 08             	movzbl (%eax),%ecx             #  
 80486c8:	8b 55 e8             	mov    -0x18(%ebp),%edx        # 
 80486cb:	8b 45 ec             	mov    -0x14(%ebp),%eax        # 
 80486ce:	01 d0                	add    %edx,%eax               # 
 80486d0:	0f b6 00             	movzbl (%eax),%eax             # 
 80486d3:	31 c8                	xor    %ecx,%eax               # 
 80486d5:	88 45 e3             	mov    %al,-0x1d(%ebp)         # 
 80486d8:	8b 15 38 a0 04 08    	mov    0x804a038,%edx          # 
 80486de:	8b 45 e8             	mov    -0x18(%ebp),%eax        # 
 80486e1:	01 d0                	add    %edx,%eax               # 
 80486e3:	0f b6 00             	movzbl (%eax),%eax             # 
 80486e6:	3a 45 e3             	cmp    -0x1d(%ebp),%al         # 
 80486e9:	75 04                	jne    80486ef <do_magic+0xad> # 
 80486eb:	83 45 e4 01          	addl   $0x1,-0x1c(%ebp)        # 
 80486ef:	83 7d e4 19          	cmpl   $0x19,-0x1c(%ebp)       # 
 80486f3:	75 12                	jne    8048707 <do_magic+0xc5> # 
 80486f5:	83 ec 0c             	sub    $0xc,%esp               # 
 80486f8:	68 ab 88 04 08       	push   $0x80488ab              # 
 80486fd:	e8 6e fd ff ff       	call   8048470 <puts@plt>      # 
 8048702:	83 c4 10             	add    $0x10,%esp              # 
 8048705:	eb 0c                	jmp    8048713 <do_magic+0xd1> # 
 8048707:	83 45 e8 01          	addl   $0x1,-0x18(%ebp)        # 
 804870b:	8b 45 e8             	mov    -0x18(%ebp),%eax        # store the value 24 above the base pointer in eax
 804870e:	3b 45 f0             	cmp    -0x10(%ebp),%eax        # compare the value 16 above the base pointer to eax 
 8048711:	7c aa                	jl     80486bd <do_magic+0x7b> # if it is less go up 26 lines
 
 # Clean up and exit
 8048713:	c9                   	leave
 8048714:	c3                   	ret  
```

### Flag:

picoCTF{}
