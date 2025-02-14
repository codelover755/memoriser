from tkinter import *
from tkinter.filedialog import * 

window = Tk()
window.title("Memoriser")

def open_file():
    f = askopenfile(title="Open File")
    if f is not None:
        listbox.delete(0,END)#deletes all items
        item = f.readlines()
        for i in item:
            listbox.insert(END,i) # inserted just after the deleted part

def add_item():
    t = entry.get()
    listbox.insert(END,t)

def save_file():
    s = asksaveasfile(defaultextension=".txt")
    if s is not None:
        for i in listbox.get(0,END):
            print(i,file=s)

def delete_item():
    index = listbox.curselection()#select the cursor item and returns index value
    listbox.delete(index)

open_button = Button(window,text="Open",width="15",command=open_file)
delete_button = Button(window,text="Delete",width="15",command=delete_item)
save_button = Button(window,text="Save",width="15",command=save_file)
add_button = Button(window,text="Add",width="15",command=add_item)
entry = Entry(window, width=35)

open_button.pack(side=LEFT,padx=5,pady=5)
delete_button.pack(side=RIGHT,padx=5,pady=5)
save_button.pack(padx=5,pady=5)
entry.pack(padx=5,pady=5)
add_button.pack(padx=5,pady=5)

frame = Frame(window)
scrollbar = Scrollbar(frame,orient="vertical")
scrollbar.pack(side=RIGHT,fill=Y)
listbox = Listbox(frame,width=70,yscrollcommand=scrollbar.set,bg="red")
for i in range(15):
    listbox.insert(END,str(i))
frame.pack(side=RIGHT)
listbox.pack(side=LEFT)
scrollbar.pack(side=RIGHT)

window.mainloop()
