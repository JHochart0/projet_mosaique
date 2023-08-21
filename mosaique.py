from PIL import Image
import os
from random import randint
im = Image.open("imageBase/image_a_transformer.PNG")

im_resized=im.resize((int(im.width/4), int(im.height/4)))
im_resized.save("imageBase/image_a_transformer2.png")

im_mosaique=im_resized.resize((int(im_resized.size[0]*20),int(im_resized.size[1]*20)))
im_mosaique.save("imageBase/image_a_transformer3.png")

taille=20, 20


global tabPetitesImages
tabPetitesImages=[]

def moyenneCouleur(image):
    rougetotal=0
    verttotal=0
    bleutotal=0
    for i in range(0,20):
        for j in range(0,20):
            rouge=image.getpixel((i,j))[0]
            rougetotal=rougetotal+rouge

            vert=image.getpixel((i,j))[1]
            verttotal=verttotal+vert

            bleu=image.getpixel((i,j))[2]
            bleutotal=bleutotal+bleu



    rougemoyenne=rougetotal/(20*20)
    vertmoyenne=verttotal/(20*20)
    bleumoyenne=bleutotal/(20*20)
    rgb=[]
    rgb.append(int(rougemoyenne))
    rgb.append(int(vertmoyenne))
    rgb.append(int(bleumoyenne))
    return(rgb)




def redimImage(taille):

    for element in os.listdir('.'):
        if element.endswith('.jpg') or element.endswith('.png') or element.endswith('.PNG') or element.endswith('.jpeg'):
            im = Image.open(element)
            im_resized=im.resize((taille))
            im_resized.save(element)
            print(element)
            moyenneRGB=moyenneCouleur(im_resized)
            tabPetitesImages.append(element)
            tabPetitesImages.append(moyenneRGB)



def mosaique():
    alea=int()
    choixImage=''
    longueur=int()
    image = Image.open("imageBase/image_a_transformer2.png")
    imageMosai = Image.open("imageBase/image_a_transformer3.png")
    for i in range(0, image.width):
        for j in range(0, image.height):
            tabChoix=[]
            rouge=image.getpixel((i,j))[0]
            vert=image.getpixel((i,j))[1]
            bleu=image.getpixel((i,j))[2]
            rgbPixel=[]
            rgbPixel.append(rouge)
            rgbPixel.append(vert)
            rgbPixel.append(bleu)
            for u in range(1, len(tabPetitesImages)+1, 2):
                couleur=tabPetitesImages[u]
                if couleur[0]>rgbPixel[0]-65 and couleur[0]<rgbPixel[0]+65 and couleur[1]>rgbPixel[1]-65 and couleur[1]<rgbPixel[1]+65 and couleur[2]>rgbPixel[2]-65 and couleur[2]<rgbPixel[2]+65:
                    tabChoix.append(tabPetitesImages[u-1])
                    longueur=int((len(tabChoix)-1))

            alea=randint(0,longueur)
            choixImage=tabChoix[alea]
            imagePixel=Image.open(choixImage)

            for m in range(0,20):
                for n in range(0,20):
                    rouge=imagePixel.getpixel((m,n))[0]
                    vert=imagePixel.getpixel((m,n))[1]
                    bleu=imagePixel.getpixel((m,n))[2]

                    r,v,b=(int(rouge),int(vert),int(bleu))
                    imageMosai.putpixel((i*20+m,j*20+n),(r,v,b))

    return(imageMosai)






redimImage(taille)

mosaique=mosaique()

mosaique.show()