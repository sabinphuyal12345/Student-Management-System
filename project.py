from tkinter import *
from tkinter import messagebox
project = Tk()

def handle():
    f = open("student_data/id.txt","w")
    a = f.write("sabinphuyalnami@gmail.com")
    a = f.close()

handle()

def handle_ii():
    r = open("student_data/password.txt","w")
    r.write("sabinpss")
    r.close()

handle_ii()

def trigger():

    f1 = form.get()
    f2 = form_ii.get()

    z1 = open("student_data/id.txt","r")
    save_id = z1.read().strip()
    z1.close()

    z2 = open("student_data/password.txt","r")
    save_pass = z2.read().strip()
    z2.close()

    if(f1 == save_id and f2 == save_pass):
        messagebox.showinfo("Your Data is Correct")
        new_window()
        
    else:
        messagebox.showerror("Your Data is Inorrect")

def new_window():
    win = Toplevel()
    win.minsize(300,200)
    win.maxsize(300,200)
    win.configure(background="black")

    btn_ii = Button(win,width="8",height="2",text="ECA",fg="black",bg="white",command=trigger_eca)
    btn_ii.pack(pady=10)

    btn_iii = Button(win,width="8",height="2",text="Grades",fg="black",bg="white",command=trigger_grades)
    btn_iii.pack(pady=10)

def trigger_eca():
    eca = Toplevel()
    eca.minsize(300,200)
    eca.maxsize(300,200)
    eca.configure(background="black")

    eca_data = open("student_data/eca.txt","r")
    std_eca = eca_data.read()
    eca_data.close()

    head_i = Label(eca,text = std_eca,fg = "white",bg="black")
    head_i.config(font=("cursive",10))
    head_i.pack(pady=10)

def trigger_grades():
    grades = Toplevel()
    grades.minsize(300,200)
    grades.maxsize(300,200)
    grades.configure(background="black")

    grades_data = open("student_data/grades.txt","r")
    grades_eca = grades_data.read()
    grades_data.close()

    head_ii = Label(grades,text = grades_eca,fg = "white",bg="black")
    head_ii.config(font=("cursive",10))
    head_ii.pack(pady=10)

project.title("Student")
project.minsize(800,600)
project.maxsize(800,600)
project.configure(background="black")

head = Label(project,text = "Student Login System",fg = "white",bg="black")
head.config(font=("cursive",30))
head.pack(pady=40)

head_ii = Label(project,text = "Enter User Name",fg = "white",bg="black")
head_ii.config(font=("cursive",15))
head_ii.pack(pady=1)

form = Entry(project,width = 30)
form.pack(pady=20)

head_iii = Label(project,text = "Enter User Password",fg = "white",bg="black")
head_iii.config(font=("cursive",15))
head_iii.pack(pady=30)

form_ii = Entry(project,width = 30)
form_ii.pack(pady=0)

btn = Button(project,width="8",height="2",text="Submit",fg="black",bg="white",command=trigger)
btn.pack(pady=50)

project.mainloop()

