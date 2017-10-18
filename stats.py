class stats(object):

    def __init__(self, array, debug = False):
        self.debug = debug;
        self.array = array;

        obj = {};

        # On init l'objet

        for i in range(len(array)) :
            obj[array[i]] = {
                'count' : 0,
                'pourcentage' : 0
            };

        self.obj = obj;

    
    def countPercentage(self):
        obj = self.obj;
        array = self.array;
        
        # On compte le nombre d'occurences dans le texte
        # Et on fais le pourcentage
        for i in range(len(array)) :
            obj[array[i]]['count'] += 1;
            pourcentage = "%.2f" % (obj[array[i]]['count'] / len(array));
            obj[array[i]]['pourcentage'] = pourcentage + " %";

        return obj;
