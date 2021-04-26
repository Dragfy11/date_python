# 1- importer les modules de date, time, datetime
from datetime import date, time, datetime
def application():    
     #Afficher le mois actuel en toute lettre
    aujourdhui=datetime.now()
    leMois = aujourdhui.month
    lesMois = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
               'Juillet', 'Août',
               'Septembre', 'Octobre', 'Novembre', 'Décembre']
    print("Le mois courant est numéro : %d "% leMois)
    print("Le mois courant est  : ",lesMois[leMois-1])
if __name__ == "__main__":
    application()
