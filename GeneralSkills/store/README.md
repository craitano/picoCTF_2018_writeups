# store
__Category:__ General Skills   
__Points:__ 400

### Problem:

We started a little [store](store), can you buy the flag? [Source](source.c). Connect with 2018shell3.picoctf.com 53220.

##### Hints:
> Two's compliment can do some weird things when numbers get really big!

### Solution:

I started out by connecting to the shell to run the program and see what it does. I checked my account balnce and tried to buy a fag.

```Bash
$nc 2018shell3.picoctf.com 53220
Welcome to the Store App V1.0
World's Most Secure Purchasing App

[1] Check Account Balance

[2] Buy Stuff

[3] Exit

 Enter a menu selection
1



 Balance: 1100 


Welcome to the Store App V1.0
World's Most Secure Purchasing App

[1] Check Account Balance

[2] Buy Stuff

[3] Exit

 Enter a menu selection
2
Current Auctions
[1] I Can't Believe its not a Flag!
[2] Real Flag
2
A genuine Flag costs 100000 dollars, and we only have 1 in stock
Enter 1 to purchase1

Not enough funds for transaction
```

I then looked at th imitation flag and hoped I could overflow the cost by buying a bunch to spend a negative value.
I assumed it is using 32 bit integers (which can store about -2 billion to 2 billion).
I bought 3 million fake flags for a total cost of 3 billion, which should overflow to around -1 billion. 

```Bash
Welcome to the Store App V1.0
World's Most Secure Purchasing App

[1] Check Account Balance

[2] Buy Stuff

[3] Exit

 Enter a menu selection
2
Current Auctions
[1] I Can't Believe its not a Flag!
[2] Real Flag
1
Imitation Flags cost 1000 each, how many would you like?
3000000

Your total cost is: -1294967296

Your new balance: 1294968396
```

I then bought the flag.

### Flag:

picoCTF{numb3r3_4r3nt_s4f3_cbb7151f}
