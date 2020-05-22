prtkl4Bwap to create message box

from tkinter import*
master=Tk()
ab="hello fycs"
msg=Message(master,text=ab)
msg.config(bg='light green',font=('items',24,'italic'))
msg.pack()
mainloop()
