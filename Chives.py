import re
import os
import glob
import sys
import time
from KeyListener import *
from Interface import *

class Chives:
    def __init__(self):
        self.commandMap = {}
        self.loadScripts()
        self.hotkeyListener = HotKeyListener()
        self.hotkeyListener.registerCallback(1, self.getUserInput)
        self.hotkeyListener.finalizeCallbackRegistrations()
        self.running = True

    def commandLoop(self):
        while self.running:
            self.hotkeyListener.checkForHotKey()

    def getUserInput(self):
        self.app = App()
        self.app.start()
        userInput = self.app.userInput
        success = self.parseCommand(userInput)
        if not success:
            self.getUserInput()

    def loadScripts(self):
        # Gets all the files with the .py extension from the script folder
        scripts = self.getAllScriptNames()
        for script in scripts:
            # Because of the above, we have to ignore the case of __init__
            if script != '__init__':
                module = __import__('scripts.' + script, fromlist=['ScriptHandler'])
                handlerClass = getattr(module, 'ScriptHandler')
                handler = handlerClass()
                self.addToCommandMap(handler)
                
    def getAllScriptNames(self):
        path = os.path.dirname(os.path.realpath(__file__)) + '/scripts/'
        scripts = [f for f in os.listdir(path) if os.path.isfile(path + f) and re.search('[\w \\\\]+.py$', f)]
        for i in range(len(scripts)):
            scripts[i] = scripts[i][:-3]
        return scripts

    def addToCommandMap(self, handler):
        commands = handler.commands
        for command in commands:
            self.commandMap[command] = handler.runScript

    def parseCommand(self, entry):
        if entry == 'Reload Scripts':
            self.reloadScripts()
        for command in self.commandMap:
            match = re.search(command, entry)
            if match:
                self.commandMap[command](match.group)
                return True
        return False

    def reloadScripts(self):
        self.commandMap = {}
        self.loadScripts()

if __name__ == '__main__':
    chives = Chives()
    chives.commandLoop()