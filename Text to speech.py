import os
import pyttsx3 as py

Engine = py.init()
os.chdir("Storage\\")

def con(Text,File_Name):
    try:
        Engine.save_to_file(Text,"{0}.mp3".format(File_Name))
        Engine.runAndWait()
        
    except Exception as Error:
        print(Error)

while True:
    Text = str(input("Text:  "))
    File_Name = str(input("FIle Name:  "))
    con(Text,File_Name)
    
