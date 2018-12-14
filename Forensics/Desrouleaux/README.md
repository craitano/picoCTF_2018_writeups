# Desrouleaux
__Category:__ Forensics  
__Points:__ 150

### Problem:

Our network administrator is having some trouble handling the tickets for all of of our incidents. Can you help him out by answering all the questions? Connect with `nc 2018shell2.picoctf.com 10493`. [incidents.json](incidents.json)

##### Hints:
> If you need to code, python has some good libraries for it.

### Solution:

I first opened the json file and established a connection to the given port. I then looked at the information in the json file to answer the questions:

__Q1:__ What is the most common source IP address? If there is more than one IP address that is the most common, you may give any of the most common ones.  
__A1:__ 53.196.3.10  
because this is the src_ip which appears in the most tickets

__Q2:__ How many unique destination IP addresses were targeted by the source IP address 205.210.212.253?  
_Note:_ Answers to this question may vary since it picks one of the ip addresses randomly.  
__A2:__ 2  
because there are 2 separate tickets with 205.219.212.253 as the src_ip and they both have different dst_ip's

__Q3:__ What is the average number of unique destination IP addresses that were sent a file with the same hash? Your answer needs to be correct to 2 decimal places.  
__A3:__ 1.8  
because eb492040be84f7f2 was sent to 1 unique dst ip, 77eb8b80e56a90a2 to 2, 38582789f5d7d7b5 to 3, 2f6cad54b82ad6bb to 1, and 6c559675243abef2 to 2 (9/5=1.8)

### Flag:

picoCTF{J4y_s0n_d3rUUUULo_a062e5f8}

