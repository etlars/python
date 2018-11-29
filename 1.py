


from tkinter import *

root = Tk()

red = IntVar()
red.set(0)
blue= IntVar()
blue.set(0)
green= IntVar()
green.set(0)


def change_color(n):
    color='#%02x%02x%02x'%(red.get(),blue.get(), green.get())
    button.configure(bg=color)


button = Button(root, text = 'button', bg = 'pink')
button.pack(fill='both')


s1= Scale(root, label = 'red', orient = 'v', from_=0, to=255, variable=red, command=change_color)
s2= Scale(root, label = 'blue', orient = 'v', from_=0, to=255, variable=blue, command=change_color)
s3= Scale(root, label = 'green', orient = 'v', from_=0, to=255, variable=green, command=change_color)


s1.pack(fill='both')
s2.pack(fill='both')
s3.pack(fill='both')


root.mainloop();
