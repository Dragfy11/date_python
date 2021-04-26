# # import datetime

# # laDate = datetime.datetime.now()
# # print(laDate)

# # 1- importer les modules de date, time, datetime
# # from datetime import date, time, datetime
# # duree = datetime.now() - datetime(2010, 1, 1)
# # print(duree)

# # 1- importer les modules de date, time, datetime
# from datetime import datetime, timedelta
# # Utiliser datetime 
# maintenant = datetime.now()   
# # Afficher la date courante 
# print ("Maintenant est : ", str(maintenant)) 
  
# # Calculer les future dates 
# # Ajout de deux ans 
# prochaine_date_apres_2ans = maintenant + timedelta(days = 730)
# # Ajout de deux mois 
# prochaine_date_apres_2mois = maintenant + timedelta(days = 61)
# # Ajout de deux jours   
# prochaine_date_apres_2jours = maintenant + timedelta(days = 2) 
# # Calculer les dates antérieures 
# # Avant deux ans 
# anterieure_date_avant_2ans = maintenant - timedelta(days = 730)
# # Avant deux mois 
# anterieure_date_avant_2mois = maintenant - timedelta(days = 61)
# # Avant deux jours   
# anterieure_date_avant_2jours = maintenant - timedelta(days = 2) 


  
# # printing calculated future_dates 
# print('Prochaine date après 2 ans sera :', str(prochaine_date_apres_2ans))
# print('Prochaine date après 2 mois sera :', str(prochaine_date_apres_2mois)) 
# print('Prochaine date après 2 jours sera :', str(prochaine_date_apres_2jours)) 

# print('Anterieure_date_avant 2 ans sera :', str(anterieure_date_avant_2ans))
# print('Anterieure_date_avant 2 mois sera :', str(anterieure_date_avant_2mois)) 
# print('Anterieure_date_avant 2 jours sera :', str(anterieure_date_avant_2jours)) 

# 1- importer les modules de date, time, datetime
# from datetime import datetime, timedelta

# current_datetime = datetime.now()
# dt = current_datetime.date()
# print('Date courant :', dt)
# dt_tomorrow = dt + timedelta(days=1)
# print('Date de demain:', dt_tomorrow)

