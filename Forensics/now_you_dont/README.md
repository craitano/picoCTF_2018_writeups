# now you don't
__Category:__ Forensics   
__Points:__ 200

### Problem:

We heard that there is something hidden in this [picture](nowYouDont.png). Can you find it?

##### Hints:
> There is an old saying: if you want to hide the treasure, put it in plain sight. Then no one will see it.

> Is it really all one shade of red?

### Solution:

I initially tried to find hidden messages in this image using several different steganography tools and was unsuccessful.

I then opened the image in a photo editor (I used [GIMP](https://www.gimp.org/)) and began messing with the hsv values. 
I noticed when the hue and saturation were turned all the way down I could see the flag faintly in the [image](modified_hsv.png). 
I couldn't quite read it here so I messed with the exposure settings until I got [this](flag.png) image with the flag clearly visible.

### Flag:

picoCTF{n0w_y0u_533_m3}
