from PIL import Image, ImageTk 
import tkinter as tk 

root = tk.Tk()
img = Image.open("image.gif")
tkimage = ImageTk.PhotoImage(img)
tk.Label(root, image=tkimage).pack()
root.mainloop()
