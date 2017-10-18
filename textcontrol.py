from config import config;

class textcontrol(object):

    def __init__(self, text, debug = False):
        self.debug = debug;
        self.text = text;
        self.remove = config().remove();

    def stabilize(self):
        table = self.baseRemove();
        return self.wordsRemove(table);
        

    # Enlève les CHAR configurés (config.py)
    # Lowercase et le split
    def baseRemove(self):
        text = self.text;
        remove = self.remove['special'];
        
        # Lowercase
        text = text.lower();
        
        # On enlève certains caractères
        for i in range(len(remove)) :
            text = text.replace(remove[i], ' ');

        return text.split();

    # Enlève les mots configurés (config.py)
    def wordsRemove(self, table):
        remove = self.remove['words'];
        return [ x for x in table if x not in remove ];
