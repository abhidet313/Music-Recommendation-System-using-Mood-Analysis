from Tkinter import *
import secondscreen
class firstscreen:

    # if user is not in db

    def __init__(self, master):
        self.master = master
        self.framei = Frame(master)
        self.framei["bg"] = "navy blue"
        self.framei.pack()
        self.name = Label(self.framei, text="Please Enter Your Name", font=("Helvetica",14),bg="navy blue", fg="white")
        self.namevar = StringVar()
        self.entry = Entry(self.framei, textvariable=self.namevar)
        self.namevar.set("")
        self.namebutton = Button(self.framei, text="Submit", command=self.addname,font=("Helvetica",14),bg="powder blue")
        self.name.grid(row=0, pady=15)
        self.entry.grid(row=1, pady=15)
        self.namebutton.grid(row=2)
        self.entry.bind("<Return>", self.addname)

    #if not then add user
    def addname(self,*args):
        self.username = self.namevar.get()
        self.framei.destroy()
        print("hello "+self.username+" "+self.userid)
        self.userob.insertToUserData(self.userid,self.username)
        ob = secondscreen.secondscreen(self.master)

if __name__=="__main__":
    root = Tk()
    ob = firstscreen(root)
    root.title("MUSIC RECOMMENDATION SYSTEM")
    # make_label(framei, img)
    root.iconbitmap(default="C:/Users/Abhishek/Desktop/python/music/icons/music.ico")
    root.configure(background="navy blue")
    root.geometry("320x260")
    root.mainloop()


