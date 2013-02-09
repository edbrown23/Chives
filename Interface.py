import time
from Tkinter import *
from win32api import GetSystemMetrics

SCREEN_WIDTH = GetSystemMetrics(0)
SCREEN_HEIGHT = GetSystemMetrics(1)

class App:
    def __init__(self, message='How can I help you, sir?'):
        self.message = message    
        self.createWindow()

    def createWindow(self):
        self.root = Tk()

        self.setHeightAndPosition()
        self.root.title("Chives")

        self.entry = Entry(self.root, width=30)
        self.entry.grid(row=0)
        self.entry.bind("<Return>", self.handle_return)
        self.entry.focus_set()

        self.speech = StringVar()
        self.speechLabel = Label(self.root, textvariable=self.speech)
        self.speechLabel.grid(row=1)
        self.speech.set(self.message)

    def setHeightAndPosition(self):
        x = SCREEN_WIDTH - 220
        y = SCREEN_HEIGHT - 130
        posString = "+" + str(x) + "+" + str(y)
        window_width = 200
        window_height = 50
        dimString = str(window_width) + "x" + str(window_height)
        self.root.geometry(dimString + posString)

    def start(self):
        self.root.focus_set()
        self.root.mainloop()

    def handle_return(self, event):
        self.userInput = self.entry.get()
        self.ackAndClose()

    def ackAndClose(self):
        self.speech.set("Yes, sir.")
        self.root.update()
        self.root.destroy()

    def informOfBadCommand(self):
        self.speech.set("I don't know that, sir.")
        self.root.update()