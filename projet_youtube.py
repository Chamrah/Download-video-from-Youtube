# Importation the libraries
from tkinter import *
# the library that responsible with the file 
from tkinter import filedialog
# the library that responsible with the dowload of the video from youtube 
import pytube
from tkinter import ttk
import threading


root = Tk()
root.geometry("600x320")
root.title("Download video from youtube")
root.resizable(FALSE,FALSE)

# Function that responsable of the open and show the directory and print it in the entry 
def file():
    file1 = filedialog.askdirectory(title="ziad")
    entr2.delete(0,"end")
    entr2.insert(0,file1)
    
# Function that do the process of downloading the video from youtube
def download():
    lbl3.config(text="Statut : Downloading...")
    url = entr1.get() 
    folder = entr2.get()
    pytube.YouTube(url,on_complete_callback=complete).streams.get_highest_resolution().download(folder)

# Function that have one mission and is display the finish of the mission
def complete(stream=None,chunk=None,file_handle=None,remaining=None):
    lbl3.config(text="Status : Finish")

# Display logo Youtube
pic = PhotoImage(file="youtube.png").subsample(2)

logo = Label(root,image=pic).place(relx=0.5,rely=0.2,anchor="center")

# Display the labels and the entries and the buttons

lbl1 = Label(root,text="Youtube link")
lbl1.place(x="120",y="120")
entr1 = ttk.Entry(root)
entr1.place(x="220",y="120",width="280")

lbl2 = ttk.Label(root,text="Download folder")
lbl2.place(x="120",y="160")


entr2 = ttk.Entry(root)
entr2.place(x="220",y="160",width="200")

btn_browse = ttk.Button(root,text="Browse",command=file)
btn_browse.place(x="430",y="159",height="25",width="70")

btn1 = ttk.Button(root,text="Download",command=threading.Thread(target=download).start)
btn1.place(x="120",y="200",width="380")

lbl3 = Label(root,text="Status : Ready",bg="white")
lbl3.place(rely=1,anchor="sw",relwidth=1)
root.mainloop()