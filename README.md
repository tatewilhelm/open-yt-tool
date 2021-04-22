# Open YT Tool
Open Yt Tool is a Windows application used to download yt videos with a simple app. Check the audio button to download the audio form
of a video. Please read the disclaimer at DISCLAIMER.md<br>
<br>
Open YT Tool is under the GPL V3 license, more information is available in the file LICENSE. <br>

# Development
Open YT Tool is based off 4 modules, all modules use Python 3.9.<br>

```
tkinter is used as the GUI Module 
pytube used to download YT videos 
winreg used to get the Windows Download Folder 
webbrowser used to open Githubm link to DISCLAIMER.md
```

To compile Open YT Tool, use PyInstaller. Make sure that icon.png is in the same directory
as the output. Use the command below:<br>
Windows :<br>
`pyinstaller --noconsole --onedir `