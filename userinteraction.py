from messages import messages;
from browser import browser;

class userinteraction(object):

    def __init__(self, debug = False):
        self.debug = debug;
        self.msg = messages().infos();
        self.err = messages().errors();

    # Gère les demandes
    def ask(self, error):

        # Si l'utilisateur c'est trompé
        # != 1 ou != 2
        if (error == True):
            print(self.err['invalid_input']);
        
        fileortext = self.askFileOrText();

        # Ouvre le browser (tkinter)
        if (fileortext == "1"):
            file = browser(self.debug);
            return file.get();

        # Texte saisi par l'user
        if (fileortext == "2"):
            return self.askText();

        return False;
            

    # Demande à l'utilisateur s'il souhaite saisir
    # son texte ou séléctionner un fichier
    def askFileOrText(self):
        return input(self.msg['askFileOrText']);

    # Demande à l'utilisateur de saisir du texte
    def askText(self):
        return input(self.msg['askText']);
        

    
        
