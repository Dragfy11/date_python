# import time
# print(time.ctime())

# import time
# print(time.ctime(0))
#Thu Jan  1 01:00:00 1970

# import time
# print(time.ctime(1556689999))
#Wed May  1 07:53:19 2019

import time
# """ Importation module « temps » pour les
# opérations de temps importer le temps"""
# """utilisant ctime () pour afficher l’heure actuelle"""
print ( "Begin Execution:" , end = "" )
print ( time . ctime ()) 
# """Mise en veille () pour suspendre l'exécution
# d' impression( « attente de 5 sec. » )""" 
time.sleep( 5 )
# """utilise ctime () pour afficher l’ impression
# de l’ heure actuelle ( "End Execution:" , end = "" )"""
print ( time . ctime ())