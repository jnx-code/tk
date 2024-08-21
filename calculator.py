from tkinter import *
def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()
        
    elif text == "c":
        scvalue.set("")
        scvalue.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
        
root = Tk()
root.title("MY CALCULATOR")
# root.wm_iconbitmap("1.icon")
root.geometry("500x900")

scvalue = StringVar()
scvalue.set("")

screen = Entry(root,textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=5, padx=10,pady=0)

f = Frame(root,bg="grey")
b = Button(f,text="9",padx=20,pady=8, font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button>", click)

b = Button(f,text="8",padx=20,pady=8, font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button>", click)

b = Button(f,text="7",padx=20,pady=8, font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button>", click)
f.pack()

f = Frame(root,bg="grey")
b = Button(f,text="6",padx=20,pady=8, font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button>", click)

b = Button(f,text="5",padx=20,pady=8, font="lucida 35 bold")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button>", click)

b = Button(f,text="4",padx=20,pady=8, font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button>", click)
f.pack()

f = Frame(root,bg="grey")
b = Button(f,text="3",padx=20,pady=8, font="lucida 35 bold")
b.pack(side=LEFT,padx=16,pady=5)
b.bind("<Button>", click)

b = Button(f,text="2",padx=20,pady=8, font="lucida 35 bold")
b.pack(side=LEFT,padx=16,pady=5)
b.bind("<Button>", click)

b = Button(f,text="1",padx=20,pady=8, font="lucida 35 bold")
b.pack(side=LEFT,padx=16,pady=5)
b.bind("<Button>", click)
f.pack()

f = Frame(root,bg="grey")
b = Button(f,text="0",padx=20,pady=8, font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button>", click)

b = Button(f,text="+",padx=20,pady=8, font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button>", click)

b = Button(f,text="-",padx=25,pady=8, font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button>", click)
f.pack()

f = Frame(root,bg="grey")
b = Button(f,text="*",padx=8,pady=8, font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button>", click)

b = Button(f,text="%",padx=8,pady=8, font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button>", click)

b = Button(f,text="c",padx=8,pady=8,bg="blue", font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button>", click)

b = Button(f,text="=",padx=8,pady=8,bg="orange", font="lucida 35 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button>", click)




f.pack()

# f = Frame(root,bg="grey")
# b = Button(f,text="c",padx=15,pady=8, font="lucida 35 bold")
# b.pack(side=LEFT,padx=15,pady=5)
# b.bind("<Button>", click)
# f.pack()

root.mainloop()