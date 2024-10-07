from tkinter import *

window = Tk()
window.title("Login App")
window.geometry("400x400")

frame = Frame(window, bg="lightgreen", height=200, width=380)
label1 = Label(frame, text="Full name :", bg="darkgreen", fg="white", width=12)
label2 = Label(frame, text="Email ID :", bg="darkgreen", fg="white", width=12)
label3 = Label(frame, text="Password :", bg="darkgreen", fg="white", width=12)
name_entry = Entry(frame, width=15)
email_entry = Entry(frame, width=15)
password_entry = Entry(frame, width=15, show="*")
txt = Text(window, bg="grey35", fg="grey1")
def greetings():
    name = name_entry.get()
    str1 = f"Hey {name}\n"
    str2 = "Congratulations for creating your account!"
    txt.insert(END, str1)
    txt.insert(END, str2)
button = Button(window, text="Create account", command=greetings, bg="orange", fg="white", width=15)

frame.place(x=10, y=10)
label1.place(x=20, y=20)
name_entry.place(x=200, y=20)
label2.place(x=20, y=80)
email_entry.place(x=200, y=80)
label3.place(x=20, y=140)
password_entry.place(x=200, y=140)
button.place(x=170, y=210)
txt.place(y=250)

window.mainloop()