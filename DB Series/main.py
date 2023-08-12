import tkinter as tk
import customtkinter as ctk

ctk.set_appearance_mode("system")  # Modes: system (default), light, dark
ctk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

root = ctk.CTk()  # create CTk window like you do with the Tk window
root.geometry("400x240")

def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
button = ctk.CTkButton(master=root, text="CTkButton", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

root.mainloop()