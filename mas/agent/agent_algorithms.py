from random import random

def nothing(agent):
    return

##############################
# Probl`eme de l’exploration #
##############################

def marche_aleatoire(agent):
    available_ports = agent.available_ports
    port = random.choice(available_ports)

    agent.move_along(port)

    #TODO : autres choses à faire ?
    return

def mdm(agent):
    #TODO : besoin de mémoire d'agent
    """
    Main droite  contre le mur
    Ici, la topologie est un arbre, et k d ́enote son nombre d’arˆetes
    :param agent:
    :return:
    """
    #TODO : port_back=0 au début (faire if pour choix etape 1)
    #TODO : sauvegarde i au fur et à mesure des appels de mdm()
    port_back = agent.get_port_back()
    available_ports = agent.available_ports
    degre = len(available_ports)
    i=0
    #TODO : get k
    k=0

    if i <= 2*k:
        if port_back+1 > degre:
            port = 1
        else:
            port = port_back+1

        agent.move_along(port)
        i+=1
    else :
        agent.wait()

    return


def dfs(agent):
    """
    Parcours en profondeur
    :param agent:
    :return:
    """
    return

def rotor_router(agent):
    """
    Rotor Router
    :param agent:
    :return:
    """
    return

####################################
# Cartographie de graphes anonymes #
####################################

def cartographie_jeton(agent):
    """
    Cartographie avec un jeton
    :param agent:
    :return:
    """
    return

def cartographie_marquage(agent):
    """
    Cartographie avec un jeton amovible
    :param agent:
    :return:
    """
    return

############################
# Probl`eme du rendez-vous #
############################


def rv_graphe(agent):
    """
    :param agent:
    :return:
    """
    return

def rv_anneau_naif1(agent):
    """
    Chaque agent fait id tours de l’anneau et s’arrˆete

    :param agent:
    :return:
    """
    return

def rv_anneau_naif2(agent):
    """
    Chaque agent bouge puis attend id −1  ́etapes (toujours dans le mˆeme sens)
    :param agent:
    :return:
    """
    return

def rv_anneau1(agent):
    """
    Rendez-vous synchrone dans l’anneau
    Identifiants de tailles similaires

    :param agent:
    :return:
    """
    i = 0 #TODO : mettre en mémoire pour pas réinitialiser à chaque fois

    if i == 0: #L'agent bouge 1 fois
        #On tourne toujours dans le même sens
        port = 1
        agent.move_along(port)

    else :  #L'agent attend id-1 étapes
        agent.wait()

    i+=1
    if i > agent.get_id():
        i = 0

    #TODO : comment stocket le i sans mémoire ?
    return

def rv_anneau2(agent):
    """
    Rendez-vous synchrone dans l’anneau
    Identifiants de tailles diff ́erentes

    :param agent:
    :return:
    """
    return

def rv_anneau_sync(agent):
    """
    Rendez-vous synchrone dans l’anneau
    Idée : Alterner les ex ́ecutions des algorithmes pour identifiants similaires et diff ́erents

    :param agent:
    :return:
    """
    return

def rv_arbre_sync(agent):
    """
    :param agent:
    :return:
    """
    return

#TODO : algo en vert
def rv_arete_sync(agent):
    """
    :param agent:
    :return:
    """
    return

def rv_ligne_anonyme(agent):
    """
    :param agent:
    :return:
    """
    return


############################
# Recherche de trous noirs #
############################

def time_out(agent):
    """
    R ́eseau synchrone

    :param agent:
    :return:
    """
    return

def cautious_walk(agent):
    """
    R ́eseau asynchrone ⇒ pas de temps, et donc pas de Time-Out

    :param agent:
    :return:
    """
    return
