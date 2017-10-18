class config(object):

    def __init__(self, debug = False):
        self.debug = debug;

    # Modifier array 'special' pour enlever des char special
    # Modifier array 'words' pour exclure un mot des stats
    def remove(self):
        return {
            'special': [ ',', ':', '\'' ],
            'words': [ 'le', 'd', 'un' ]
        };
