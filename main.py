import os
import random
import webbrowser
import pygame
from PIL import Image, ImageFilter, ImageOps, ImageTk
from tkinter import Button, Entry, Frame, Label, Menu, PhotoImage, Tk, Toplevel, filedialog, messagebox
SOUNDS = {'click': 'sounds/click.wav', 'edit': 'sounds/edit.wav', 'success': 'sounds/success.wav'}
NEW_SIZE = (512, 512)
root = Tk()
root.title('Simple Image Gallery Filterer')
root.geometry('512x707')
root.resizable(False, False)
root.iconphoto(True, PhotoImage(file='images/icon.png'))
image_data = {}
image_tk_list = []
for i in range(1, 6):
    pil_image = Image.open(f"images/image{i}.png")
    tk_image = ImageTk.PhotoImage(pil_image)
    image_data[i] = {'pil': pil_image}
    image_tk_list.append(tk_image)
counter = 0
def resize_image(image, size):
    return image.resize(size)
def crop_image_window():
    crop_window = Toplevel(root)
    crop_window.title("Input Cropping Points")
    crop_window.geometry("350x200")
    crop_window.minsize(350, 200)
    crop_window.maxsize(350, 200)
    crop_window.resizable(False, False)
    size_label = Label(crop_window, width=50, text='Size Of Pixels From Center')
    size_label.pack()
    global size_entry
    size_entry = Entry(crop_window, width=50)
    size_entry.pack()
    crop_button = Button(crop_window, text='Crop', command=crop_image_and_update_label)
    crop_button.pack()
    crop_window.mainloop()
def crop_image_and_update_label():
    global counter
    pil_image = image_data[counter + 1]['pil']
    size = int(size_entry.get())
    x = ((size // 2) * -1) + 256
    y = size // 2 + 256
    cropped_pil_image = pil_image.crop((x, x, y, y))
    resized_pil_image = cropped_pil_image.resize((512, 512))
    resized_tk_image = ImageTk.PhotoImage(resized_pil_image)
    image_data[counter + 1]['pil'] = resized_pil_image
    image_data[counter + 1]['tk'] = resized_tk_image
    image_tk_list[counter] = resized_tk_image
    update_image()
    play_sound('edit')
def show_error_message(message):
    messagebox.showerror("Error", message)
def play_sound(sound):
    pygame.mixer.Sound(SOUNDS[sound]).play()
def update_image():
    global counter
    image_label.configure(image=image_tk_list[counter])
    info_label.config(text=f'Image {counter + 1} of {len(image_tk_list)}')
def next_image():
    global counter
    play_sound('click')
    counter = (counter + 1) % len(image_tk_list)
    update_image()
def previous_image():
    global counter
    play_sound('click')
    counter = (counter - 1) % len(image_tk_list)
    update_image()
def save_image():
    global counter
    pil_image = image_data[counter + 1]['pil']
    filename = filedialog.asksaveasfilename(
        initialdir="/",
        title="Save As",
        filetypes=(
            ("Image files", "*.png;*.jpeg;*.jpg;*.bmp;*.dds;*.webp;*.tga;*.dds"),
            ("All files", "*.*")
        )
    )
    if filename:
        pil_image.save(filename)
        play_sound('success')
def apply_filter(filter_type):
    global counter
    pil_image = image_data[counter + 1]['pil']
    if pil_image.mode != 'RGB':
        pil_image = pil_image.convert('RGB')
    pil_image_filtered = pil_image.filter(getattr(ImageFilter, filter_type.upper()))
    image_data[counter + 1]['pil'] = pil_image_filtered
    image_data[counter + 1]['tk'] = ImageTk.PhotoImage(pil_image_filtered)
    image_tk_list[counter] = image_data[counter + 1]['tk']
    update_image()
    play_sound('edit')
def invert_colors():
    global counter
    pil_image = image_data[counter + 1]['pil']
    if pil_image.mode != 'RGB':
        pil_image = pil_image.convert('RGB')
    inverted_pil_image = ImageOps.invert(pil_image)
    image_data[counter + 1]['pil'] = inverted_pil_image
    image_data[counter + 1]['tk'] = ImageTk.PhotoImage(inverted_pil_image)
    image_tk_list[counter] = image_data[counter + 1]['tk']
    update_image()
    play_sound('edit')
def rotate_image(angle):
    global counter
    pil_image = image_data[counter + 1]['pil'].rotate(angle, expand=True)
    image_data[counter + 1]['pil'] = pil_image
    image_data[counter + 1]['tk'] = ImageTk.PhotoImage(pil_image)
    image_tk_list[counter] = image_data[counter + 1]['tk']
    update_image()
    play_sound('edit')
def flip_or_mirror(action):
    global counter
    pil_image = getattr(ImageOps, action.lower())(image_data[counter + 1]['pil'])
    image_data[counter + 1]['pil'] = pil_image
    image_data[counter + 1]['tk'] = ImageTk.PhotoImage(pil_image)
    image_tk_list[counter] = image_data[counter + 1]['tk']
    update_image()
    play_sound('edit')
def open_file():
    global counter
    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Open",
        filetypes=(
            ("Image files", "*.png;*.jpeg;*.jpg;*.bmp;*.xpm;*.dds;*.psd;*.webp;*.tiff;*.tga;*.dds;*.dib;*.icns;*.ico;*.im;*.msp;*.wmf;*.emf;*.pcx;*.pbm;*.ppm;*.pgm;*.pnm;*.sgi;*.blp;*.eps;*.sun;*.wal"),
            ("All files", "*.*")
        )
    )
    if filename:
        try:
            pil_image = Image.open(filename)
            pil_image_resized = resize_image(pil_image, (512, 512))
            tk_image = ImageTk.PhotoImage(pil_image_resized)
            counter = len(image_data)
            image_data[counter + 1] = {'pil': pil_image_resized, 'tk': tk_image}
            image_tk_list.append(tk_image)
            update_image()
            play_sound('success')
        except Exception as e:
            show_error_message(f"Error opening image: {e}")
def save_file():
    filename = filedialog.asksaveasfilename(
        initialdir="/",
        title="Save As",
        filetypes=(
            ("Image files", "*.png;*.jpeg;*.jpg;*.bmp;*.dds;*.webp;*.tga;*.dds"),
            ("All files", "*.*")
        )
    )
def help_info():
    def callback(url):
        webbrowser.open_new_tab(url)
    help_window = Toplevel(root)
    help_window.title("Info")
    help_window.geometry("350x160")
    help_window.resizable(False, False)
    help_text = Label(
        help_window,
        text="Credits:\nPython: Python Software Foundation.\nTkinter: Steen Lumholt and Guido van Rossum.\n"
             "Pillow: Fredrik Lundh, Jeffrey A. Clark.\nPygame: Pete Shinners.\nWinsound: Python Software Foundation\n"
             "Random: Python Software Foundation.\nOS: Python Software Foundation.\n"
             "WebBrowser: Python Software Foundation.\nMusic and sounds by Nintendo.",
        font=('Arial', 7)
    )
    help_text.pack()
    github_link = Label(
        help_window,
        text='Source Code',
        font=('Arial', 22),
        fg="blue",
        cursor="hand2"
    )
    github_link.pack()
    github_link.bind("<Button-1>", lambda e: callback("https://github.com/LandonPerkinsProsser/SimpleImageGalleryFilterer"))
    help_window.mainloop()
def music_on():
    pygame.mixer.music.unpause()
def music_off():
    pygame.mixer.music.pause()
def close_gui():
    root.destroy()
    quit()
image_label = Label(root, image=image_tk_list[counter])
info_label = Label(root, text=f'Image {counter + 1} of {len(image_tk_list)}')
next_button = Button(root, text="Next Image", command=next_image, width=34, height=10)
back_button = Button(root, text="Previous Image", command=previous_image, width=34, height=10)
menubar = Menu(root)
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Save", command=save_image)
file_menu.add_command(label="Open", command=open_file)
menubar.add_cascade(label="File", menu=file_menu)
edit_menu = Menu(menubar, tearoff=0)
edit_menu.add_command(label="Blur", command=lambda: apply_filter('blur'))
edit_menu.add_command(label="Sharpen", command=lambda: apply_filter('sharpen'))
edit_menu.add_command(label="Smooth", command=lambda: apply_filter('smooth'))
edit_menu.add_command(label="Detail", command=lambda: apply_filter('detail'))
edit_menu.add_command(label="Contour", command=lambda: apply_filter('contour'))
edit_menu.add_command(label="Emboss", command=lambda: apply_filter('emboss'))
edit_menu.add_command(label="Invert Colors", command=invert_colors)
edit_menu.add_command(label="Crop", command=crop_image_window)
edit_menu.add_command(label="Rotate Right", command=lambda: rotate_image(90))
edit_menu.add_command(label="Rotate Left", command=lambda: rotate_image(-90))
edit_menu.add_command(label="Flip", command=lambda: flip_or_mirror('flip'))
edit_menu.add_command(label="Mirror", command=lambda: flip_or_mirror('mirror'))
menubar.add_cascade(label="Edit", menu=edit_menu)
music_menu = Menu(menubar, tearoff=0)
music_menu.add_command(label="Music On", command=music_on)
music_menu.add_command(label="Music Off", command=music_off)
menubar.add_cascade(label="Music", menu=music_menu)
help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label="Info", command=help_info)
menubar.add_cascade(label="Help", menu=help_menu)
root.config(menu=menubar)
info_label.pack()
image_label.pack()
button_frame = Frame(root)
button_frame.pack(side="bottom", fill="x")
back_button.pack(side="left", padx=5, pady=5)
next_button.pack(side="right", padx=5, pady=5)
pygame.mixer.init()
pygame.mixer.music.load("music/album.wav")
pygame.mixer.music.play(-1)
root.protocol("WM_DELETE_WINDOW", close_gui)
root.mainloop()
