import random
import os



print("benvenuto/bentornato nell OpenCore selezionare sistema operativo")
print("1. macOS High Sierra")
print("2. Ubuntu")
print("3. Windows 10")
print("4. Windows 11")
print("5. exit")
oschoice = input()
#macos
if oschoice == "1":
    print("macOS High Sierra selezionato")
    print("installando i file di sistema per" + oschoice)
    print("la preghiamo di rilassarsi mentre facciamo la magia")
    print("premere invio")
    invio = input()
    os.system("sudo apt-get install qemu-system uml-utilities virt-manager git \
    wget libguestfs-tools p7zip-full make dmg2img tesseract-ocr \
    tesseract-ocr-eng genisoimage vim net-tools screen -y")
    for numero in range(1000000):
        print(numero)
    print("installazione completata")
    print("riavii il dispositivo per maggiora sicurezza")
    print("prema invio per uscire")
    usci = input()
    #Ubuntu
elif oschoice == "2":
    print("Ubuntu selezionato")
    print("installando i file di sistema per" + oschoice)
    print("la preghiamo di rilassarsi mentre facciamo la magia")
    print("premere invio per iniziare l'installazione vera")
    invio2 = input()
    os.system("sudo apt-get install qemu-system uml-utilities virt-manager git")
    for numero in range(1000000):
        print(numero)
    print("installazione completata")
    print("riavii il dispositivo per maggiora sicurezza")
    print("prema invio per uscire")
    usci = input()
#win10
elif oschoice == "3":
    print("Windows 10 selezionato")
    print("installando i file di sistema per" + oschoice)
    print("la preghiamo di rilassarsi mentre facciamo la magia")
    print("premere invio per iniziare l'installazione vera")
    invio3 = input()
    os.system("sudo apt-get install qemu-system uml-utilities virt-manager git")
    print("che architettura hai?")
    print("1. x64")
    print("2. x32")
    print("1-2")
    arch = input()
    if arch == "1":
        os.system("sudo apt update")
        os.system("sudo apt -get install wine64")
        os.system("sudo apt-get install winetricks")
        for numero in range(1000000):
            print(numero)
        print("installazione terminata premi invio per uscire")
    usci = input()
elif arch == "2": # type: ignore
    os.system("sudo apt update")
    os.system("sudo apt -get install wine32")
    os.system("sudo apt-get install winetricks")
    for numero in range(1000000):
        print(numero)
    print("installazione terminata premi invio per uscire")
    usci = input()
    #win11
elif oschoice == "4":
    print("Windows 11 selezionato")
    print("installando i file di sistema per windows 11")
    print("la preghiamo di rilassarsi mentre facciamo la magia")
    print("premere invio per iniziare l'installazione vera")
    invio3 = input()
    os.system("sudo apt-get install qemu-system uml-utilities virt-manager git")
    print("che architettura hai?")
    print("1. x64")
    print("2. x32")
    print("1-2")
    arch = input()
    if arch == "1":
        os.system("sudo apt update")
        os.system("sudo apt -get install wine64")
        os.system("sudo apt-get install winetricks")
        for numero in range(1000000):
            print(numero)
        print("installazione terminata premi invio per uscire")
    usci = input()
elif arch == "2": # type: ignore
    os.system("sudo apt update")
    os.system("sudo apt -get install wine32")
    os.system("sudo apt-get install winetricks")
    for numero in range(1000000):
        print(numero)
    print("installazione terminata premi invio per uscire")
    usci = input()
    #EXIT
elif oschoice == "5":
    print("ciao")
#Default
else:
    print("errore")