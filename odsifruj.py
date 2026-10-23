def cesarova_sifra(text,posun):
    abeceda = "abcdefghijklmnopqrstuvwxyz"
    vysledek = ""
    for znak in text.lower():
            index = abeceda.find(znak)
            if index != -1:
                novy_index = (index - posun) % 26
                vysledek += abeceda[novy_index]
            else:
                vysledek += znak           
    return vysledek

print(cesarova_sifra("ahoj svete",3))