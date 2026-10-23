def zasifruj(text,posun):
    abeceda = "abcdefghijklmnopqrstuvwxyz"
    vysledek = ""
    
    for znak in text.lower():
        index = abeceda.find(znak)
        if index != -1:
            novy_index = (index + posun) % 26
            vysledek += abeceda[novy_index]
        else:
            vysledek += znak           
    return vysledek

print(zasifruj("ahoj svete",3))
