class ScriptHandler:
    def __init__(self):
        self.commands = ['google (\w)']

    def runScript(self, args):
        print args