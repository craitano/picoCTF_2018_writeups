# you can't see me
__Category:__ General Skills   
__Points:__ 200

### Problem:

'...reading transmission... Y.O.U. .C.A.N.'.T. .S.E.E. .M.E. ...transmission ended...' Maybe something lies in /problems/you-can-t-see-me_2_cfb71908d8368e3062423b45959784aa.

##### Hints:
> What command can see/read files?

> What's in the manual page of ls?

### Solution:

I started by navigating to the directory and using ls but found nothing. I then used the -a option to show hidden directories.

```Bash
$ ls -a
.  .    ..
```

This seemed weird since there should only be 1 '.' directory (indicating the current directory).

I figured there was probably some extra whitespace in the name of the second one. I used -Qa to get the full names and cat to get the flag.

```Bash
$ ls -Qa                                        
"."  ".  "  ".."
$ cat ".  "
```

### Flag:

picoCTF{j0hn_c3na_paparapaaaaaaa_paparapaaaaaa_093d6aff}
