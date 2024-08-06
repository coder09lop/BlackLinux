print("benvenuto/bentornato nell dtabase dell ufficio")
print("chi accede ogii?")
print("1. amministratore")
print("2. riyad")
print("3. 19979075")
print("4. aggiungi utente")
dt = input()
if dt == "1":
    print("benvenuto amministratore")

#2

elif dt == "2":
    print("benvenuto riyad")
    print("inserisci password")
    paswd = input()
    if paswd == "1974516715":
        print("ok inizio lavoro premi invio per iniziare")
        inv = input()
        for numero in range(100000000):
            print(numero)
    print("ciao")
    #3

elif dt == "3":
    print("benvenuto 19979075")
    print("inserisci password")
    pass1 = input()
    if pass1 == "2317":
        print("esci")
    #4
elif dt == "4":
    print("inserisci nome utente")
    nm = input()
    if nm == "admin159874":
        print("inserisci password")
        password = input()
        if password == "admin159876":
            print("utente aggiunto")
            print("digita invio per uscire")
            invio = input()
    
    else:
        print("ciao")




#def



else:
    print("ciao")