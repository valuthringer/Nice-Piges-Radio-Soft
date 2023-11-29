import os
import requests
from datetime import datetime, timedelta
import time


            ### VALEURS A CHANGER EN FONCTION DE LA RADIO ###
##############################################################################

radio_nom = "Redzing Radio"

url_flux = "https://redzingradio.com/stream"

extension_flux = "mp3"   #(on peut mettre "aac", "mp3", "flac"...)

##############################################################################



            ### NE PAS MODIFIER POUR BON FONCTIONNEMENT ###
def telecharger_flux(url):
    reponse = requests.get(url, stream=True)
    return reponse.iter_content(chunk_size=1024)

def enregistrer_horaire(extension_flux, url_flux, dossier_sortie, dossier_jour, heure):
    temps_actuel = datetime.now()
    
    nom_fichier_sortie = f"{dossier_sortie}/{dossier_jour}/{heure:02}H."+extension_flux

    donnees_flux = telecharger_flux(url_flux)

    # Enregistrer pendant une heure complète
    prochaine_heure = (temps_actuel + timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)

    # Flag indiquant que l'écriture est en cours -- impossible d'ouvrir le fichier pour l'utilisateur
    writing_flag = f"{nom_fichier_sortie}.writing"

    with open(writing_flag, "w") as flag_file:
        pass  # Créer le fichier d'indication d'écriture

    with open(nom_fichier_sortie, "wb") as fichier_sortie:
        for morceau in donnees_flux:
            with open(writing_flag, "r") as flag_file:
                if flag_file.read().strip() == "stop":
                    break  # Arrêter l'écriture si le drapeau est défini sur "stop"
            fichier_sortie.write(morceau)
            if datetime.now() >= prochaine_heure:
                break

    # Supprimer le drapeau d'écriture
    os.remove(writing_flag)

    print(f"Enregistrement {nom_fichier_sortie}")


def main(nom_radio):
    print("________________________________________________________________________")
    print("          Bienvenue sur Nice Piges Radio - by @valuthringer")
    print("________________________________________________________________________")
    print("")
    print("L'enregistrement des piges pour " + nom_radio + " a démarré !")
    print("Pour arrêter l'enregistrement, fermez cette fenêtre, sinon, laissez la ouverte tant que vous souhaiterez enregistrer")
    print("")
    print("Vos piges s'enregistrent dans le dossier 'Piges " + nom_radio + "' du dossier courant du logiciel")
    print("")
    print("")
    print("Fabrication des piges en cours...")

    dossier_sortie = "Piges " + nom_radio

    if not os.path.exists(dossier_sortie):
        os.makedirs(dossier_sortie)

    jours_de_la_semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
    derniere_heure_enregistree = -1

    while True:
        temps_actuel = datetime.now()
        jour_actuel = jours_de_la_semaine[temps_actuel.weekday()]
        heure_actuelle = temps_actuel.hour

        # Créer un nouveau dossier par jour si nécessaire
        dossier_jour = jours_de_la_semaine[temps_actuel.weekday()]
        if not os.path.exists(f"{dossier_sortie}/{dossier_jour}"):
            os.makedirs(f"{dossier_sortie}/{dossier_jour}")

        # Vérifier si l'heure a changé depuis le dernier enregistrement
        if heure_actuelle != derniere_heure_enregistree:
            enregistrer_horaire(extension_flux, url_flux, dossier_sortie, jour_actuel, heure_actuelle)
            derniere_heure_enregistree = heure_actuelle

        # Attendre une courte période avant de vérifier à nouveau
        time.sleep(1)  # toutes les 1s

if __name__ == "__main__":
    main(radio_nom)