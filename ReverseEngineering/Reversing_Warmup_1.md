# Reversing Warmup 1
__Category:__ Reverse Engineering
__Points:__ 50

### Problem:

Throughout your journey you will have to run many programs. Can you navigate to /problems/reversing-warmup-1_3_7c0eade7faf60ffe3485e12098e2a6c2 on the shell server and run this [program](https://2018shell3.picoctf.com/static/ed5cc27f269a3a4653f0a65b2e8a2d46/run) to retreive the flag?

### Solution:

Login to the picoCTF shell and enter the following command to navigate to the given directory:

```bash
cd /problems/reversing-warmup-1_3_7c0eade7faf60ffe3485e12098e2a6c2
```

Enter the command to list files in the directory:

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

