import os
import random


print("selezionare aggiornamento da eefetuare")
print("1. aggiornamento wine e tutti i tool")
print("2. aggiornamento completo ")
print("3. aggiornamento solo wine")
print("4. installa/aggiorna PlayOnLinux")
print("5. esci")
opzione = input("inserisci il numero della tua scelta: ")
if opzione == "1":
    os.system("sudo apt-get update && sudo apt-get install -y wine-stable wine64")
    os.system("sudo apt-get install -y winetricks")
    os.system("sudo apt-get install -y winbind")
    print("finito digita invio per uscire")
    usci = input()
elif opzione == "2":
    os.system("sudo apt-get update && sudo apt-get install -y wine-stable wine64")
    os.system("sudo apt-get install -y winetricks")
    print("finito digita invio per uscire")
    usci = input()
elif opzione == "3":
    os.system("sudo apt-get update && sudo apt-get install -y wine-stable wine64")
    print("finito digita invio per uscire")
    usci = input()
elif opzione == "4":
    os.system("sudo apt-get update && sudo apt-get install -y playonlinux")
    print("finito digita invio per uscire")
    usci = input()
elif opzione == "5":
    print("buona giornata")
else:
    print("scelta non valida")


