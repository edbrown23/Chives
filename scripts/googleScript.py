import webbrowser

class ScriptHandler:
    def __init__(self):
        self.commands = ['google ([\w ]+)', 'search ([\w ]+)']

    def runScript(self, args):
        searchTerm = str(args(1))
        terms = searchTerm.split()
        first = True
        url = 'www.google.com/search?q='
        for term in terms:
            if first:
                url += term
                first = False
            else:
                url += '+' + term
        webbrowser.open(url)
