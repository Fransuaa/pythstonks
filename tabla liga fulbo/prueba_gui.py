from customtkinter import *

root=CTk()
frame=CTkFrame(root)

root.title("Prueba GUI")
root.resizable(1,1) 
root.geometry("700x500")
root.config(bg="Blue")
root.iconbitmap("")    
      
# frame.config(bg="red")
# frame.config(width="500",height="300")
# frame.pack()

# frame.config(bd=35)
# frame.config(relief=SUNKEN)
# frame.config(cursor="pirate")

root.mainloop()