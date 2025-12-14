from tkinter import *
from time import strftime
root=Tk()
root.geometry("400x200")
root.title("DIGITAL CLOCK BY VISHAL")
root.config(bg="green")
l1=Label(root,text="Vishal Gautam",bg="green",fg="white")
l1.pack(pady="15")
l2=Label(root,text="TIME",bg="green",fg="white",font=("digital",40))
l2.pack(pady="15")

def demo():
	x=strftime("%H:%M:%S")
	l2.config(text=x)
	l2.after(1000,demo)
demo()	
	
root.mainloop()