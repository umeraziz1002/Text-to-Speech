import os
import pyttsx3 as py
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

Engine = py.init()
os.chdir("Storage\\")
def con(Text,File_Name):
    try:
        Engine.save_to_file(Text,"{0}.mp3".format(File_Name))
        Engine.runAndWait()
        messagebox.showinfo("Created","Audio File have been saved to Storage Folder")
        
    except Exception as Error:
        messagebox.showerror("Error",Error)
def get_text():
    Text = Text_Entry.get("1.0","end-1c")
    File_Name = Name_Entry.get()
    con(Text,File_Name)

root = Tk()

root.geometry("700x600")
root.title("Text To Talk")

canvas = Canvas(root,height=600,width=700,bg="yellow")
canvas.pack(fill="both")
Text_Label = Label(root,text="Text",font="arial 16",background="yellow")
Text_Entry = Text(root,height=10,width=50)
Name_Label = Label(root,text="Name",font="arial 16",background="yellow")
Name_Entry = Entry(root,width=65)
Create_Button = Button(root,command=get_text,text="Create")

canvas.create_window(180,100,window=Text_Label)
canvas.create_window(350,200,window=Text_Entry)
canvas.create_window(350,350,window=Name_Entry)
canvas.create_window(180,320,window=Name_Label)
canvas.create_window(350,400,window=Create_Button)

root.mainloop()