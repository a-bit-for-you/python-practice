prtkl5A: wap for creating radio button

from tkinter import*
def sel():
    selection="your selected option"+str(var.get())
    Label.config(text=selection)
root=Tk()
var=IntVar()
R1=Radiobutton(root,text="option1",variable=var,value=1,command=sel)
R1.pack()
R2=Radiobutton(root,text="option2",variable=var,value=2,command=sel)
R2.pack()
R3=Radiobutton(root,text="option3",variable=var,value=3,command=sel)
R3.pack()
Label=Label(root)
Label.pack()
root.mainloop()
