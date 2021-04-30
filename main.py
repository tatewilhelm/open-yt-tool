# Open YT Tool
# A Capital I Project

# Imports
import platform
import os
from tkinter import *
import tkinter.messagebox
from pytube import *
import webbrowser

# Platform download folder being found
if platform.system() == "Windows":
    from winreg import *

    # Getting Windows download path registry
    with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
        Downloads = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]
elif platform.system() == "Darwin" or platform.system() == "Linux":
    # Compatible with Linux and Mac
    Downloads = os.path.expanduser("~") + "/Downloads/"
else:
    print("Open YT Tool is not compatible with your OS.")
    exit()


# Function called on text being pressed, used to open disclaimer
def callback(url):
    webbrowser.open_new(url)


# Function called to download video on being called
def buttonPressed():
    if audioCheck.get() == 0:
        print("Video")
        try:
            yt = YouTube(ent.get())
            yt.streams.first().download(Downloads)
            tkinter.messagebox.showinfo("Open YT Tool", "Downloaded Successfully!")
        except:
            tkinter.messagebox.showerror("Open YT Tool",
                                       "Cannot Connect to Internet, or invalid link. \nCheck your internet connection.")
    else:
        print("Audio")
        try:
            yt = YouTube(ent.get())
            yt.streams.last().download(Downloads)
            tkinter.messagebox.showinfo("Open YT Tool", "Downloaded Successfully!")
        except:
            tkinter.messagebox.showerror("Open YT Tool",
                                       "Cannot Connect to Internet, or invalid link. \nCheck your internet connection.")


# Window
root = Tk()
root.title("Open YT Tool")
root.geometry("250x140")
root.resizable(False, False)
p = PhotoImage(file='icon.png')
root.iconphoto(False, p)

# Variables
audioCheck = IntVar()

# Window Elements and Attributes
txt = Label(root, text="Enter a Valid YouTube URL")
txt.pack(side=TOP)

ent = Entry(root)
ent.pack(side=TOP)

aud = Checkbutton(root, text="Audio? ", variable=audioCheck)
aud.pack(side=TOP)

txt1 = Label(root, text="Before downloading, read the disclaimer at")
txt1.pack(side=TOP)

link = Label(root, text="https://github.com/ (click here)", fg="blue", cursor="hand2")
link.pack(side=TOP)
link.bind("<Button-1>", lambda e: callback("https://github.com/capital-I/open-yt-tool/blob/main/DISCLAIMER.md"))

btn = Button(root, text="Download", command=buttonPressed)
btn.pack(side=TOP)

# Mainloop

root.mainloop()
