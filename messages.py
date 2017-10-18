class messages(object):

    def __init__(self, debug = False):
        self.debug = debug;

    def infos(self):
        return {
            'askFileOrText': 'Tapez "1" pour séléctionner un fichier'
                              + ' ou "2" pour saisir du texte : \n',
            'askText': 'Saisir le texte : \n'
        };


    def errors(self):
        return {
            'invalid_input': 'Saisie incorrecte !'
        };

    
        
