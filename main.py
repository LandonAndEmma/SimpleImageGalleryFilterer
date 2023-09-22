from tkinter import *
from PIL import ImageTk, Image, ImageFilter
import pygame
import random
import os

root = Tk()
root.title('Image Slideshow Program')
root.geometry('512x635')
icon = PhotoImage(file='images/icon.png')
root.iconphoto(True, icon)
root.minsize(512, 635)
root.maxsize(512, 635)
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


def save():
    randomname1 = random.randint(1, 10000)
    randomname2 = random.randint(1, 10000)
    randomname3 = randomname1 + randomname2
    if counter == 0:
        global im1pil
        global im1tk
        im1pil.save(str(randomname3) + ".png")
        im1tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im1tk)
    if counter == 1:
        global im2pil
        global im2tk
        im2pil.save(str(randomname3) + ".png")
        im2tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im2tk)
    if counter == 2:
        global im3pil
        global im3tk
        im3pil.save(str(randomname3) + ".png")
        im3tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im3tk)
    if counter == 3:
        global im4pil
        global im4tk
        im4pil.save(str(randomname3) + ".png")
        im4tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im4tk)
    if counter == 4:
        global im5pil
        global im5tk
        im5pil.save(str(randomname3) + ".png")
        im5tk = PhotoImage(file=str(randomname3) + ".png")
        imageLabel.config(image=im5tk)


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


def helpinfo():
    helpwindow = Toplevel(root)
    helpwindow.title("Help")
    helpwindow.geometry("250x250")
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
filemenu1.add_command(label="Save", command=save)
menubar1.add_cascade(label="File", menu=filemenu1)
filemenu2 = Menu(menubar1, tearoff=0)
filemenu2.add_command(label="Blur", command=blur)
filemenu2.add_command(label="Sharpen", command=sharpen)
menubar1.add_cascade(label="Edit", menu=filemenu2)
filemenu3 = Menu(menubar1, tearoff=0)
filemenu3.add_command(label="Info", command=helpinfo)
menubar1.add_cascade(label="Help", menu=filemenu3)
root.config(menu=menubar1)
button = Button(root, text="Next Image", font=('Minecraft Pixel Font 5x5 Regular', 20), command=nextimage)
infoLabel.pack()
imageLabel.pack()
button.pack()
pygame.mixer.init()
pygame.mixer.music.load("music/album.wav")
pygame.mixer.music.play(-1)
root.mainloop()
