#!/usr/bin/env python
# -*- coding:utf-8 -*-

from PIL import Image


def plus(strr):

    return strr.zfill(8)


def get_key(strr):
     
    tmp = strr
     
    f = file(tmp, "rb")
     
    strr = ""
     
    s = f.read()

    for i in range(len(s)):

        strr = strr + plus(bin(ord(s[i])).replace('0b', ''))

    f.close()


    return strr

def mod(x, y):
     
    return x%y
     
def func(str1,str2,str3):
     
        im = Image.open(str1)
     
        width = im.size[0]
     
        print "width:"+str(width)+"\n"
     
        height = im.size[1]
     
        print "height:"+str(height)+"\n"
     
        count = 0
     
        key = get_key(str2)
     
        keylen = len(key)
     
        for h in range(0,height):
     
            for w in range(0,width):
     
                pixel = im.getpixel((w,h))
     
                a=pixel[0]
     
                b=pixel[1]
     
                c=pixel[2]
     
                if count == keylen:
     
                    break

                a= a-mod(a,2)+int(key[count])
     
                count+=1
     
                if count == keylen:
     
                    im.putpixel((w,h),(a,b,c))
     
                    break
     
                b =b-mod(b,2)+int(key[count])
     
                count+=1
     
                if count == keylen:
     
                    im.putpixel((w,h),(a,b,c))
     
                    break
     
                c= c-mod(c,2)+int(key[count])
     
                count+=1
     
                if count == keylen:
     
                    im.putpixel((w, h), (a, b, c))
     
                    break
     
                if count % 3 == 0:
     
                    im.putpixel((w, h), (a, b, c))
     
        im.save(str3)

     
old = "C:/Users/94019/Desktop/Darius2.png"
     
new = "C:/Users/94019/Desktop/Darius.png"
     
enc = "C:/Users/94019/Desktop/flag.txt"
     
func(old,enc,new)