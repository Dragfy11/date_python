# 1- importer les modules de date, time, datetime
from datetime import date, time, datetime
def application():    
    #Afficher le jour actuelle en toute lettre
    aujourdhui=datetime.now()
    leJour = date.weekday(aujourdhui)
    lesJours = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    print("Aujourd'hui c'est le jour numéro : %d "% leJour)
    print("Aujourd'hui c'est le  : ",lesJours[leJour])
if __name__ == "__main__":
    application()