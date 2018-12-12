# ssh-keyz
__Category:__ General Skills  
__Points:__ 150

### Problem:

As nice as it is to use our webshell, sometimes its helpful to connect directly to our machine. To do so, please add your own public key to ~/.ssh/authorized_keys, using the webshell. The flag is in the ssh banner which will be displayed when you login remotely with ssh to with your username.

###Solution:

I first created a ~/.shh directory in the picoctf shell using the following command:

```Bash
mkdir ~/.ssh
```

I then created a key on my own computer using the ssh-keygen command in a terminal. The steps are pretty straightforward. I then opened the file containing my key and used the echo command on the picoctf shell to copy it to the a new file:

```Bash
echo <key> ~/.ssh/authorized_keys
```

From my own computer I was then able to ssh to the picoctf shell and get the flag:

```Bash
ssh <username>@<shell>@picoctf.com
```

For me the shell was 2018shell3. Look at the top of the picoctf shell webpage to determine your shell.

###Flag:

picoCTF{who_n33ds_p4ssw0rds_38dj21}

