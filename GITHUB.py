from tkinter import *
import tkinter.messagebox as tkMessageBox
import sqlite3

root = Tk()
root.title("Movie Recommendation System")
 
width = 640
height = 480
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)


#=======================================VARIABLES=====================================
USERNAME = StringVar()
PASSWORD = StringVar()
FIRSTNAME = StringVar()
LASTNAME = StringVar()

#=======================================METHODS=======================================
def Database():
    global conn, cursor
    conn = sqlite3.connect("db_member.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, password TEXT, firstname TEXT, lastname TEXT)")


def Exit():
    result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


def LoginForm():
    global LoginFrame, lbl_result1
    LoginFrame = Frame(root)
    LoginFrame.pack(side=TOP, pady=80)
    lbl_username = Label(LoginFrame, text="Username:", font=('arial', 25), bd=18)
    lbl_username.grid(row=1)
    lbl_password = Label(LoginFrame, text="Password:", font=('arial', 25), bd=18)
    lbl_password.grid(row=2)
    lbl_result1 = Label(LoginFrame, text="", font=('arial', 18))
    lbl_result1.grid(row=3, columnspan=2)
    username = Entry(LoginFrame, font=('arial', 20), textvariable=USERNAME, width=15)
    username.grid(row=1, column=1)
    password = Entry(LoginFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=2, column=1)
    btn_login = Button(LoginFrame, text="Login", font=('arial', 18), width=35, command=Login)
    btn_login.grid(row=4, columnspan=2, pady=20)
    lbl_register = Label(LoginFrame, text="Register", fg="Blue", font=('arial', 12))
    lbl_register.grid(row=0, sticky=W)
    lbl_register.bind('<Button-1>', ToggleToRegister)

def RegisterForm():
    global RegisterFrame, lbl_result2
    RegisterFrame = Frame(root)
    RegisterFrame.pack(side=TOP, pady=40)
    lbl_username = Label(RegisterFrame, text="Username:", font=('arial', 18), bd=18)
    lbl_username.grid(row=1)
    lbl_password = Label(RegisterFrame, text="Password:", font=('arial', 18), bd=18)
    lbl_password.grid(row=2)
    lbl_firstname = Label(RegisterFrame, text="Firstname:", font=('arial', 18), bd=18)
    lbl_firstname.grid(row=3)
    lbl_lastname = Label(RegisterFrame, text="Lastname:", font=('arial', 18), bd=18)
    lbl_lastname.grid(row=4)
    lbl_result2 = Label(RegisterFrame, text="", font=('arial', 18))
    lbl_result2.grid(row=5, columnspan=2)
    username = Entry(RegisterFrame, font=('arial', 20), textvariable=USERNAME, width=15)
    username.grid(row=1, column=1)
    password = Entry(RegisterFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
    password.grid(row=2, column=1)
    firstname = Entry(RegisterFrame, font=('arial', 20), textvariable=FIRSTNAME, width=15)
    firstname.grid(row=3, column=1)
    lastname = Entry(RegisterFrame, font=('arial', 20), textvariable=LASTNAME, width=15)
    lastname.grid(row=4, column=1)
    btn_login = Button(RegisterFrame, text="Register", font=('arial', 18), width=35, command=Register)
    btn_login.grid(row=6, columnspan=2, pady=20)
    lbl_login = Label(RegisterFrame, text="Login", fg="Blue", font=('arial', 12))
    lbl_login.grid(row=0, sticky=W)
    lbl_login.bind('<Button-1>', ToggleToLogin)

def ToggleToLogin(event=None):
    RegisterFrame.destroy()
    LoginForm()

def ToggleToRegister(event=None):
    LoginFrame.destroy()
    RegisterForm()

def Register():
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "" or FIRSTNAME.get() == "" or LASTNAME.get == "":
        lbl_result2.config(text="Please complete the required field!", fg="orange")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ?", (USERNAME.get(),))
        if cursor.fetchone() is not None:
            lbl_result2.config(text="Username is already taken", fg="red")
        else:
            cursor.execute("INSERT INTO `member` (username, password, firstname, lastname) VALUES(?, ?, ?, ?)", (str(USERNAME.get()), str(PASSWORD.get()), str(FIRSTNAME.get()), str(LASTNAME.get())))
            conn.commit()
            USERNAME.set("")
            PASSWORD.set("")
            FIRSTNAME.set("")
            LASTNAME.set("")
            lbl_result2.config(text="Successfully Created!", fg="black")
        cursor.close()
        conn.close()
def Login():
    Database()
    if USERNAME.get == "" or PASSWORD.get() == "":
        lbl_result1.config(text="Please complete the required field!", fg="orange")
    else:
        cursor.execute("SELECT * FROM `member` WHERE `username` = ? and `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            lbl_result1.config(text="You Successfully Login", fg="blue")
        else:
            lbl_result1.config(text="Invalid Username or password", fg="red")
LoginForm()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)


if __name__ == '__main__':
    root.mainloop()


   second page:
       from tkinter import *
import sqlite3
main_screen = Tk()
main_screen.geometry("300x250")
main_screen.title("Movie Recommentation System")

    
 
# Set text variables
Passenger= StringVar()
Survived = StringVar()
Pclass=StringVar()
Name=StringVar()

Sex= StringVar()
Age = StringVar()
SibSP=StringVar()
Parch=StringVar()

Ticket= StringVar()
Fare = StringVar()
Cabin=StringVar()
Embarked=StringVar()

def database():
   Passengerid=Passenger.get()
   Survivedid=Survived.get()
   Pclassid=Pclass.get()
   Nameid=Name.get()
   
   Sexid=Sex.get()
   Ageid=Age.get()
   SibSPid=SibSP.get()
   Parchid=Parch.get()

   Ticketid=Ticket.get()
   Fareid=Fare.get()
   Cabinid=Cabin.get()
   Embarkedid=Embarked.get()
   
   conn = sqlite3.connect('predict.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS predict (Passenger TEXT,Survived TEXT,Pclass TEXT,Name TEXT,Sex TEXT,Age TEXT,SibSP TEXT,Parch TEXT,Ticket TEXT,Fare TEXT,Cabin TEXT,Embarked TEXT)')
   cursor.execute('INSERT INTO  predict(Passenger,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',(Passengerid,Survivedid,Pclassid,Nameid,Sexid,Ageid,SibSPid,Parchid,Ticketid,Fareid,Cabinid,Embarkedid,))
   conn.commit()
 
# Set label for user's instruction
Label(main_screen, text="Please enter details below", bg="orange").pack()
Label(main_screen, text="").pack()
    
# Set username label
Passengerid_lable = Label(main_screen, text="Passenger")
Passengerid_lable.pack()
 
# Set username entry
# The Entry widget is a standard Tkinter widget used to enter or display a single line of text.

    
Passengerid_entry = Entry(main_screen, textvariable=Passenger)
Passengerid_entry.pack()
   
# Set password label
Survivedid_lable = Label(main_screen, text="Survived  ")
Survivedid_lable.pack()

Survivedid_entry = Entry(main_screen, textvariable=Survived)
Survivedid_entry.pack()

Pclassid_lable = Label(main_screen, text="Pclass  ")
Pclassid_lable.pack()

Pclassid_entry = Entry(main_screen, textvariable=Pclass)
Pclassid_entry.pack()


Nameid_lable = Label(main_screen, text="Name  ")
Nameid_lable.pack()

Nameid_entry = Entry(main_screen, textvariable=Name)
Nameid_entry.pack()




Sexid_lable = Label(main_screen, text="Sex")
Sexid_lable.pack()
Sexid_entry = Entry(main_screen, textvariable= Sex)
Sexid_entry.pack()

Ageid_lable = Label(main_screen, text="Age")
Ageid_lable.pack()
Ageid_entry = Entry(main_screen, textvariable= Age)
Ageid_entry.pack()




SibSPid_lable = Label(main_screen, text="SibSP ")
SibSPid_lable.pack()

SibSPid_entry = Entry(main_screen, textvariable=SibSP)
SibSPid_entry.pack()


Parchid_lable = Label(main_screen, text="Parch")
Parchid_lable.pack()

Parchid_entry = Entry(main_screen, textvariable=Parch)
Parchid_entry.pack()


Ticketid_lable = Label(main_screen, text="Ticket")
Ticketid_lable.pack()
Ticektid_entry = Entry(main_screen, textvariable= Ticket)
Ticektid_entry.pack()

Fareid_lable = Label(main_screen, text="Fare")
Fareid_lable.pack()
Fareid_entry = Entry(main_screen, textvariable= Fare)
Fareid_entry.pack()

Cabinid_lable = Label(main_screen, text="Cabin")
Cabinid_lable.pack()
Cabinid_entry = Entry(main_screen, textvariable= Cabin)
Cabinid_entry.pack()

Embarkedid_lable = Label(main_screen, text="Embarked")
Embarkedid_lable.pack()
Embarkedid_entry = Entry(main_screen, textvariable= Embarked)
Embarkedid_entry.pack()


    
Label(main_screen, text="").pack()
# Set register button
Button(main_screen, text="Submit", width=10, height=1, bg="blue",command=database).pack()


main_screen.mainloop()

Algorithm:
    def findWaitingTime(processes, n, wt):  
    wt[0] = 0
   
    for i in range(1, n):  
        wt[i] = processes[i - 1][1] + wt[i - 1]  
  
# Function to calculate turn around time  
def findTurnAroundTime(processes, n, wt, tat):  
      
    # Calculating turnaround time by 
    # adding bt[i] + wt[i]  
    for i in range(n): 
        tat[i] = processes[i][1] + wt[i]  
  
# Function to calculate average waiting  
# and turn-around times.  
def findavgTime(processes, n):  
    wt = [0] * n 
    tat = [0] * n  
  
    # Function to find waiting time  
    # of all processes  
    findWaitingTime(processes, n, wt)  
  
    # Function to find turn around time 
    # for all processes  
    findTurnAroundTime(processes, n, wt, tat)  
  
    # Display processes along with all details  
    print("\nProcesses    Burst Time    Waiting",  
          "Time    Turn-Around Time") 
    total_wt = 0
    total_tat = 0
    for i in range(n): 
  
        total_wt = total_wt + wt[i]  
        total_tat = total_tat + tat[i]  
        print(" ", processes[i][0], "\t\t",  
                   processes[i][1], "\t\t",  
                   wt[i], "\t\t", tat[i]) 
  
    print("\nAverage waiting time = %.5f "%(total_wt /n)) 
    print("Average turn around time = ", total_tat / n)  
  
def priorityScheduling(proc, n): 
      
    # Sort processes by priority  
    proc = sorted(proc, key = lambda proc:proc[2],  
                                  reverse = True);  
  
    print("Order in which processes gets executed") 
    for i in proc: 
        print(i[0], end = " ") 
    findavgTime(proc, n)  
      
# Driver code  
if __name__ =="__main__": 
      
    # Process id's  
    proc = [[1, 10, 1],  
            [2, 5, 0],  
            [3, 8, 1]] 
    n = 3
    priorityScheduling(proc, n) 
      

