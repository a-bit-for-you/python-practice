prtkl4D:  wap to create buttons

from tkinter import*
root=Tk()
frame=Frame(root)
frame.pack()
bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM)
redbutton=Button(frame,text="red",fg="red")
redbutton.pack(side=LEFT)
greenbutton=Button(frame,text="green",fg="green")
greenbutton.pack(side=LEFT)
bluebutton=Button(frame,text="blue",fg="blue")
bluebutton.pack(LEFT)
root.mainloop()
