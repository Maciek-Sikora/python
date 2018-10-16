path = ("C:/Users/%USERNAME%/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/")
tekst = ("print(echo)")
with open(path+'test.bat', mode='w') as f:
     file.write(f"""
    {tekst}
    """)

    
