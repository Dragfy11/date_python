from datetime import date, time, datetime
# 2- Créer une instance de l'objet date.
aujourdhui=datetime.now()
    # 3- Afficher la date d'aujourd'hui
print("Aujourd'hui nous somme le : ",aujourdhui)
    # ce qui affiche:.....2021-04-26 15:19:13.475320
    # 4- Afficher l'heure actuelle
heure=datetime.time(datetime.now())
print("Il est : ",heure)
    # ce qui affiche:.....15:20:22.069350