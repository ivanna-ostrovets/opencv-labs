import tkinter as tk
from tkinter import filedialog

from lab_10 import lab_10
from lab_11_morphological import lab_11_morphological
from lab_11_transform import lab_11_transform
from lab_12 import lab_12
from lab_13 import lab_13
from lab_15 import lab_15
from lab_9 import lab_9

root = tk.Tk()
root.title("onenCV labs")


def open_file():
    return filedialog.askopenfilename(initialdir="initialdir", title="Select file",
                                      filetypes=(("png files", "*.png"), ("all files", "*.*")))


def exec_lab(func):
    def inner():
        func(open_file())

    return inner


lab_9_button = tk.Button(root, text="Lab 9: open image with openCV", width=50, command=exec_lab(lab_9))
lab_9_button.pack()

lab_10_button = tk.Button(root, text="Lab 10: image histogram", width=50, command=exec_lab(lab_10))
lab_10_button.pack()

lab_11_button_transform = tk.Button(root, text="Lab 11: image transformations", width=50, command=exec_lab(lab_11_transform))
lab_11_button_transform.pack()

lab_11_button_morphological = tk.Button(root, text="Lab 11: morphological transformations", width=50, command=exec_lab(lab_11_morphological))
lab_11_button_morphological.pack()

lab_12_button = tk.Button(root, text="Lab 12: object recognition", width=50, command=exec_lab(lab_12))
lab_12_button.pack()

lab_13_button = tk.Button(root, text="Lab 13: finding contour", width=50, command=exec_lab(lab_13))
lab_13_button.pack()

lab_15_button = tk.Button(root, text="Lab 15: Haar-like feature", width=50, command=exec_lab(lab_15))
lab_15_button.pack()

exit_button = tk.Button(root, text="Exit", width=50, command=root.destroy)
exit_button.pack()

root.mainloop()
