# Affichage d'objets proprement
from pprint import pprint;

# Import la classe userinteraction
# permettant d'interroger l'user
from userinteraction import userinteraction;

# Manipulation du texte
from textcontrol import textcontrol;

# Statistiques sur le tableau
from stats import stats;


# Fonction pour interroger l'user
user = userinteraction();
def askUser(fail = False):
    response = user.ask(fail);

    # Si l'utilisateur c'est trompé != 1 || !=2
    if (response == False): askUser(True);

    return response;


# Interroge l'utilisateur
text = askUser();

# Contrôle du texte (remove words & char)
control = textcontrol(text);
array = control.stabilize();

# Statistiques sur l'array contenant
# tous les mots
stat = stats(array);
finalArray = stat.countPercentage();

# On affiche l'array
pprint(finalArray);
