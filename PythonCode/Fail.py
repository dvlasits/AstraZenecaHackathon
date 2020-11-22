from tkinter import *
from PIL import ImageTk, Image
from Person import Person

a = [Person("Daniel", "123"), Person("Hari", "456"), Person("Kirpal", "190"), Person("Tommy", 45)]

class StartPage(frame):

def hello():
    global a
    global frame
    for p in a:
        if entry.get() == p.name and entry2.get() == p.password:
            global User
            User = p
            frame.forgetGrid()


def on_entry_click2(event):
    if entry2.get() == 'Enter your password...':
        entry2.delete(0, "end")  # delete all the text in the entry
        entry2.insert(0, '')  # Insert blank for user input
        entry2.config(fg='black')


def on_focusout2(event):
    if entry2.get() == '':
        entry2.insert(0, 'Enter your username...')
        entry2.config(fg='grey')


def on_entry_click(event):
    if entry.get() == 'Enter your user name...':
        entry.delete(0, "end")  # delete all the text in the entry
        entry.insert(0, '')  # Insert blank for user input
        entry.config(fg='black')


def on_focusout(event):
    if entry.get() == '':
        entry.insert(0, 'Enter your username...')
        entry.config(fg='grey')


root = Tk()

root.title("AstraZeneca")
root.geometry("500x700")
root.iconbitmap("favicon.ico")

frame = LabelFrame(root, text="This is my Frame...", padx=500,pady=600).grid(row=0,column=0)


my_img = ImageTk.PhotoImage(Image.open("SaveThePlanet.jpg"))
img_label = Label(frame,image=my_img).grid(row=4, column=0)



myLabel = Label(frame, text="Enter your name and password").grid(row=0, column=0)

entry = Entry(frame, bd=1)
entry.insert(0, 'Enter your user name...')
entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_focusout)
entry.config(fg='grey')
entry.grid(row=1, column=0)

entry2 = Entry(frame, bd=1)
entry2.insert(0, 'Enter your password...')
entry2.bind('<FocusIn>', on_entry_click2)
entry2.bind('<FocusOut>', on_focusout2)
entry2.config(fg='grey')
entry2.grid(row=2, column=0)

myButton = Button(frame, text="Submit", command=hello, pady=50, fg="white", bg="green", width=15, height=1).grid(row=3,column=0)

root.mainloop()
