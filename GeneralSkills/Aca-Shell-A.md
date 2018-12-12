# Aca-Shell-A
__Category:__ General Skills  
__Points:__ 150

### Problem:

It's never a bad idea to brush up on those linux skills or even learn some new ones before you set off on this adventure! Connect with `nc 2018shell2.picoctf.com 33158`.

### Solution:

I used the given command to connect to the server. I then used ls to see what files were available in the shell. After using cd to look through all of the folders it seemed secret was the only one with anything in it. I then ran the following commands to delete the intel files as described by the program:

```bash
rm intel_1
rm intel_2
rm intel_3
rm intel_4
rm intel_5
```

I then input the given command:

```bash
echo 'Drop it in!'
```

I then navigated to the executables folder and executed the program:

```bash
./dontLookHere
```

I then used the following command to show the username:

```bash
whoami
```

I had a difficult time after this. I used cd to go back to the home directory and attempted to copy the TopSecret file from /tmp, /var/tmp, $TMPDIR, and $TMP to no avail. It turns out you have to be in the executables directory, despite the hint you get when you type "echo 'Help Me!'" which states that you must be in the home directory.

From the executables directory enter the following command:

```bash
cp /tmp/TopSecret ../passwords
```

Then navigate to the passwords directory and enter the followin command:

```bash
cat TopSecret
```

At the bottom of the output it lists the flag.

### Flag:

picoCTF{CrUsHeD_It_9edaa84a}

