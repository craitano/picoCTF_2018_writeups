# Recovering From the Snap
__Category:__ Forensics  
__Points:__ 150

### Problem:

There used to be a bunch of [animals](https://2018shell3.picoctf.com/static/040c56434beb57348cc5032272c04350/animals.dd) here, what did Dr. Xernon do to them?

### Solution:

After downloading the given disk image I opened it using test disk:

```bash
testdisk animals.dd
```

I then selected the disk and selected `[None]` as the partition table type.
I then picked `[Analyze]` from the options menu, did a quick search then pressed `<p>` to show files on the listed partitionHere it lists all files on the partition including deleted files.
I navigated to the file 'theflag.jpg' and pressed `<c>` to copy the file. I then pressed `<c>` again to choose the current directory.
Now the image shows up in the filesystem and can be opened to get the flag.

### Flag:

picoCTF{th3_5n4p_happ3n3d}

