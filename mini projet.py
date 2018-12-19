# Mini Projet 2 - Paulien C. - Aida C. - Eliot T.
#version 0.1
from tkinter import *
from PIL import Image, ImageTk

images = []
width = 2000
height = 3000

pathImg="deadpool.jpg"
im=Image.open(pathImg).load()

imFlou=Image.new("RGB", (width, height))


rouge=int(0)
vert=int(0)
bleu=int(0)


couleur=(rouge,vert,bleu)


for x in range(width):
    for y in range(height):

        if x-2>=0 and y-2>=0 and x+2<=width and y+2<=height:

            for x2 in range(x-2,x+2):

                for y2 in range(y-2,y+2):

                    im.getpixel((x2,y2))=couleur


                    rouge=rouge+pix[0]

                    vert=vert+pix[1]

                    bleu=bleu+pix[2]



            rouge=rouge//25

            vert=vert//25

            bleu=bleu//25

            imflou.putpixel((x,y),(rouge,vert,bleu))

            rouge=0

            vert=0

            bleu=0



imFlou.show()

