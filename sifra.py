def cesarova_sifra(text):
    abeceda = "abcdefghijklmnopqrstuvwxyz"
    vysledek = ""
    
    for znak in text.lower():
        # Najde pozici písmena v abecedě
        index = abeceda.find(znak)
        
        if index != -1:
            # Posune o 3 a zajistí zavinutí na začátek pomocí % 26
            novy_index = (index + 3) % 26
            vysledek += abeceda[novy_index]
        else:
            # Pokud to není písmeno (např. mezera), nechá ho být
            vysledek += znak
            
    return vysledek

# Příklad použití:
print(cesarova_sifra("ahoj svete"))