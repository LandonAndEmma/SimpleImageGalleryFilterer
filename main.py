import os
import random
import webbrowser
from tkinter import *
from tkinter import filedialog
import pygame
import winsound
from PIL import Image, ImageFilter

clicksound = 'sounds/click.wav'
editsound = 'sounds/edit.wav'
savesound = 'sounds/success.wav'
newsize = (512, 512)
root = Tk()
root.title('Image Slideshow Program')
root.geometry('512x707')
icon = PhotoImage(file='images/icon.png')
root.iconphoto(True, icon)
root.minsize(512, 707)
root.maxsize(512, 707)
root.resizable(False, False)


def defineimages():
    global im1pil
    global im2pil
    global im3pil
    global im4pil
    global im5pil
    global im1tk
    global im2tk
    global im3tk
    global im4tk
    global im5tk
    global image_list
    global image_names
    global counter
    im1pil = Image.open("images/aliendude.png")
    im2pil = Image.open("images/bluesmurfcat.png")
    im3pil = Image.open("images/imspongebob.png")
    im4pil = Image.open("images/jonesy.png")
    im5pil = Image.open("images/pythonlogo.png")
    im1tk = PhotoImage(file='images/aliendude.png')
    im2tk = PhotoImage(file='images/bluesmurfcat.png')
    im3tk = PhotoImage(file='images/imspongebob.png')
    im4tk = PhotoImage(file='images/jonesy.png')
    im5tk = PhotoImage(file='images/pythonlogo.png')
    image_list = [im1tk, im2tk, im3tk, im4tk, im5tk]
    counter = 0


def nextimage():
    global counter
    winsound.PlaySound(clicksound, winsound.SND_FILENAME)
    if counter < len(image_list) - 1:
        counter += 1
    else:
        counter = 0
    imageLabel.configure(image=image_list[counter])
    if counter == 0:
        global im1tk
        imageLabel.config(image=im1tk)
    if counter == 1:
        global im2tk
        imageLabel.config(image=im2tk)
    if counter == 2:
        global im3tk
        imageLabel.config(image=im3tk)
    if counter == 3:
        global im4tk
        imageLabel.config(image=im4tk)
    if counter == 4:
        global im5tk
        imageLabel.config(image=im5tk)
    infoLabel.config(text='Image ' + str(counter + 1) + ' of ' + str(len(image_list)))


def lastimage():
    global counter
    winsound.PlaySound(clicksound, winsound.SND_FILENAME)
    if counter > 0:
        counter -= 1
    else:
        counter = 4
    imageLabel.configure(image=image_list[counter])
    if counter == 0:
        global im1tk
        imageLabel.config(image=im1tk)
    if counter == 1:
        global im2tk
        imageLabel.config(image=im2tk)
    if counter == 2:
        global im3tk
        imageLabel.config(image=im3tk)
    if counter == 3:
        global im4tk
        imageLabel.config(image=im4tk)
    if counter == 4:
        global im5tk
        imageLabel.config(image=im5tk)
    infoLabel.config(text='Image ' + str(counter + 1) + ' of ' + str(len(image_list)))


def savefile():
    randomname1 = random.randint(1, 10000)
    randomname2 = random.randint(1, 10000)
    randomname3 = randomname1 + randomname2
    filename = filedialog.asksaveasfilename(initialdir="/", title="Save As", filetypes=(("Image files",
                                                                                         "*.png;*.jpeg;*.jpg;*.bmp;*.dds;*.webp;*.tga;*.dds"),
                                                                                        ("All files", "*.*")))
    if counter == 0:
        global im1pil
        im1pil.save(str(randomname3) + ".png")
        im1pil = Image.open(str(randomname3) + ".png")
        im1pil = im1pil.convert('RGB')
        os.remove(str(randomname3) + ".png")
        im1pil.save(filename)
        winsound.PlaySound(savesound, winsound.SND_FILENAME)
    if counter == 1:
        global im2pil
        im2pil.save(str(randomname3) + ".png")
        im2pil = Image.open(str(randomname3) + ".png")
        im2pil = im1pil.convert('RGB')
        os.remove(str(randomname3) + ".png")
        im2pil.save(filename)
        winsound.PlaySound(savesound, winsound.SND_FILENAME)
    if counter == 2:
        global im3pil
        im3pil.save(str(randomname3) + ".png")
        im3pil = Image.open(str(randomname3) + ".png")
        im3pil = im1pil.convert('RGB')
        os.remove(str(randomname3) + ".png")
        im3pil.save(filename)
        winsound.PlaySound(savesound, winsound.SND_FILENAME)
    if counter == 3:
        global im4pil
        im4pil.save(str(randomname3) + ".png")
        im4pil = Image.open(str(randomname3) + ".png")
        im4pil = im1pil.convert('RGB')
        os.remove(str(randomname3) + ".png")
        im4pil.save(filename)
        winsound.PlaySound(savesound, winsound.SND_FILENAME)
    if counter == 4:
        global im5pil
        im5pil.save(str(randomname3) + ".png")
        im5pil = Image.open(str(randomname3) + ".png")
        im5pil = im1pil.convert('RGB')
        os.remove(str(randomname3) + ".png")
        im5pil.save(filename)
        winsound.PlaySound(savesound, winsound.SND_FILENAME)


def openfile():
    global newsize
    randomname1 = random.randint(1, 10000)
    randomname2 = random.randint(1, 10000)
    randomname3 = randomname1 + randomname2
    filename = filedialog.askopenfilename(initialdir="/", title="Open", filetypes=(("Image files",
                                                                                    "*.png;*.jpeg;*.jpg;*.bmp;*.xpm;*.dds;*.psd;*.webp;*.tiff;*.tga;*.dds;*.dib;*.icns;*.ico;*.im;*.msp;*.wmf;*.emf;*.pcx;*.pbm;*.ppm;*.pgm;*.pnm;*.sgi;*.blp;*.eps;*.sun;*.wal"),
                                                                                   ("All files", "*.*")))
    if counter == 0:
        global im1pil
        global im1tk
        im1pil = Image.open(str(filename))
        im1pil = im1pil.resize(newsize, 0)
        im1pil = im1pil.convert('RGB')
        im1pil.save(str(randomname3) + ".png")
        im1tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im1tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 1:
        global im2pil
        global im2tk
        im2pil = Image.open(str(filename))
        im2pil = im2pil.resize(newsize, 0)
        im2pil = im2pil.convert('RGB')
        im2pil.save(str(randomname3) + ".png")
        im2tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im2tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 2:
        global im3pil
        global im3tk
        im3pil = Image.open(str(filename))
        im3pil = im3pil.resize(newsize, 0)
        im3pil = im3pil.convert('RGB')
        im3pil.save(str(randomname3) + ".png")
        im3tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im3tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 3:
        global im4pil
        global im4tk
        im4pil = Image.open(str(filename))
        im4pil = im4pil.resize(newsize, 0)
        im4pil = im4pil.convert('RGB')
        im4pil.save(str(randomname3) + ".png")
        im4tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im4tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 4:
        global im5pil
        global im5tk
        im5pil = Image.open(str(filename))
        im5pil = im5pil.resize(newsize, 0)
        im5pil = im5pil.convert('RGB')
        im5pil.save(str(randomname3) + ".png")
        im5tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im5tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)


def resetimages():
    if counter == 0:
        global im1pil
        global im1tk
        im1pil = Image.open("images/aliendude.png")
        im1tk = PhotoImage(file='images/aliendude.png')
        imageLabel.config(image=im1tk)
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 1:
        global im2pil
        global im2tk
        im2pil = Image.open("images/bluesmurfcat.png")
        im2tk = PhotoImage(file='images/bluesmurfcat.png')
        imageLabel.config(image=im2tk)
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 2:
        global im3pil
        global im3tk
        im3pil = Image.open("images/imspongebob.png")
        im3tk = PhotoImage(file='images/imspongebob.png')
        imageLabel.config(image=im3tk)
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 3:
        global im4pil
        global im4tk
        im4pil = Image.open("images/jonesy.png")
        im4tk = PhotoImage(file='images/jonesy.png')
        imageLabel.config(image=im4tk)
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 4:
        global im5pil
        global im5tk
        im5pil = Image.open("images/pythonlogo.png")
        im5tk = PhotoImage(file='images/pythonlogo.png')
        imageLabel.config(image=im5tk)
        winsound.PlaySound(editsound, winsound.SND_FILENAME)


def blur():
    randomname1 = random.randint(1, 10000)
    randomname2 = random.randint(1, 10000)
    randomname3 = randomname1 + randomname2
    if counter == 0:
        global im1pil
        global im1tk
        im1pil.save(str(randomname3) + ".png")
        im1pil = Image.open(str(randomname3) + ".png")
        im1pil = im1pil.convert('RGB')
        im1pil = im1pil.filter(ImageFilter.BLUR)
        im1pil.save(str(randomname3) + ".png")
        im1tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im1tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 1:
        global im2pil
        global im2tk
        im2pil.save(str(randomname3) + ".png")
        im2pil = Image.open(str(randomname3) + ".png")
        im2pil = im2pil.convert('RGB')
        im2pil = im2pil.filter(ImageFilter.BLUR)
        im2pil.save(str(randomname3) + ".png")
        im2tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im2tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 2:
        global im3pil
        global im3tk
        im3pil.save(str(randomname3) + ".png")
        im3pil = Image.open(str(randomname3) + ".png")
        im3pil = im3pil.convert('RGB')
        im3pil = im3pil.filter(ImageFilter.BLUR)
        im3pil.save(str(randomname3) + ".png")
        im3tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im3tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 3:
        global im4pil
        global im4tk
        im4pil.save(str(randomname3) + ".png")
        im4pil = Image.open(str(randomname3) + ".png")
        im4pil = im4pil.convert('RGB')
        im4pil = im4pil.filter(ImageFilter.BLUR)
        im4pil.save(str(randomname3) + ".png")
        im4tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im4tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 4:
        global im5pil
        global im5tk
        im5pil.save(str(randomname3) + ".png")
        im5pil = Image.open(str(randomname3) + ".png")
        im5pil = im5pil.convert('RGB')
        im5pil = im5pil.filter(ImageFilter.BLUR)
        im5pil.save(str(randomname3) + ".png")
        im5tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im5tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)


def sharpen():
    randomname1 = random.randint(1, 10000)
    randomname2 = random.randint(1, 10000)
    randomname3 = randomname1 + randomname2
    if counter == 0:
        global im1pil
        global im1tk
        im1pil.save(str(randomname3) + ".png")
        im1pil = Image.open(str(randomname3) + ".png")
        im1pil = im1pil.convert('RGB')
        im1pil = im1pil.filter(ImageFilter.SHARPEN)
        im1pil.save(str(randomname3) + ".png")
        im1tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im1tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 1:
        global im2pil
        global im2tk
        im2pil.save(str(randomname3) + ".png")
        im2pil = Image.open(str(randomname3) + ".png")
        im2pil = im2pil.convert('RGB')
        im2pil = im2pil.filter(ImageFilter.SHARPEN)
        im2pil.save(str(randomname3) + ".png")
        im2tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im2tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 2:
        global im3pil
        global im3tk
        im3pil.save(str(randomname3) + ".png")
        im3pil = Image.open(str(randomname3) + ".png")
        im3pil = im3pil.convert('RGB')
        im3pil = im3pil.filter(ImageFilter.SHARPEN)
        im3pil.save(str(randomname3) + ".png")
        im3tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im3tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 3:
        global im4pil
        global im4tk
        im4pil.save(str(randomname3) + ".png")
        im4pil = Image.open(str(randomname3) + ".png")
        im4pil = im4pil.convert('RGB')
        im4pil = im4pil.filter(ImageFilter.SHARPEN)
        im4pil.save(str(randomname3) + ".png")
        im4tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im4tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 4:
        global im5pil
        global im5tk
        im5pil.save(str(randomname3) + ".png")
        im5pil = Image.open(str(randomname3) + ".png")
        im5pil = im5pil.convert('RGB')
        im5pil = im5pil.filter(ImageFilter.SHARPEN)
        im5pil.save(str(randomname3) + ".png")
        im5tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im5tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)


def smoothen():
    randomname1 = random.randint(1, 10000)
    randomname2 = random.randint(1, 10000)
    randomname3 = randomname1 + randomname2
    if counter == 0:
        global im1pil
        global im1tk
        im1pil.save(str(randomname3) + ".png")
        im1pil = Image.open(str(randomname3) + ".png")
        im1pil = im1pil.convert('RGB')
        im1pil = im1pil.filter(ImageFilter.SMOOTH)
        im1pil.save(str(randomname3) + ".png")
        im1tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im1tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 1:
        global im2pil
        global im2tk
        im2pil.save(str(randomname3) + ".png")
        im2pil = Image.open(str(randomname3) + ".png")
        im2pil = im2pil.convert('RGB')
        im2pil = im2pil.filter(ImageFilter.SMOOTH)
        im2pil.save(str(randomname3) + ".png")
        im2tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im2tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 2:
        global im3pil
        global im3tk
        im3pil.save(str(randomname3) + ".png")
        im3pil = Image.open(str(randomname3) + ".png")
        im3pil = im3pil.convert('RGB')
        im3pil = im3pil.filter(ImageFilter.SMOOTH)
        im3pil.save(str(randomname3) + ".png")
        im3tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im3tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 3:
        global im4pil
        global im4tk
        im4pil.save(str(randomname3) + ".png")
        im4pil = Image.open(str(randomname3) + ".png")
        im4pil = im4pil.convert('RGB')
        im4pil = im4pil.filter(ImageFilter.SMOOTH)
        im4pil.save(str(randomname3) + ".png")
        im4tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im4tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 4:
        global im5pil
        global im5tk
        im5pil.save(str(randomname3) + ".png")
        im5pil = Image.open(str(randomname3) + ".png")
        im5pil = im5pil.convert('RGB')
        im5pil = im5pil.filter(ImageFilter.SMOOTH)
        im5pil.save(str(randomname3) + ".png")
        im5tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im5tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)


def detail():
    randomname1 = random.randint(1, 10000)
    randomname2 = random.randint(1, 10000)
    randomname3 = randomname1 + randomname2
    if counter == 0:
        global im1pil
        global im1tk
        im1pil.save(str(randomname3) + ".png")
        im1pil = Image.open(str(randomname3) + ".png")
        im1pil = im1pil.convert('RGB')
        im1pil = im1pil.filter(ImageFilter.DETAIL)
        im1pil.save(str(randomname3) + ".png")
        im1tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im1tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 1:
        global im2pil
        global im2tk
        im2pil.save(str(randomname3) + ".png")
        im2pil = Image.open(str(randomname3) + ".png")
        im2pil = im2pil.convert('RGB')
        im2pil = im2pil.filter(ImageFilter.DETAIL)
        im2pil.save(str(randomname3) + ".png")
        im2tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im2tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 2:
        global im3pil
        global im3tk
        im3pil.save(str(randomname3) + ".png")
        im3pil = Image.open(str(randomname3) + ".png")
        im3pil = im3pil.convert('RGB')
        im3pil = im3pil.filter(ImageFilter.DETAIL)
        im3pil.save(str(randomname3) + ".png")
        im3tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im3tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 3:
        global im4pil
        global im4tk
        im4pil.save(str(randomname3) + ".png")
        im4pil = Image.open(str(randomname3) + ".png")
        im4pil = im4pil.convert('RGB')
        im4pil = im4pil.filter(ImageFilter.DETAIL)
        im4pil.save(str(randomname3) + ".png")
        im4tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im4tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 4:
        global im5pil
        global im5tk
        im5pil.save(str(randomname3) + ".png")
        im5pil = Image.open(str(randomname3) + ".png")
        im5pil = im5pil.convert('RGB')
        im5pil = im5pil.filter(ImageFilter.DETAIL)
        im5pil.save(str(randomname3) + ".png")
        im5tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im5tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)


def contour():
    randomname1 = random.randint(1, 10000)
    randomname2 = random.randint(1, 10000)
    randomname3 = randomname1 + randomname2
    if counter == 0:
        global im1pil
        global im1tk
        im1pil.save(str(randomname3) + ".png")
        im1pil = Image.open(str(randomname3) + ".png")
        im1pil = im1pil.convert('RGB')
        im1pil = im1pil.filter(ImageFilter.CONTOUR)
        im1pil.save(str(randomname3) + ".png")
        im1tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im1tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 1:
        global im2pil
        global im2tk
        im2pil.save(str(randomname3) + ".png")
        im2pil = Image.open(str(randomname3) + ".png")
        im2pil = im2pil.convert('RGB')
        im2pil = im2pil.filter(ImageFilter.CONTOUR)
        im2pil.save(str(randomname3) + ".png")
        im2tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im2tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 2:
        global im3pil
        global im3tk
        im3pil.save(str(randomname3) + ".png")
        im3pil = Image.open(str(randomname3) + ".png")
        im3pil = im3pil.convert('RGB')
        im3pil = im3pil.filter(ImageFilter.CONTOUR)
        im3pil.save(str(randomname3) + ".png")
        im3tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im3tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 3:
        global im4pil
        global im4tk
        im4pil.save(str(randomname3) + ".png")
        im4pil = Image.open(str(randomname3) + ".png")
        im4pil = im4pil.convert('RGB')
        im4pil = im4pil.filter(ImageFilter.CONTOUR)
        im4pil.save(str(randomname3) + ".png")
        im4tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im4tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 4:
        global im5pil
        global im5tk
        im5pil.save(str(randomname3) + ".png")
        im5pil = Image.open(str(randomname3) + ".png")
        im5pil = im5pil.convert('RGB')
        im5pil = im5pil.filter(ImageFilter.CONTOUR)
        im5pil.save(str(randomname3) + ".png")
        im5tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im5tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)


def emboss():
    randomname1 = random.randint(1, 10000)
    randomname2 = random.randint(1, 10000)
    randomname3 = randomname1 + randomname2
    if counter == 0:
        global im1pil
        global im1tk
        im1pil.save(str(randomname3) + ".png")
        im1pil = Image.open(str(randomname3) + ".png")
        im1pil = im1pil.convert('RGB')
        im1pil = im1pil.filter(ImageFilter.EMBOSS)
        im1pil.save(str(randomname3) + ".png")
        im1tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im1tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 1:
        global im2pil
        global im2tk
        im2pil.save(str(randomname3) + ".png")
        im2pil = Image.open(str(randomname3) + ".png")
        im2pil = im2pil.convert('RGB')
        im2pil = im2pil.filter(ImageFilter.EMBOSS)
        im2pil.save(str(randomname3) + ".png")
        im2tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im2tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 2:
        global im3pil
        global im3tk
        im3pil.save(str(randomname3) + ".png")
        im3pil = Image.open(str(randomname3) + ".png")
        im3pil = im3pil.convert('RGB')
        im3pil = im3pil.filter(ImageFilter.EMBOSS)
        im3pil.save(str(randomname3) + ".png")
        im3tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im3tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 3:
        global im4pil
        global im4tk
        im4pil.save(str(randomname3) + ".png")
        im4pil = Image.open(str(randomname3) + ".png")
        im4pil = im4pil.convert('RGB')
        im4pil = im4pil.filter(ImageFilter.EMBOSS)
        im4pil.save(str(randomname3) + ".png")
        im4tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im4tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 4:
        global im5pil
        global im5tk
        im5pil.save(str(randomname3) + ".png")
        im5pil = Image.open(str(randomname3) + ".png")
        im5pil = im5pil.convert('RGB')
        im5pil = im5pil.filter(ImageFilter.EMBOSS)
        im5pil.save(str(randomname3) + ".png")
        im5tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im5tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)


def croptheimage():
    global sizeentry
    global newsize
    size = int(sizeentry.get())
    xy1 = 256 - size
    xy2 = 256 + size
    randomname1 = random.randint(1, 10000)
    randomname2 = random.randint(1, 10000)
    randomname3 = randomname1 + randomname2
    if counter == 0:
        global im1pil
        global im1tk
        im1pil = im1pil.crop((xy1, xy1, xy2, xy2))
        im1pil = im1pil.resize(newsize, 0)
        im1pil.save(str(randomname3) + ".png")
        im1tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im1tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 1:
        global im2pil
        global im2tk
        im2pil = im2pil.crop((xy1, xy1, xy2, xy2))
        im2pil = im2pil.resize(newsize, 0)
        im2pil.save(str(randomname3) + ".png")
        im2tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im2tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 2:
        global im3pil
        global im3tk
        im3pil = im3pil.crop((xy1, xy1, xy2, xy2))
        im3pil = im3pil.resize(newsize, 0)
        im3pil.save(str(randomname3) + ".png")
        im3tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im3tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 3:
        global im4pil
        global im4tk
        im4pil = im4pil.crop((xy1, xy1, xy2, xy2))
        im4pil = im4pil.resize(newsize, 0)
        im4pil.save(str(randomname3) + ".png")
        im4tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im4tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)
    if counter == 4:
        global im5pil
        global im5tk
        im5pil = im5pil.crop((xy1, xy1, xy2, xy2))
        im5pil = im5pil.resize(newsize, 0)
        im5pil.save(str(randomname3) + ".png")
        im5tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im5tk)
        os.remove(str(randomname3) + ".png")
        winsound.PlaySound(editsound, winsound.SND_FILENAME)


def cropimage():
    global sizeentry
    cropwindow = Toplevel(root)
    cropwindow.title("Input Cropping Points")
    cropwindow.geometry("350x200")
    cropwindow.minsize(350, 200)
    cropwindow.maxsize(350, 200)
    cropwindow.resizable(False, False)
    sizelabel = Label(cropwindow, width=50, text='Size Of Pixels From Center')
    sizelabel.pack()
    sizeentry = Entry(cropwindow, width=50)
    sizeentry.pack()
    cropbutton = Button(cropwindow, text='Crop', command=croptheimage)
    cropbutton.pack()
    cropwindow.mainloop()


def musicon():
    pygame.mixer.music.unpause()


def musicoff():
    pygame.mixer.music.pause()


def helpinfo():
    def callback(url):
        webbrowser.open_new_tab(url)

    helpwindow = Toplevel(root)
    helpwindow.title("Info")
    helpwindow.geometry("350x160")
    helpwindow.minsize(350, 160)
    helpwindow.maxsize(350, 160)
    helpwindow.resizable(False, False)
    helptext = Label(helpwindow,
                     text="Credits:\nPython: Python Software Foundation.\nTkinter: Steen Lumholt and Guido van Rossum.\nPillow: Fredrik Lundh, Jeffrey A. Clark.\nPygame: Pete Shinners.\nWinsound: Python Software Foundation\nRandom: Python Software Foundation.\nOS: Python Software Foundation.\nWebBrowser: Python Software Foundation.\nMusic and sounds by Nintendo.",
                     font=('Minecraft Pixel Font 5x5 Regular', 6))
    helptext.pack()
    githublink = Label(helpwindow, text='Source Code', font=('Minecraft Pixel Font 5x5 Regular', 22), fg="blue",
                       cursor="hand2")
    githublink.pack()
    githublink.bind("<Button-1>", lambda e:
    callback("https://github.com/LandonPerkinsProsser/SimpleImageGalleryFilterer"))
    helpwindow.mainloop()


run_once = 0
if run_once == 0:
    defineimages()
    run_once = 1
imageLabel = Label(root, image=im1tk)
infoLabel = Label(root, text='Image ' + str(counter + 1) + ' of ' + str(len(image_list)),
                  font=('Minecraft Pixel Font 5x5 Regular', 20))
menubar1 = Menu(root)
filemenu1 = Menu(menubar1, tearoff=0)
filemenu1.add_command(label="Save", command=savefile)
filemenu1.add_command(label="Open", command=openfile)
filemenu1.add_command(label="Reset", command=resetimages)
menubar1.add_cascade(label="File", menu=filemenu1)
filemenu2 = Menu(menubar1, tearoff=0)
filemenu2.add_command(label="Blur", command=blur)
filemenu2.add_command(label="Sharpen", command=sharpen)
filemenu2.add_command(label="Smooth", command=smoothen)
filemenu2.add_command(label="Detail", command=detail)
filemenu2.add_command(label="Contour", command=contour)
filemenu2.add_command(label="Emboss", command=emboss)
filemenu2.add_command(label="Crop", command=cropimage)
menubar1.add_cascade(label="Edit", menu=filemenu2)
filemenu3 = Menu(menubar1, tearoff=0)
filemenu3.add_command(label="Music On", command=musicon)
filemenu3.add_command(label="Music Off", command=musicoff)
menubar1.add_cascade(label="Music", menu=filemenu3)
filemenu4 = Menu(menubar1, tearoff=0)
filemenu4.add_command(label="Info", command=helpinfo)
menubar1.add_cascade(label="Help", menu=filemenu4)
root.config(menu=menubar1)
nextbutton = Button(root, text="Next Image", font=('Minecraft Pixel Font 5x5 Regular', 20), command=nextimage)
backbutton = Button(root, text="Previous Image", font=('Minecraft Pixel Font 5x5 Regular', 20), command=lastimage)
infoLabel.pack()
imageLabel.pack()
nextbutton.pack()
backbutton.pack()
pygame.mixer.init()
pygame.mixer.music.load("music/album.wav")
pygame.mixer.music.play(-1)
root.mainloop()
