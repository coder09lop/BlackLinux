import random



print("benvenuti/bentornato nella vpn degli hackers")
print("per favore inserisci il tuo username e password")
username = input("inserisci il tuo username: ")
if username == "riyadsuper":
    print("benvenuto" + username)
    print("inserisci password")
    password = input()
    if password == "Omargrini2011@":
        print("password corretta")
        print("sei connesso alla vpn degli hacker")
        print("ora ti daremo l'ip")
        print("l'ip è")
        ip = ("192.89.0987", "1892.9303,9393", "9393.9484.9494", "192.9090.8765", "hacking.9090")
        print(random.choice(ip))
        print("premi invio per uscire")
        esc = input()
    else:
        print("password sbagliata")

#default
else:
    print("username non trovato")