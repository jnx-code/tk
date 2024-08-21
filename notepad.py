from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("untitled - notepad")
    file = None
    TextArea.delete(1.0, END)
    
def openFile():
    global file
    file = asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.*")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()
        
def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.*")])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + "-notepad")
            print("file saved")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
        
def quitApp():
    root.destroy()
    
def cut():
    TextArea.event_generate(("<<Cut>>"))
    
def copy():
    TextArea.event_generate(("<<Copy>>"))
    
def paste():
    TextArea.event_generate(("<<Paste>>"))
    
def about():
    showinfo("Notepad", "Notepad by juned")

if __name__ == '__main__':
    root = Tk()
    root.geometry("650x550")
    root.title("untitled - notepad")
    
    TextArea = Text(root,font="lucida 13")
    file = None
    TextArea.pack(expand=True,fill=BOTH)
    
    MenuBar = Menu(root)
    
    FileMenu = Menu(MenuBar, tearoff=0)
    FileMenu.add_command(label="New", command=newFile)
    FileMenu.add_command(label="Open", command= openFile)
    FileMenu.add_command(label="Save", command= saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label= "Exit",command=quitApp)
    MenuBar.add_cascade(label= "File", menu=FileMenu)
    
    #edit menu
    EditMenu = Menu(MenuBar,tearoff=0)
    EditMenu.add_command(label= "cut", command=cut)
    EditMenu.add_command(label= "copy", command=copy)
    EditMenu.add_command(label= "paste", command=paste)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)
    
    #help menu
    HelpMenu = Menu(MenuBar,tearoff=0)
    HelpMenu.add_command(label="about notepad",command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)
    
    #scroll bar
    scroll = Scrollbar(TextArea)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scroll.set)
    
    root.config(menu=MenuBar)
    root.mainloop()