import os
import glob
import sys
import time
import re
from Tkinter import *
from win32api import GetSystemMetrics

SCREEN_WIDTH = GetSystemMetrics(0)
SCREEN_HEIGHT = GetSystemMetrics(1)

class Chives:
    def __init__(self, master):
        self.entry = Entry(master, width=30)
        self.entry.grid(row=0)
        self.entry.focus_set()

        self.speech = StringVar()
        self.speechLabel = Label(master, textvariable=self.speech)
        self.speechLabel.grid(row=1)
        self.speech.set("How may I help you, sir?")

        self.commandMap = {}
        self.loadScripts()

    def loadScripts(self):
        # Gets all the files with the .py extension from the script folder
        scripts = [os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__)+"/scripts/*.py")]
        for script in scripts:
            # Because of the above, we have to ignore the case of __init__
            if script != '__init__':
                mod = __import__('scripts.' + script, fromlist=['ScriptHandler'])
                handlerClass = getattr(mod, 'ScriptHandler')
                handler = handlerClass()
                self.addToCommandMap(handler)
                
    def addToCommandMap(self, handler):
        commands = handler.commands
        for command in commands:
            self.commandMap[command] = handler.runScript

    def parseCommand(self):
        entry = self.entry.get()
        if entry == 'Reload Scripts':
            self.reloadScripts()
        for command in self.commandMap:
            match = re.search(command, entry)
            if match:
                self.speech.set("Yes, sir.")
                self.commandMap[command](match.group)
                return True
        return False

    def reloadScripts(self):
        self.commandMap = {}
        self.loadScripts()

class App:
    def __init__(self):    
        self.root = Tk()

        self.chives = Chives(self.root)
        self.root.bind("<Return>", self.handle_return)

        self.setHeightAndPosition()
        self.root.title("Chives")

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
        success = self.chives.parseCommand()
        if(success):
            self.root.update()
            time.sleep(2)
            self.root.quit()
        else:
            self.chives.entry.delete(0, END)

if __name__ == "__main__":
    app = App()
    app.start()