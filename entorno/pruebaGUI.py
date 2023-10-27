import tkinter as tk

app = tk.Tk()
palabra=tk.StringVar(app)
entrada=tk.StringVar(app)

def saludar(a):
    print("Holaaa!",a)

def wordChange():
    palabra.set("Marihuana "+entrada.get())

#dimensiones (ANCHOxALTO)
app.geometry("600x300")
app.configure(background="black")
tk.Wm.wm_title(app, "sex machine")

tk.Button(
    app,
    text="APREMATE",
    font=("Time New Romans",22),
    bg="Pink",
    fg="white",
    command=wordChange,
    relief="flat",
).pack(
    fill=tk.BOTH,
    expand=True
)
tk.Label(
    app,
    text="im darth vader",
    textvariable=palabra,
    fg="white",
    bg="blue",
    justify="center",
).pack(
    fill=tk.BOTH,
    expand=True
)
tk.Entry(
    app,
    text="im a barbie girl",
    fg="white",
    bg="blue",
    justify="center",
    textvariable=entrada
).pack(
    fill=tk.BOTH,
    expand=True
)

app.mainloop()