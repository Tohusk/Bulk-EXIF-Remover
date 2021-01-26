from tkinter import Tk, Button, filedialog, StringVar

root = Tk()

def browse_directory():
    # open directory browser and let user pick a folder
    folder_selected = filedialog.askdirectory()
    folder_path.set(folder_selected)
    print(folder_selected, "is the folder selected")
    



folder_path = StringVar()

# myLabel = Label(root, text="Enter Directory:")
browse_directory_button = Button(root, text="Enter Directory", padx=50, pady=20, command=browse_directory)

browse_directory_button.grid(row=0, column=0)


browse_directory_button.pack()

root.mainloop()

