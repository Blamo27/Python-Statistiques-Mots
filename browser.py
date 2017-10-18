# Interface nav' pour fichier
from tkinter.filedialog import *;

class browser(object):

    def __init__(self, debug = False):
        self.debug = debug;

        # Ouvre le browser sans afficher de fenêtre Tk
        Tk().withdraw();
        file = askopenfilename();

        # Lecture du fichier
        file = open(file, "r");
        self.text = file.read();


    def get(self):
        text = self.text;

        # Si débug activé
        if (self.debug == True):
            print(file.read());
        
        return text;
