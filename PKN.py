import random
uzytkownik = input("Jaki jest twój ruch: ")
ruchy = ["p","k","n"]
secure_random = random.SystemRandom()
komputer = secure_random.choice(ruchy)
print(komputer)
if uzytkownik == komputer:
    print("remis")
elif uzytkownik == "p" and komputer == "k":
    print("wygrałes")
elif uzytkownik == "k" and komputer == "p": 
    print("przegrales")
elif uzytkownik == "p" and komputer == "n": 
    print("przegrales")
elif uzytkownik == "n" and komputer == "p": 
    print("wygrałes")
elif uzytkownik == "n" and komputer == "k":
    print("przegrałes")
elif uzytkownik == "k" and komputer == "n":
    print("wygrales")