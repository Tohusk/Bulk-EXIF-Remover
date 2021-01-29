import tkinter as tk
from tkinter import filedialog
import os
from PIL import ImageTk, Image
import piexif

root = tk.Tk()

folder_path = tk.StringVar()

def remove_exif(filename):
    image = Image.open(filename)

    if "exif" in image.info:
        exif_dict = piexif.load(image.info["exif"])

        # rotate accordingly
        if piexif.ImageIFD.Orientation in exif_dict["0th"]:
            orientation = exif_dict["0th"].pop(piexif.ImageIFD.Orientation)
            if orientation == 2:
                image = image.transpose(Image.FLIP_LEFT_RIGHT)
            elif orientation == 3:
                image = image.rotate(180)
            elif orientation == 4:
                image = image.rotate(180).transpose(Image.FLIP_LEFT_RIGHT)
            elif orientation == 5:
                image = image.rotate(-90, expand=True).transpose(Image.FLIP_LEFT_RIGHT)
            elif orientation == 6:
                image = image.rotate(-90, expand=True)
            elif orientation == 7:
                image = image.rotate(90, expand=True).transpose(Image.FLIP_LEFT_RIGHT)
            elif orientation == 8:
                image = image.rotate(90, expand=True)

            newfilename = filename.split('.')[0] + "_1" + '.' + filename.split('.')[1]
            image.save(newfilename, quality=95)
            piexif.remove(newfilename)
    else:
        print("Image skipped")

            

def process_images():
    directory = folder_path.get()
    for filename in os.listdir(directory):
        # jpg or tif or wav
        if filename.endswith(".jpg") or filename.endswith(".png"):
            print("Current photo is:", directory + filename)
            remove_exif(directory + filename)


def browse_directory():
    # open directory browser and let user pick a folder
    folder_selected = filedialog.askdirectory(parent=root, title="Choose folder of images to remove EXIF data from")
    folder_selected = folder_selected + "/"
    print(folder_selected, "is the folder selected")
    directory_label.config(text=folder_selected)
    folder_path.set(folder_selected)
    remove_exif_button.config(state=tk.NORMAL)

remove_exif_button = tk.Button(root, text="Remove Exif", padx=20, pady=5, command=process_images, state=tk.DISABLED)
remove_exif_button.grid(row=1, column=1)

directory_label = tk.Label(root, text="No directory selected")
directory_label.grid(row=0, column=1)

browse_directory_button = tk.Button(root, text="Choose Directory", padx=20, pady=20, command=browse_directory)
browse_directory_button.grid(row=0, column=0)

root.mainloop()