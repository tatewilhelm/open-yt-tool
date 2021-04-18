# Open YT Tool
# A Capital I Project

# imports
import tkinter.messagebox
import webbrowser
from tkinter import *
from pytube import *
from winreg import *

# Getting the downloads folder
with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
    Downloads = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]

# Functions called on events
def callback(url):
    webbrowser.open_new(url)


def buttonPressed():
    try:
        yt = YouTube(ent.get())
        yt.streams.first().download(Downloads)
        tkinter.messagebox.showinfo("Open YT Tool", "Downloaded Successfully!")
    except:
        tkinter.messagebox.showerror("Open YT Tool",
                                     "Cannot Connect to Internet, or invalid link. \nCheck your internet connection.")

# Window
root = Tk()
root.title("Open YT Tool")
root.geometry("250x125")
root.resizable(False, False)
p = PhotoImage(file='icon.png')
root.iconphoto(False, p)


# Window Attributes
txt = Label(root, text="Enter a Valid YouTube URL")
txt.pack(side=TOP)

ent = Entry(root)
ent.pack(side=TOP)

txt1 = Label(root, text="Before downloading, read the disclaimer at")
txt1.pack(side=TOP)

link = Label(root, text="https://github.com", fg="blue", cursor="hand2")
link.pack(side=TOP)
link.bind("<Button-1>", lambda e: callback("https://github.com/capital-I/open-yt-tool/blob/main/DISCLAIMER.md"))

btn = Button(root, text="Download", command=buttonPressed)
btn.pack(side=TOP)


# Mainloop
root.mainloop()
