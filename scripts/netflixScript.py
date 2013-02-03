class ScriptHandler:
    def __init__(self):
        self.commands = ['netfix ([\w ]+)']

    def runScript(self, args):
        print ""