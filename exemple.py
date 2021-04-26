# import datetime
# now = datetime.datetime.now()
# print ("La date courante est : ")
# print (now.strftime("%H:%M:%S %d/%m/%Y "))

# import locale
# import time
# locale.setlocale(locale.LC_TIME, '')

# print(time.strftime('%A %d/%m/%Y %H:%M:%S'))


from datetime import date, time, datetime


# # 2- Créer une instance de l'objet date.
aujourdhui=date.today()

# # 3- Afficher la date d'aujourd'hui
# print("Aujourd'hui nous somme le : ",aujourdhui)


    # 3-1- Afficher le jour de la date d'aujourd'hui
print("Aujourd'hui c'est : ",aujourdhui.day)
    # 3-1- Afficher le mois en cours
print("Le mois courant c'est : ",aujourdhui.month)
     # 3-1- Afficher l'année en cours
print("L'année courant c'est : ",aujourdhui.year)

# 3-2- Afficher le numéro de jour de la semaine
print("Le numéro numéro de jour de la semaine : ",aujourdhui.weekday())

