import tkinter as tk
from tkinter import filedialog
import subprocess

'''
I've created this program for self-learning, as I've just started learning about python.
If you want to give it a try, change the default folders by the ones you use
Feel free to leave any comment or improve my noob code!
'''

def getDestFolder(folder): # open a "choose folder" dialog
    global locText # defining a global var that keeps the value of the location entry: path where the songs are saved
    locText = None # setting it to None
    destFolder = tk.filedialog.askdirectory(initialdir=r'/') # default folder shown when open the dialog
    location.insert(0,destFolder) # location entry's text is set to the selected path
    locText = location.get() # now "locText" gets the value of "location" entry, which is the desired path

def parseYoutube(url): # the main function, which calls the powersell and executes youtube-dl
    if locText == None: # check whether the user has selected a custom folder
        subprocess.call([r'C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe', r'C:\Youtube\dl\youtube-dl -i --extract-audio --audio-format mp3 ' +  r'"'+entry.get() +r'"'+ r' -o "C:\Users\myUser\Music\Youtube\dl\%(title)s.%(ext)s" '+entry.get()])
    else:
        subprocess.call([r'C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe', r'C:\Youtube\dl\youtube-dl -i --extract-audio --audio-format mp3 ' +  r'"'+entry.get()+r'"'+ r' -o "'+locText+r'/%(title)s.%(ext)s" ' + r'"'+entry.get() +r'"'])
    window.destroy()

window = tk.Tk() # create main tkinter window, to which everything is referred to
window.title("Youtube-dl GUI") 
window.configure(bg="white")
window.resizable(0,0)

# labels' definition
tk.Label(window, text="Youtube-dl GUI", bg="white", font = ("Arial", 14, "bold"))
tk.Label(window, text="Enter your URL (sole video or playlist): ", bg="white", font = ("Arial", 11)).grid(column=2, row=2, padx=6, pady=14)
tk.Label(window, text="Enter a path to save your files: ", bg="white", font = ("Arial", 11)).grid(column=2, row=4, padx=4, pady=14)

# defining entry of url
entry = tk.Entry(window, width=60, font = ("Arial", 12), justify='center',borderwidth=4,relief='groove', insertwidth=1) # define new tk entry
entry.grid(column=2,row=3,padx=10,pady=15)
entry.focus_set() # get the focus on this entry
entry.bind("<Return>", parseYoutube) # bind the Return key to the url entry, call the function "parseYoutube"
# definining the "choose path" entry box
location = tk.Entry(window, width=60, font = ("Arial", 12), justify='center',borderwidth=4,relief='groove', insertwidth=1)
location.grid(column=2,row=5, padx=10,pady=15)
location.insert(0,'You can leave this empty and the default folder will be Youtube-dl\'s one')
location.bind("<Button-1>",getDestFolder) # bind mouse's left button to the path entry, so it calls the "getDestFolder" function 

# defining Download button, it does the sames as pressing Intro if entry has focus
ent_bttn = tk.Button(window, text="Download!") # create tkinter button, which calls the "parseYoutube" function
ent_bttn.grid(column=2,rows=6,padx=5)
ent_bttn.bind("<Button-1>",parseYoutube)

tk.mainloop() # finish execution of code
