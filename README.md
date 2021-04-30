# Open YT Tool
Open Yt Tool is a Windows application used to download yt videos with a simple app. Check the audio button to download the audio form
of a video. Please read the disclaimer at DISCLAIMER.md<br>
<br>
Open YT Tool is under the GPL V3 license, more information is available in the file LICENSE. <br>

# Development
Open YT Tool is based off 6 modules, all modules use Python 3.<br>

```
tkinter is used as the GUI Module 
pytube used to download YT videos 
winreg used to get the Windows Download Folder 
webbrowser used to open Github link to DISCLAIMER.md
platform used to get the current os's name
os used to combine files
```
Use Python 3 when using Open YT Tool. <br>
<br>
To compile Open YT Tool for releases, use PyInstaller. Make sure that icon.png is in the same directory
as the output. Use the command below:<br>

Windows:<br>
`pyinstaller --noconsole --onefile --icon=icon.ico main.py`

Linux:<br>
`pyinstaller --noconsole --onefile --icon=icon.png main.py`

Mac:<br>
`pyinstaller --noconsole --onefile --icon=icon.png main.py`