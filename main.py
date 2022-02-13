import string
import tkinter as tk
from tkinter import Button
from ChipReader import ChipReader
from RequestService import RequestService
from loopExecuter import LoopExecuter


class ABC(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.pack()
        self.make_widgets()

    def make_widgets(self):
        def checkForScan(self):
            chipId = ChipReader().read()
            requestservice = RequestService()
            userinfo = requestservice.getUserInfoByChip(chipId)

            if userinfo:
                showUser(userinfo, True)
            # if userinfo
            #    removeUser()
            # if userinfo
            #    notAssignedChip()

        def showUser(username: string, signedIn):
            userLable.config(text="Wilkommen {}".format(username))
            if signedIn == True:
                signIn.pack_forget()
                signOut.pack()
            if signedIn != True:
                signOut.pack_forget()
                signIn.pack()

        def removeUser():
            userLable.config(text="")
            signIn.pack_forget()
            signOut.pack_forget()

        def notAssignedChip():
            userLable.config(text="Unbekannter / nicht zugewiesener Chip")
            signIn.pack_forget()
            signOut.pack_forget()

        self.winfo_toplevel().title("ChipScanner")

        titleFrame = tk.Frame(master=self.winfo_toplevel(), height=100, bg="#eeeeee")
        titleFrame.pack(fill=tk.X, side=tk.TOP)

        title = tk.Label(master=titleFrame, text="ChipScanner", bg="#eeeeee")
        title.config(font=("Courier", 44))
        title.pack()

        body = tk.Frame(
            master=self.winfo_toplevel(), width=100, height=100, bg="#eeeeee"
        )
        body.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        userInfo = tk.Frame(body, height=100, bg="#eeeeee")
        userInfo.pack(fill=tk.X, side=tk.TOP)
        userLable = tk.Label(master=userInfo, bg="#eeeeee")
        userLable.config(font=("Courier", 22))
        userLable.pack()

        footer = tk.Frame(master=body, height=50, bg="#eeeeee")
        footer.pack(side=tk.BOTTOM)

        actions = tk.Frame(body, height=100, width=200, bg="#eeeeee")
        actions.pack(side=tk.BOTTOM)

        signIn = tk.Frame(master=actions, width=100, height=100, bg="#aaffaa")
        signInButton = Button(
            signIn,
            text="Kommen",
            bg="#aaffaa",
            width=10,
            height=5,
        )
        signInButton.config(font=("Courier", 22))
        signInButton.pack()

        signOut = tk.Frame(master=actions, width=100, height=100, bg="#ffaaaa")
        signOutButton = Button(
            signOut,
            text="Gehen",
            bg="#ffaaaa",
            width=10,
            height=5,
        )
        signOutButton.config(font=("Courier", 22))
        signOutButton.pack()

        spacer = tk.Frame(master=body, height=50, bg="#eeeeee")
        spacer.pack(side=tk.BOTTOM)

        LoopExecuter(2, checkForScan)


def toggleFullScreen(self, event):
    self.window.attributes("-fullscreen", True)


def quitFullScreen(self, event):
    self.window.attributes("-fullscreen", False)


root = tk.Tk()
root.geometry("480x320")
# root.attributes("-fullscreen", True)
# root.bind("<F11>", toggleFullScreen)
# root.bind("<Escape>", quitFullScreen)
abc = ABC(root)
root.mainloop()
