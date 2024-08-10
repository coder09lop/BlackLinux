import os
import random


print("selezionare aggiornamento da eefetuare")
print("1. aggiornamento wine e tutti i tool")
print("2. aggiornamento completo ")
print("3. aggiornamento solo wine")
opzione = input("inserisci il numero della tua scelta: ")
if opzione == "1":
    os.system("sudo apt-get update && sudo apt-get install -y wine-stable wine64")
    os.system("sudo apt-get install -y winetricks")
elif opzione == "2":
    os.system("sudo apt-get update && sudo apt-get install -y wine-stable wine64")
    os.system("sudo apt-get install -y winetricks")
elif opzione == "3":
    os.system("sudo apt-get update && sudo apt-get install -y wine-stable wine64")
else:
    print("scelta non valida")


