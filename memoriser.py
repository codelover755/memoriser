from tkinter import *
from tkinter.filedialog import * 

window = Tk()
window.title("Memoriser")

open_button = Button(window,text="Open",width="15")
delete_button = Button(window,text="Delete",width="15")
save_button = Button(window,text="Save",width="15")
add_button = Button(window,text="Add",width="15")
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