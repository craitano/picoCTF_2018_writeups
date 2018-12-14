# Reversing Warmup 1
__Category:__ Reverse Engineering  
__Points:__ 50

### Problem:

Throughout your journey you will have to run many programs. Can you navigate to /problems/reversing-warmup-1_3_7c0eade7faf60ffe3485e12098e2a6c2 on the shell server and run this [program](run) to retreive the flag?

##### Hints:
> If you are searching online, it might be worth finding how to exeucte a program in command line.

### Solution:

Login to the picoCTF shell and enter the following command to navigate to the given directory:

```bash
cd /problems/reversing-warmup-1_3_7c0eade7faf60ffe3485e12098e2a6c2
```

Use the ls command to list files in the directory:

```bash
ls
```

You should see a program called "run". Use the following command to run this program:

```bash
./run
```

This prints out the flag

### Flag:

picoCTF{welc0m3_t0_r3VeRs1nG}

