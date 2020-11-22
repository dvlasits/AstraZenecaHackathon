import tkinter as tk
from tkinter import *
from Person import Person
from PIL import ImageTk, Image
import SSH
import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy

LARGE_FONT = ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.container = tk.Frame(self)

        self.container.pack(side="top", fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            frame = F(self.container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont,override = False):
        if override:
            frame = cont(self.container,self)
            frame.grid(row=0, column=0, sticky="nsew")
            frame.update2()
            frame.tkraise()
        else:

            frame = self.frames[cont]
            frame.update2()
            frame.tkraise()


global User

class PageTwo(tk.Frame):

    def on_entry_click3(self, event):
        if self.entry3.get() == 'How much to withdraw':
            self.entry3.delete(0, "end")  # delete all the text in the entry
            self.entry3.insert(0, '')  # Insert blank for user input
            self.entry3.config(fg='black')

    def on_focusout3(self, event):
        if self.entry3.get() == '':
            self, self.entry3.insert(0, 'How much to withdraw')
            self, self.entry3.config(fg='grey')

    def withdraw(self):
        self.label2.config(text="There is currently £" + str(sum([k.PersonSaved() for k in a]) - int(self.entry3.get())) + " in the funds")
        tk.messagebox.showinfo("Withdrawn Money", "Make sure your colleagues put in what they got from this money for the cycle to continue!!!!!")


    def update2(self):
        self.label.config(font=("Courier", 20), text="Welcome Admin " + User.name)
        self.configure(background="light green")
        self.label2 = self.label = tk.Label(self, text="There is currently £" + str(sum([k.PersonSaved() for k in a])) + " in the funds", font=LARGE_FONT)
        self.label2.pack(pady=5)

        self.entry3 = Entry(self, bd=1, width=30)
        self.entry3.insert(0, 'How much to withdraw')
        self.entry3.bind('<FocusIn>', self.on_entry_click3)
        self.entry3.bind('<FocusOut>', self.on_focusout3)
        self.entry3.pack(pady=5)

        self.button1 = tk.Button(self, text="Withdraw!!!!",
                                 command=self.withdraw)
        self.button1.pack()

        self.button1 = tk.Button(self, text="Back to Home",
                                 command=lambda: self.controller.show_frame(StartPage, True))
        self.button1.pack()

        self.my_img = ImageTk.PhotoImage(Image.open("SaveThePlanet.jpg"))
        img_label = Label(self, image=self.my_img).pack(pady=5)



    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self, text="Welcome Admin", font=LARGE_FONT)
        self.label.pack(pady=10, padx=10)




class PageOne(tk.Frame):

    def update2(self):
        global User
        global a
        a = sorted(a, key=lambda person: person.PersonSaved())
        self.label.config(font=("Courier", 20), text="Welcome " + User.name)

        if User.name == a[-1].name:
            self.label2.config(font=("Courier", 20), text="Your winning!!!! Keep up the great work")
        else:
            for index,item in enumerate(a):
                if item == User:
                    self.label2.config(font=("Courier", 20),
                                       text=(a[index+1].name + " is beating you by " + str(a[index+1].PersonSaved()-a[index].PersonSaved()) + " you got this!!!"))

        self.f = Figure(figsize=(5, 4), dpi=100)

        self.ax = self.f.add_subplot(111)
        self.ax.clear()

        totals = [k.PersonSaved() for k in a]

        data1 = tuple([k.PersonSaved() for k in a])
        data2 = ([k.PersonSaved() - k.savedCarbon["Heating"] for k in a])
        data3 = ([k.PersonSaved() - k.savedCarbon["Heating"] - k.savedCarbon["Cups"] for k in a])
        data4 = ([k.PersonSaved() - k.savedCarbon["Heating"] - k.savedCarbon["Cups"] - k.savedCarbon["Bike"] for k in a])

        ind = numpy.array([k.name for k in a])  # the x locations for the groups
        width = .5

        rects1 = self.ax.barh(ind, data1, width, label="Heating")
        self.ax.barh(ind, data2, width, label="Cups")
        self.ax.barh(ind, data3, width, label="Bike")
        self.ax.barh(ind, data4, width, label="Trees")
        self.ax.legend()


        self.done = 1
        self.canvas = FigureCanvasTkAgg(self.f, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    def help(self):

        global a
        for item in a:
            if item == User:
                item.savedCarbon[self.entry3.get()] += int(self.entry4.get())
        SSH.OnlineInterface().putData(a)
        print(a)
        self.controller.show_frame(PageOne,True)

    def on_entry_click3(self, event):
        if self.entry3.get() == 'What have you done':
            self.entry3.delete(0, "end")  # delete all the text in the entry
            self.entry3.insert(0, '')  # Insert blank for user input
            self.entry3.config(fg='black')

    def on_focusout3(self, event):
        if self.entry3.get() == '':
            self, self.entry3.insert(0, 'What have you done')
            self, self.entry3.config(fg='grey')

    def on_entry_click4(self, event):
        if self.entry4.get() == 'How much have you done':
            self.entry4.delete(0, "end")  # delete all the text in the entry
            self.entry4.insert(0, '')  # Insert blank for user input
            self.entry4.config(fg='black')

    def on_focusout4(self,event):
        if self.entry4.get() == '':
            self.entry4.insert(0, 'How much have you done')
            self.entry4.config(fg='grey')

    def __init__(self, parent, controller):
        self.done = 0
        tk.Frame.__init__(self, parent)
        global User
        self.configure(background="light green")
        self.label = tk.Label(self, text="Welcome ", font=LARGE_FONT)
        self.label.pack(pady=10, padx=10)
        self.label2 = tk.Label(self, text="Welcome ", font=LARGE_FONT)
        self.label2.pack(pady=10, padx=10)
        self.controller = controller

        self.button1 = Button(self, text="Back to Home",
                                 command=lambda: controller.show_frame(StartPage, True))


        self.entry3 = Entry(self, bd=1, width=30)
        self.entry3.insert(0, 'What have you done')
        self.entry3.bind('<FocusIn>', self.on_entry_click3)
        self.entry3.bind('<FocusOut>', self.on_focusout3)
        self.entry3.pack(pady=5)
        self.entry4 = Entry(self, bd=1, width=30)
        self.entry4.insert(0, 'How much have you done')
        self.entry4.bind('<FocusIn>', self.on_entry_click4)
        self.entry4.bind('<FocusOut>', self.on_focusout4)
        self.entry4.pack(pady=5)
        self.button2 = Button(self, text="Enter Info", command=self.help, pady=1, fg="white", bg="green", width=15,
                          height=0).pack(pady=5)

        self.button1.pack()



class StartPage(tk.Frame):

    def update2(self):
        pass


    def hello(self):
        global a
        correct = 0
        a = SSH.OnlineInterface().getData()
        for p in a:
            if self.entry.get() == p.name and self.entry2.get() == p.password:
                global User
                User = p
                correct = 1
                if not p.admin:
                    self.controller.show_frame(PageOne, True)
                else:
                    self.controller.show_frame(PageTwo, True)
        if correct == 0:
            tk.messagebox.showinfo("Error", "Incorrect username or password, please try again")

    def on_entry_click2(self, event):
        if self.entry2.get() == 'Enter your password...':
            self.entry2.delete(0, "end")  # delete all the text in the entry
            self.entry2.insert(0, '')  # Insert blank for user input
            self.entry2.config(fg='black')

    def on_focusout2(self, event):
        if self.entry2.get() == '':
            self, self.entry2.insert(0, 'Enter your username...')
            self, self.entry2.config(fg='grey')

    def on_entry_click(self, event):
        if self.entry.get() == 'Enter your user name...':
            self.entry.delete(0, "end")  # delete all the text in the entry
            self.entry.insert(0, '')  # Insert blank for user input
            self.entry.config(fg='black')

    def on_focusout(self,event):
        if self.entry.get() == '':
            self.entry.insert(0, 'Enter your username...')
            self.entry.config(fg='grey')

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)

        self.configure(background="light green")
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        myLabel = Label(self, text="Enter your name and password", font=("Courier", 20)).grid(row=0, column=0, pady=5)

        self.entry = Entry(self, bd=1, width=30)
        self.entry.insert(0, 'Enter your user name...')
        self.entry.bind('<FocusIn>', self.on_entry_click)
        self.entry.bind('<FocusOut>', self.on_focusout)
        self.entry.config(fg='grey')
        self.entry.grid(row=1, column=0, pady=5)
        self.entry2 = Entry(self, bd=1, show="*", width=30)
        self.entry2.insert(0, 'Enter your password...')
        self.entry2.bind('<FocusIn>', self.on_entry_click2)
        self.entry2.bind('<FocusOut>', self.on_focusout2)
        self.entry2.config(fg='grey')
        self.entry2.grid(row=2, column=0, pady=5)
        myButton = Button(self, text="Submit", command=self.hello, pady=1, fg="white", bg="green", width=15,
                          height=0).grid(row=3, column=0, pady=5)
        self.my_img = ImageTk.PhotoImage(Image.open("SaveThePlanet.jpg"))
        img_label = Label(self, image=self.my_img).grid(row=5, column=0)

        '''
        button = tk.Button(self, text="Visit Page 1",
                           command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = tk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()'''




app = SeaofBTCapp()
app.iconbitmap("favicon.ico")
app.title("AstraZeneca Sustainability Project")
app.mainloop()
