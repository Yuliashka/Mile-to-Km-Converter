
import tkinter

# creating of a window:
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=500)
window.config(padx=30, pady=30)

# ENTRY:
entry = tkinter.Entry(width=7)
entry.insert(tkinter.END, string="0")
entry.grid(column=1, row=0)


# LABEL1:
label1 = tkinter.Label(text="Miles")
label1.grid(column=2, row=0)

# LABEL2:
label2 = tkinter.Label(text="is equal to:")
label2.grid(column=0, row=1)

# LABEL3:
label3 = tkinter.Label(text="0")
label3.grid(column=1, row=1)

# LABEL4:
label4 = tkinter.Label(text="Km")
label4.grid(column=2, row=1)


# FUNCTION FOR BUTTON:
def button_used():
    label3.config(text=f"{int(entry.get())*1.609}")
    print(type(entry.get()))
    print((int(entry.get())*1.609))


# BUTTON
button = tkinter.Button(text="Calculate", command=button_used)
button.grid(column=1, row=2)


# to keep our window open and to listen to users actions we need to use method:
window.mainloop()
