# grep 2
__Category:__ General Skills  
__Points:__ 125

### Problem:

This one is a little bit harder. Can you find the flag in /problems/grep-2_4_06c2058761f24267033e7ca6ff9d9144/files on the shell server? Remember, grep is your friend.

##### Hints:
> grep [tutorial](https://ryanstutorials.net/linuxtutorial/grep.php)

### Solution:

I navigated to the given dirctory and found 10 directories (files0, files1, ... files9). I then used the following command to find the flag

```bash
grep */*
```

### Flag:

picoCTF{grep_r_and_you_will_find_036bbb25}

