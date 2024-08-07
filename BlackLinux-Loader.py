import os
import random


print("benvenuto nell installer di black linux")
print("continuare con l'installer?")
print("S/N")
sn = input()
if sn == "S":
    print("Aaccetta i termini di utilizzo e condizioni?")
    print("S/N")
    sn2 = input()
    if sn2 == "S":
        print("installazione in corso...")
        os.system("sudo apt-get update")
        os.system("sudo apt-get install -y git")
        os.system("sudo apt-get install -y curl")
        os.system("sudo apt-get install -y wget")
        os.system("sudo apt-get install -y python3-pip")
        print("installazione terminata a buon fine")
        print("digita invio per terminare l'installazione")
        input()
    else:
        print("installazione annullata")
else:
    print("non siamo riusciti a completare l'installazione")