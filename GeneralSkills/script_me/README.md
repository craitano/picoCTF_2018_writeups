# script me
__Category:__ General Skills   
__Points:__ 500

### Problem:

Can you understand the language and answer the questions to retrieve the flag? Connect to the service with nc 2018shell3.picoctf.com 8672

##### Hints:
> Maybe try writing a python script?

### Solution:

I started by connecting to the server and got the rules for one of the worst languages ever written.

```
Rules:
() + () = ()()                                      => [combine]
((())) + () = ((())())                              => [absorb-right]
() + ((())) = (()(()))                              => [absorb-left]
(())(()) + () = (())(()())                          => [combined-absorb-right]
() + (())(()) = (()())(())                          => [combined-absorb-left]
(())(()) + ((())) = ((())(())(()))                  => [absorb-combined-right]
((())) + (())(()) = ((())(())(()))                  => [absorb-combined-left]
() + (()) + ((())) = (()()) + ((())) = ((()())(())) => [left-associative]

Example: 
(()) + () = () + (()) = (()())

```

It took a bit of testing for me to completely understand these rules. This is my explanation of the language:

> Each sentence includes pairs of parenthesis. E.g. ()

> Parenthesis can be nested. E.g. (()) or ((()()))

> The _depth_ of a sentence is the largest number of unpaired open parenthesis at any point in the sentence. E.g. () has depth 1, (()) and (())() have depth 2 ((())) and ((())()) have depth 3.

> Two sentences can be added as follows (left sentence is __bold__):
> * if both have the same depth: concatenate. E.g. __()__ + () = __()__() and __(())__ + (()()) = __(())__(()())  
> * if the left has a smaller depth it is placed inside the outermost pair of parenthesis at the start of the right sentence. E.g. __()__ + (()) = (__()__()) and __(())__ + (()(())()) = (__(())__()(())())  
> * if the right has a smaller depth it is placed inside the outermot pair of parenthesis at the end of the left sentence. E.g. __(())__ + () = __(()__()__)__ and __(()(())())__ + (()) = __(()(())()__(())__)__  
> * if there are multiple additions, they occur from left to right

I created the following python script to parse the input.

```Python
#!/usr/bin/env python3

import re

def depth(arg):
  depth = 0
  max = 0
  for c in arg:
    if(c == '('):
      depth += 1
    if(c == ')'):
      depth -= 1
    if(max < depth):
      max = depth
  return max

def process(a1, a2):
  d_a1 = depth(a1)
  d_a2 = depth(a2)
  if(d_a1 == d_a2):
    return a1 + a2
  elif(d_a1 < d_a2):
    return "(" + a1 + a2[1:]
  else:
    return a1[:-1] + a2 + ")"

eq = input("Enter input\n")
regex = re.compile("[()+ ]+")
while regex.match(eq):
  args = eq.split(" ")
  left_arg = args[0]
  right_arg = ""
  for i, arg in enumerate(args):
    if i > 0 and  arg != "+":
      right_arg = arg
      left_arg = process(left_arg, right_arg)
  print(left_arg)
  eq = input("Enter input\n")
print("Goodbye!")
```

The program will repeatedly prompt for inputs until an input with invalid chars is enterred (valid chars are parenthesis, space, and plus).

I used the python script to answer all of the questions and get the flag.

### Flag:

picoCTF{5cr1pt1nG_l1k3_4_pRo_0970eb2d}
