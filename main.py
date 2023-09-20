from tkinter import *
from PIL import ImageTk, Image
import pygame

root = Tk()
root.title('Image Slideshow Program')
root.geometry('512x635')
icon = PhotoImage(file='images/icon.png')
root.iconphoto(True, icon)
root.minsize(512, 635)
root.maxsize(512, 635)
root.resizable(False, False)
im1 = ImageTk.PhotoImage(Image.open('images/aliendude.png'))
im2 = ImageTk.PhotoImage(Image.open('images/bluesmurfcat.png'))
im3 = ImageTk.PhotoImage(Image.open('images/imspongebob.png'))
im4 = ImageTk.PhotoImage(Image.open('images/jonesy.png'))
im5 = ImageTk.PhotoImage(Image.open('images/pythonlogo.png'))
image_list = [im1, im2, im3, im4, im5]
counter = 0


def nextimage():
    global counter
    if counter < len(image_list) - 1:
        counter += 1
    else:
        counter = 0
    imageLabel.configure(image=image_list[counter])
    infoLabel.config(text='Image ' + str(counter + 1) + ' of ' + str(len(image_list)))


imageLabel = Label(root, image=im1)
infoLabel = Label(root, text='Image ' + str(counter + 1) + ' of ' + str(len(image_list)),
                  font=('Minecraft Pixel Font 5x5 Regular', 20))
button = Button(root, text="Next Image", font=('Minecraft Pixel Font 5x5 Regular', 20), command=nextimage)
infoLabel.pack()
imageLabel.pack()
button.pack()
pygame.mixer.init()
pygame.mixer.music.load("music/album.wav")
pygame.mixer.music.play(-1)
root.mainloop()
