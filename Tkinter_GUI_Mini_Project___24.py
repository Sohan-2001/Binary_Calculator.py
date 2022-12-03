from tkinter import * #to import tkinter
from tkinter import ttk #style the tkinter widgets just like CSS does in HTML
from tkinter.messagebox import showinfo #to import messagebox
from tkinter import Menu #to import menu
from PIL import Image, ImageTk #for image
import time #for time
import webbrowser #for opening website
import os #for accessing device file, interacting with the operating system
from tkinter import filedialog #for accessing file directory


url="https://wa.me/916265619188?text=I%20need%20help%20regarding%20the%20Binary%20Calculator"
ws = Tk()
ws.state('zoomed')
ws.config(bg='#0f4b6e')

def dark_theme():
    ws.config(bg='black')
    binary_calculator.config(bg='black',fg='white')
    num1_lbl.config(bg='black',fg='white')
    num2_lbl.config(bg='black',fg='white')
    label1.config(bg='black')
    

def normal_theme():
    ws.config(bg='#0f4b6e')
    binary_calculator.config(bg='#0f4b6e',fg='white')
    num1_lbl.config(bg='#0f4b6e',fg='white')
    num2_lbl.config(bg='#0f4b6e',fg='white')
    label1.config(bg='#0f4b6e')

def need_help():
    webbrowser.open(url)

btn_dark=Button(ws,
                text='Dark Mode',
                font=("Arial",10),
                command=dark_theme,
                borderwidth = 5
                ).place(relx=0,rely=0)

btn_Help=Button(ws,
                text='Need Help',
                font=("Arial",10),
                command=need_help,
                borderwidth = 5
                ).place(relx=0.95,rely=0)
                

btn_normal=Button(ws,
                text='Normal Mode',
                font=("Arial",10),
                command=normal_theme,
                borderwidth = 5
                ).place(relx=0.053,rely=0)


image = Image.open("C:\\Users\\sohan\\Downloads\\Binary.png")
resize_image = image.resize((80, 80))
img = ImageTk.PhotoImage(resize_image)
label1 = Label(image=img,bg='#0f4b6e')
label1.image = img
label1.place(x=260,y=10)


def about():
    sk=Toplevel(ws) #Topelevel to import functions from the main window
    
    sk.state('zoomed')
    image = Image.open("C:\\Users\\sohan\\Downloads\\Sohan.JPEG")
    resize_image = image.resize((70, 90))
    img = ImageTk.PhotoImage(resize_image)
    label10 = Label(sk,image=img)
    label10.image = img
    label10.place(x=610,y=570)
    ##
    image = Image.open("C:\\Users\\sohan\\Downloads\\Shivesh.jpg")
    resize_image = image.resize((70, 90))
    img = ImageTk.PhotoImage(resize_image)
    label11 = Label(sk,image=img)
    label11.image = img
    label11.place(x=610,y=690)
    ##
    image = Image.open("C:\\Users\\sohan\\Downloads\\Asish.png")
    resize_image = image.resize((70, 90))
    img = ImageTk.PhotoImage(resize_image)
    label12 = Label(sk,image=img)
    label12.image = img
    label12.place(x=610,y=460)
    sk.config(bg='#050A30')
    l1=Label(sk,text='It is a free-to-use bitwise operation Graphical User Interface\n',font=('',15),bg='#050A30',fg='white').place(x=0,y=50)
    l1=Label(sk,text='Instructions',font=('bold',20),bg='#050A30',fg='white').place(x=0,y=100)
    l1=Label(sk,text='1. Here are two input bars to take input of two decimal numbers',font=('',15),bg='#050A30',fg='white').place(x=0,y=140)
    l1=Label(sk,text='2. Four buttons named AND, OR, XOR, NOT',font=('',15),bg='#050A30',fg='white').place(x=0,y=170)
    l1=Label(sk,text='3. Each button performs the respective biwise function on the two numbers given by the user',font=('',15),bg='#050A30',fg='white').place(x=0,y=200)
    l1=Label(sk,text='4. The result is shown in the display bar',font=('',15),bg='#050A30',fg='white').place(x=0,y=230)
    l1=Label(sk,text='5. Another button EXPLAIN opens a new window with the explanation of the bitwise operation',font=('',15),bg='#050A30',fg='white').place(x=0,y=260)
    l1=Label(sk,text='About the last Update',font=('bold',20),bg='#050A30',fg='white').place(x=0,y=310)
    l1=Label(sk,text='The last update added the most awaited Dark Theme',font=('',15),bg='#050A30',fg='white').place(x=0,y=350)
    l1=Label(sk,text='Developers & Members',font=('bold',20),bg='#050A30',fg='white').place(x=0,y=410)
    l1=Label(sk,text='Role',font=('bold',20),bg='#050A30',fg='white').place(x=1200,y=410)
    l1=Label(sk,text='Profile',font=('bold',20),bg='#050A30',fg='white').place(x=600,y=410) # Profile
    l1=Label(sk,text='1. Ashis',font=('',15),bg='#050A30',fg='white').place(x=0,y=460) # Ashish
    l1=Label(sk,text='1. Coding of the Dark Theme',font=('',15),bg='#050A30',fg='white').place(x=1200,y=460)
    l1=Label(sk,text='2. Designing of the about Page',font=('',15),bg='#050A30',fg='white').place(x=1200,y=490)
    l1=Label(sk,text='2. Sohan Karfa',font=('',15),bg='#050A30',fg='white').place(x=0,y=600) # Sohan Karfa
    l1=Label(sk,text='1. Coding of the main frame',font=('',15),bg='#050A30',fg='white').place(x=1200,y=600)
    l1=Label(sk,text='3. Shivesh Singh',font=('',15),bg='#050A30',fg='white').place(x=0,y=710) # Shivesh Singh
    l1=Label(sk,text='1. Designing',font=('',15),bg='#050A30',fg='white').place(x=1200,y=710)
    l1=Label(sk,text='2. Coding of Fullscreen, Need Help',font=('',15),bg='#050A30',fg='white').place(x=1200,y=740)
        

def CheckUpdate():
    gui=Toplevel(ws)
    gui.geometry('500x100')
    gui.config(bg='#003100')
    
    def StartProgress():
        start_btn.destroy()
        label2=Label(gui,
                     text='Checking...',
                     bg='#003100',
                     fg='white',
                     font=('Lucida Console',18))
        label2.place(x=150,y=50)
        for i in range(5):
            progress_var['value'] += 20
            stringvar.set(progress_var['value'])
            # get the value
            label.config(text=stringvar.get()+' %')
            # update value
            gui.update_idletasks()
            time.sleep(1)
        
        progress_var.destroy()
        label.destroy()
        label1=Label(gui,
                     text='You are Up-To-Date',
                     bg='#003100',
                     fg='white',
                     font=("Times New Roman",30)).place(x=65,y=25)
        
        label2.destroy()
    
        

    progress_var=ttk.Progressbar(gui,orient=HORIZONTAL,length=400,mode='determinate')
    progress_var.place(x=10,y=20)
    start_btn=Button(gui,text='Check',command=StartProgress)
    start_btn.place(x=200,y=50)
    # string variable
    stringvar=StringVar()
    stringvar.set('00.0 %')
    label=Label(gui,text=stringvar.get(),font=('',12),bg='#003100',fg='white')
    label.place(x=430,y=25)

menu=Menu(ws)
ws.config(menu=menu)
filemenu=Menu(menu,tearoff="off")
menu.add_cascade(label='File', menu=filemenu,font=("",20))
filemenu.add_command(label='About',font=("",10),command=about)
filemenu.add_command(label='Update',font=("",10),command=CheckUpdate)

def normalscreen():
    ws.attributes('-fullscreen',False)
    ws.state('zoomed')

def fullscreen():
    ws.attributes('-fullscreen',True)


btn_fullscreen=Button(ws,
                      text='Full Screen',
                      font=('Arial',10),
                      command=fullscreen,
                      borderwidth=5
                      ).place(relx=0,rely=0.955)

btn_normalscreen=Button(ws,
                        text='Normal Screen',
                        font=('Arial',10),
                        command=normalscreen,
                        borderwidth=5
                        ).place(relx=0.055,rely=0.955)

def AND_OPERATION():
    num1 = int(num1_tf.get())
    num2 = int(num2_tf.get())
    ADD=num1&num2
    disp_tf.configure(state='normal')
    disp_tf.delete(0,END)
    disp_tf.insert(0,f'The AND is {ADD}')
    disp_tf.configure(state='disabled')
    btn01=Button(
            ws,
            text='E X P L A I N',
            font=(20),
            borderwidth = 10,
            bg='#99ccff',
            fg='#001a33',
            activebackground='yellow',
            command=open_new1
            )

    btn01.place(relx=0.45, rely=0.8)
    
    

def OR_OPERATION():
    num1 = int(num1_tf.get())
    num2 = int(num2_tf.get())
    OR=num1|num2
    disp_tf.configure(state='normal')
    disp_tf.delete(0,END)
    disp_tf.insert(0,f'The OR is {OR}')
    disp_tf.configure(state='disabled')
    btn02=Button(
            ws,
            text='E X P L A I N',
            font=(20),
            borderwidth = 10,
            bg='#99ccff',
            fg='#001a33',
            activebackground='yellow',
            command=open_new2
            )

    btn02.place(relx=0.45, rely=0.8)
    

def XOR_OPERATION():
    num1 = int(num1_tf.get())
    num2 = int(num2_tf.get())
    X_O_R=num1^num2
    disp_tf.configure(state='normal')
    disp_tf.delete(0,END)
    disp_tf.insert(0,f'The XOR is {X_O_R}')
    disp_tf.configure(state='disabled')
    btn03=Button(
            ws,
            text='E X P L A I N',
            font=(20),
            borderwidth = 10,
            bg='#99ccff',
            fg='#001a33',
            activebackground='yellow',
            command=open_new3
            )

    btn03.place(relx=0.45, rely=0.8)

def NOT_OPERATION():
    num1 = int(num1_tf.get())
    num2 = int(num2_tf.get())
    N_O_T_num1=~num1
    N_O_T_num2=~num2
    disp_tf.configure(state='normal')
    disp_tf.delete(0,END)
    disp_tf.insert(0,f'The NOT of the first number is {N_O_T_num1} and NOT of second number is {N_O_T_num2}')
    disp_tf.configure(state='disabled')
    btn03=Button(
            ws,
            text='E X P L A I N',
            font=(20),
            borderwidth = 10,
            bg='#99ccff',
            fg='#001a33',
            activebackground='yellow',
            command=open_new4
            )

    btn03.place(relx=0.45, rely=0.8)



ws.title('Binary Calculator')

binary_calculator=Label(ws,text="BINARY CALCULATOR",
      font=("Segoe Script",50),
      bg='#0f4b6e',
      fg='white'
      )
binary_calculator.pack()

num1_tf = Entry(
    ws,
    width=20,
    font=("Helvetica",20)
    )

num1_tf.insert=(0, "Type")
num2_tf = Entry(
    ws,
    width=20,
    font=("Helvetica",20)
    )

num1_lbl = Label(
    ws,
    text='First number',
    bg='#0f4b6e',
    fg='white',
    font=("Helvetica",20)
)
num2_lbl = Label(
    ws,
    text='Second number',
    bg='#0f4b6e',
    fg='white',
    font=("Helvetica",20)
)

num1_lbl.place(relx=0.05, rely=0.2)
num1_tf.place(relx=0.16, rely=0.2)
num2_lbl.place(relx=0.52, rely=0.2)
num2_tf.place(relx=0.66, rely=0.2)




btn1=Button(ws, text='A N D',
           font=("Castellar",20,'bold'),
           borderwidth = 10,
           bg='#ffffcc',
           activebackground='yellow',
           command=AND_OPERATION
           )



btn1.place(relx=0.2, rely=0.4)

btn2=Button(ws, text='O R',
           font=("Castellar",20,'bold'),
           borderwidth = 10,
           bg='#ffffcc',
           activebackground='yellow',
           command=OR_OPERATION
           )



btn2.place(relx=0.4, rely=0.4)

btn3=Button(ws, text='X O R',
           font=("Castellar",20,'bold'),
           borderwidth = 10,
           bg='#ffffcc',
           activebackground='yellow',
           command=XOR_OPERATION)

btn3.place(relx=0.6, rely=0.4)

btn4=Button(ws, text='N O T',
           font=("Castellar",20,'bold'),
           borderwidth = 10,
           bg='#ffffcc',
           activebackground='yellow',
           command=NOT_OPERATION)

btn4.place(relx=0.8, rely=0.4)



disp_tf = Entry(
    ws, 
    width=100,
    justify='center',
    font=('Arial', 20)
    )

disp_tf.insert(0, 'Result appears here')
disp_tf.configure(state='disabled')

disp_tf.place(relx=0.01, rely=0.6)

def open_new1():
    new_win= Toplevel(ws)
    new_win.title("AND")
    
    x=int(num1_tf.get())
    y=int(num2_tf.get())
    a=bin(x)[2:]
    b=bin(y)[2:]
    C=x&y
    c=bin(C)[2:]
    d=int(c,2)
    
    
    new_win.config(bg='#050A30')
    Label1=Label(new_win, text="First decimal numeber : ",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=0, column=0)
    new_win.state('zoomed')
    Label1=Label(new_win, text=x,font=('Cascadia 20 bold'),bg='#050A30',fg='white').grid(row=0, column=1)
    Label1=Label(new_win, text="\n",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=1, column=1)
    Label1=Label(new_win, text="Its binary number : ",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=2, column=0)
    Label1=Label(new_win, text=a,font=('Cascadia 20 bold'),bg='#050A30',fg='white').grid(row=2, column=1)
    Label1=Label(new_win, text="\n",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=3, column=1)
    Label1=Label(new_win, text="Second decimal numeber : ",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=4, column=0)
    Label1=Label(new_win, text=y,font=('Cascadia 20 bold'),bg='#050A30',fg='white').grid(row=4, column=1)
    Label1=Label(new_win, text="\n",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=5, column=1)
    Label1=Label(new_win, text="Its binary number : ",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=6, column=0)
    Label1=Label(new_win, text=b,font=('Cascadia 20 bold'),bg='#050A30',fg='white').grid(row=6, column=1)
    Label1=Label(new_win, text="\n",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=7, column=1)
    Label1=Label(new_win, text="Their binary addition: ",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=8, column=0)
    Label1=Label(new_win, text=c,font=('Cascadia 20 bold'),bg='#050A30',fg='white').grid(row=8, column=1)
    Label1=Label(new_win, text="\n",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=9, column=1)
    Label1=Label(new_win, text="Its decimal number: ",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=10, column=0)
    Label1=Label(new_win, text=d,font=('Cascadia 20 bold'),bg='#050A30',fg='white').grid(row=10, column=1)
    

def open_new2():
    new_win= Toplevel(ws)
    new_win.config(bg='#050A30')
    new_win.title("OR")
    
    x=int(num1_tf.get())
    y=int(num2_tf.get())
    a=bin(x)[2:]
    b=bin(y)[2:]
    D=x|y
    c=bin(D)[2:]
    d=int(c,2)
    Label(new_win, text="First decimal numeber : ",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=0, column=0)
    new_win.state('zoomed')
    Label(new_win, text=x,font=('Cascadia 20 bold'),bg='#050A30',fg='white').grid(row=0, column=1)
    Label(new_win, text="\n",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=1, column=1)
    Label(new_win, text="Its binary number : ",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=2, column=0)
    Label(new_win, text=a,font=('Cascadia 20 bold'),bg='#050A30',fg='white').grid(row=2, column=1)
    Label(new_win, text="\n",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=3, column=1)
    Label(new_win, text="Second decimal numeber : ",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=4, column=0)
    Label(new_win, text=y,font=('Cascadia 20 bold'),bg='#050A30',fg='white').grid(row=4, column=1)
    Label(new_win, text="\n",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=5, column=1)
    Label(new_win, text="Its binary number : ",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=6, column=0)
    Label(new_win, text=b,font=('Cascadia 20 bold'),bg='#050A30',fg='white').grid(row=6, column=1)
    Label(new_win, text="\n",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=7, column=1)
    Label(new_win, text="Their binary OR: ",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=8, column=0)
    Label(new_win, text=c,font=('Cascadia 20 bold'),bg='#050A30',fg='white').grid(row=8, column=1)
    Label(new_win, text="\n",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=9, column=1)
    Label(new_win, text="Its decimal number: ",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=10, column=0)
    Label(new_win, text=d,font=('Cascadia 20 bold'),bg='#050A30',fg='white').grid(row=10, column=1)
 

def open_new3():
    new_win= Toplevel(ws)
    new_win.title("XOR")
    new_win.config(bg='#050A30')
    
    x=int(num1_tf.get())
    y=int(num2_tf.get())
    a=bin(x)[2:]
    b=bin(y)[2:]
    E=x^y
    c=bin(E)[2:]
    d=int(c,2)
    Label(new_win, text="First decimal numeber : ",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=0, column=0)
    new_win.state('zoomed')
    Label(new_win, text=x,font=('Cascadia 20 bold'),bg='#050A30',fg='white').grid(row=0, column=1)
    Label(new_win, text="\n",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=1, column=1)
    Label(new_win, text="Its binary number : ",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=2, column=0)
    Label(new_win, text=a,font=('Cascadia 20 bold'),bg='#050A30',fg='white').grid(row=2, column=1)
    Label(new_win, text="\n",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=3, column=1)
    Label(new_win, text="Second decimal numeber : ",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=4, column=0)
    Label(new_win, text=y,font=('Cascadia 20 bold'),bg='#050A30',fg='white').grid(row=4, column=1)
    Label(new_win, text="\n",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=5, column=1)
    Label(new_win, text="Its binary number : ",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=6, column=0)
    Label(new_win, text=b,font=('Cascadia 20 bold'),bg='#050A30',fg='white').grid(row=6, column=1)
    Label(new_win, text="\n",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=7, column=1)
    Label(new_win, text="Their binary XOR: ",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=8, column=0)
    Label(new_win, text=c,font=('Cascadia 20 bold'),bg='#050A30',fg='white').grid(row=8, column=1)
    Label(new_win, text="\n",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=9, column=1)
    Label(new_win, text="Its decimal number: ",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=10, column=0)
    Label(new_win, text=d,font=('Cascadia 20 bold'),bg='#050A30',fg='white').grid(row=10, column=1)


def open_new4():
    new_win= Toplevel(ws)
    new_win.title("NOT")
    new_win.config(bg='#050A30')
    
    x=int(num1_tf.get())
    y=int(num2_tf.get())
    F=~x
    G=~y
    Label(new_win, text="First decimal numeber : ",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=0, column=0)
    new_win.state('zoomed')
    Label(new_win, text=x,font=('Cascadia 20 bold'),bg='#050A30',fg='white').grid(row=0, column=1)
    Label(new_win, text="\n",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=1, column=1)
    Label(new_win, text="Its NOT : ",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=2, column=0)
    Label(new_win, text=F,font=('Cascadia 20 bold'),bg='#050A30',fg='white').grid(row=2, column=1)
    Label(new_win, text="\n",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=3, column=1)
    Label(new_win, text="Second decimal numeber : ",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=4, column=0)
    Label(new_win, text=y,font=('Cascadia 20 bold'),bg='#050A30',fg='white').grid(row=4, column=1)
    Label(new_win, text="\n",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=5, column=1)
    Label(new_win, text="Its NOT : ",font=('Georgia 20 bold'),bg='#050A30',fg='white').grid(row=6, column=0)
    Label(new_win, text=G,font=('Cascadia 20 bold'),bg='#050A30',fg='white').grid(row=6, column=1)
  
btn00=Button(
            ws,
            text='E X P L A I N',
            font=(20),
            borderwidth = 10,
            bg='#99ccff',
            fg='#001a33',
            activebackground='yellow'
            )

btn00.place(relx=0.45, rely=0.8)


ws.mainloop()



