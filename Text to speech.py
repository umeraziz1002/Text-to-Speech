import os
import pyttsx3 as py
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

Engine = py.init()
path = os.path.dirname(os.path.abspath(__file__))
folder = os.path.join(path,"Storage")
try:
    os.chdir("Storage\\")
except Exception:
    os.mkdir(folder)
    os.chdir("Storage\\")
def con(Text,File_Name):
    try:
        Engine.save_to_file(Text,"{0}.mp3".format(File_Name))
        Engine.runAndWait()
        messagebox.showinfo("Created","Audio File have been saved to Storage Folder")
        os.startfile(folder)
    except Exception as Error:
        messagebox.showerror("Error",Error)
def get_text():
    Text = Text_Entry.get("1.0","end-1c")
    File_Name = Name_Entry.get()
    con(Text,File_Name)

root = Tk()

root.geometry("700x450")
root.title("Text To Talk")

style = Style()
style.configure("TButton",height=10,font="arial 12 bold",background="red",width=40)

canvas = Canvas(root,height=600,width=700,bg="yellow")
canvas.pack(fill="both")
Title_Label = Label(root,text="ROBIN TEXT TO SPEECH",background="light green",foreground="red",font=("Black Ops One",35,"bold"))
Text_Label = Label(root,text="Text",font="arial 16",background="yellow")
Text_Entry = Text(root,height=10,width=50)
Name_Label = Label(root,text="Name",font="arial 16",background="yellow")
Name_Entry = Entry(root,width=65)
Create_Button = Button(root,command=get_text,text="Create",style="TButton")

canvas.create_window(350,50,window=Title_Label)
canvas.create_window(180,100,window=Text_Label)
canvas.create_window(350,200,window=Text_Entry)
canvas.create_window(350,350,window=Name_Entry)
canvas.create_window(180,320,window=Name_Label)
canvas.create_window(350,400,window=Create_Button)

root.mainloop()