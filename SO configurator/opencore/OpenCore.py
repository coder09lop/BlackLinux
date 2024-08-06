print("benvenuto/bentornato nell OpenCore selezionare sistema operativo")
print("1. macOS High Sierra")
print("2. Ubuntu")
print("2. Windows 10")
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
    for numero in range(1000000):
        print(numero)
    print("riavii il dispositivo per maggiora sicurezza")
    print("prema invio per uscire")
    usci = input()

    #win11
elif oschoice == "4":
    print("Windows 11 selezionato")
    print("installando i file di sistema per" + oschoice)
    print("la preghiamo di rilassarsi mentre facciamo la magia")
    print("premere invio per iniziare l'installazione vera")
    invio4 = input()
    for numero in range(10000000000):
        print(numero)
    print("riavii il dispositivo per maggiora sicurezza")
    print("prema invio per uscire")
    usci = input()


else:
    print("errore")