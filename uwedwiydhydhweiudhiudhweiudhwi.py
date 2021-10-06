from tkinter import*
from PIL import Image, ImageTk
import pytz
from datetime import datetime
import time

root = Tk()
root.geometry("700x700")
root.title("Time")

indflag= ImageTk.PhotoImage(Image.open ("indflag.png"))
usflag= ImageTk.PhotoImage(Image.open ("usflag.png"))
ausflag= ImageTk.PhotoImage(Image.open ("ausflag.png"))
japflag= ImageTk.PhotoImage(Image.open ("japflag.png"))

#Ind
indlabel = Label(root,text="India")
indlabel.place(relx=0.2,rely=0.03,anchor=CENTER)

indimg = Label(root)
indimg["image"]=indflag
indimg.place(relx=0.2,rely=0.15,anchor=CENTER)

indtime = Label(root)
indtime.place(relx=0.2,rely=0.25,anchor=CENTER)

#Us
uslabel = Label(root,text="USA")
uslabel.place(relx=0.7,rely=0.05,anchor=CENTER)

usimg = Label(root)
usimg["image"]=usflag
usimg.place(relx=0.7,rely=0.15,anchor=CENTER)

ustime = Label(root)
ustime.place(relx=0.7,rely=0.25,anchor=CENTER)

#Aus
auslabel = Label(root,text="Australia")
auslabel.place(relx=0.2,rely=0.45,anchor=CENTER)

ausimg = Label(root)
ausimg["image"]=ausflag
ausimg.place(relx=0.2,rely=0.55,anchor=CENTER)

austime = Label(root)
austime.place(relx=0.2,rely=0.65,anchor=CENTER)

#Jap
japlabel = Label(root,text="Japan")
japlabel.place(relx=0.7,rely=0.43,anchor=CENTER)

japimg = Label(root)
japimg["image"]=japflag
japimg.place(relx=0.7,rely=0.55,anchor=CENTER)

japtime = Label(root)
japtime.place(relx=0.7,rely=0.65,anchor=CENTER)

class Ind():
    def times(self):
        home=pytz.timezone("Asia/Kolkata")
        localtm = datetime.now(home)
        crtm = localtm.strftime("%H:%M:%S")
        indtime["text"]="Time: " + crtm
        indtime.after(200,self.times)
        
class USA():
    def times(self):
        home=pytz.timezone("US/Central")
        localtm = datetime.now(home)
        crtm = localtm.strftime("%H:%M:%S")
        ustime["text"]="Time: " + crtm
        ustime.after(200,self.times)
        
class Aus():
    def times(self):
        home=pytz.timezone("Australia/ACT")
        localtm = datetime.now(home)
        crtm = localtm.strftime("%H:%M:%S")
        austime["text"]="Time: " + crtm
        austime.after(200,self.times)
        
class Jap():
    def times(self):
        home=pytz.timezone("Japan")
        localtm = datetime.now(home)
        crtm = localtm.strftime("%H:%M:%S")
        japtime["text"]="Time: " + crtm
        japtime.after(200,self.times)
        
indobj = Ind()
indbtn = Button(root,text="Show Time",command=indobj.times)
indbtn.place(relx=0.2,rely=0.3,anchor=CENTER)

usobj = USA()
usbtn = Button(root,text="Show Time",command=usobj.times)
usbtn.place(relx=0.7,rely=0.3,anchor=CENTER)

ausobj = Aus()
ausbtn = Button(root,text="Show Time",command=ausobj.times)
ausbtn.place(relx=0.2,rely=0.7,anchor=CENTER)

japobj = Jap()
japbtn = Button(root,text="Show Time",command=japobj.times)
japbtn.place(relx=0.7,rely=0.7,anchor=CENTER)

root.mainloop()

