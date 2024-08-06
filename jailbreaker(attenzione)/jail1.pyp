print("benvenuto nei file dell sistema")
print("che vuoi fare?")
print("1. Modificare registri di sistema")
print("2. Aviia JailBreak")
print("3. EXIT")
loop = input()

#1

if loop == "1":
    print("DISCLAIMER💀")
    print("questo può danneggiare il tuo sistema quindi per ragioni di sicurezza ci dia il codice assegnato dall amministratore")
    disc = input()
    if disc == "159874":
        print("ok")


#jailbreak
elif loop == "2":
    print("DISCLAIMER💀")
    print("questo può danneggiare il tuo sistema quindi per ragioni di sicurezza ci dia il codice assegnato dall amministratore")
    disc = input()
    if disc == "2317159874":
        print("ok")
        print("che cosa vuoi moddare")
        print("1. bootloader")
        print("2. OpenCore")
        #bl
        loop3 = input()
        if loop3 == "1":
            print("ok")
            print("premi invio per iniziare")
            for numero in range(10000):
                print(numero)
            print("ecco finito premi invio per uscire")
            usci = input()
                
            #op
        elif loop3 == "2":
            print("ok")
            print("premi invio per iniziare")
            for numero in range(10000):
                print(numero)
            print("ecco finito premi invio per uscire")
            usci = input()
    #EXIT
elif loop == "3":
    print("ok")


#default
else:
    print("errore")