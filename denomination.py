from tkinter import *
from tkinter import messagebox

tk = Tk()
tk.geometry("800x800")
tk.title("Denomination Calculator")
tk.configure(bg= "light blue")

label1 = Label(tk, text="Do you want to try the denomination calculator.", bg = "light blue")

label1.place_configure(x=180,y=20)

def msg():
    msg_box = messagebox.showinfo("Alert","Do you want to use the denomination calculator")
    if msg_box == "ok":
        topwin()

btn = Button(text="Let's get started!",command= msg,bg="red",fg="white")
btn.place(x=260, y=360)

def topwin():
    top = Toplevel()
    top.configure(bg= "light grey")
    top.title("Denomination Calculator")
    top.geometry("600x350+50+50")

    lbl = Label(top,text="Enter Total Ammount:", bg= "light grey")
    entry = Entry(top)

    l1 = Label(top,text="1000:",bg= "red")
    l2 = Label(top,text="500:",bg="red")
    l3 = Label(top,text="100:",bg="red")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():
        try:
            ammount = int(entry.get())

            note1000 = ammount // 1000
            ammount %= 1000

            note500 = ammount // 500
            ammount %= 500

            note100 = ammount // 100
            ammount %= 100

            t1.delete(0, END)
            t2.delete(0,END)
            t3.delete(0,END)

            t1.insert(END, note1000)
            t2.insert(END, note500)
            t3.insert(END, note100)
        except ValueError:
            messagebox.showerror("Error","Please enter a valid number!")
    
    btn2 = Button(top, command=calculator, text="Calculate",fg="red",bg="black")

    label1.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn2.place(x=240, y=120)

    lbl.place(x=140, y=170)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)


    top.mainloop()

# -------------------------------
# Start Main Loop
# -------------------------------
tk.mainloop()

