from tkinter import *
from tkinter import messagebox
import base64
import os
   
def encrypt():
    password=code.get()

    if password=="9876":
        screen1=Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ADD8E6")

        message=text1.get(1.0,END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")

        Label(screen1,text="ENCRYPT",font="timesnewroman",fg="black",bg="#87CEEB").place(x=10,y=0)
        text2=Text(screen1,font="robote 10",bg="#FFEBCD",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)

        text2.insert(END,encrypt)

    elif password !="":
        messagebox.showerror("encryption","Input Password")

    elif password !="9876":
        messagebox.showerror("encryption","Invalid Password")

def decrypt():
     password=code.get()

     if password=="9876":
        screen2=Toplevel(screen)
        screen2.title("decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#E6E6FA")

        message=text1.get(1.0,END)
        decode_message=message.encode("ascii")
        base64_bytes=base64.b64decode(decode_message)
        decrypt=base64_bytes.decode("ascii")

        Label(screen2,text="DECRYPT",font="timesnewroman",fg="black",bg="#FFF0F5").place(x=10,y=0)
        text2=Text(screen2,font="robote 10",bg="#FFEBCD",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)

        text2.insert(END,decrypt)
        
     elif password !="":
        messagebox.showerror("decryption","Input Password")
        
     elif password !="9876":
        messagebox.showerror("decryption","Invalid Password")


def main_screen():

    global screen
    global code
    global text1

    screen=Tk()
    screen.geometry("375x398")

    #icon
    
    screen.title("CodeAPP")

    def reset():
        code.set("")
        text1.delete(1.0,END)

    Label(text="Enter text for encryption and decryption",fg="black",font=("calbri",13)).place(x=10,y=10)
    text1=Text(font="Timesnewroman 13",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=50,width=355,height=100)

    Label(text="Enter secret key for encryption and decryption",fg="black",font=("calbri",13)).place(x=10,y=170)

    code=StringVar()
    Entry(textvariable=code,width=19,bd=0,font=("calbri",18),show="*").place(x=10,y=200)

    Button(text="ENCRYPT TEXT",height="2",width=23,bg="#87CEEB",fg="white",bd=0,command=encrypt).place(x=10,y=250)
    Button(text="DECRYPT TEXT",height="2",width=23,bg="#DDA0DD",fg="white",bd=0,command=decrypt).place(x=200,y=250)
    Button(text="RESET",height="2",width=50,bg="#DB7093",fg="white",bd=0,command=reset).place(x=10,y=300)
    

    screen.mainloop()

main_screen()
