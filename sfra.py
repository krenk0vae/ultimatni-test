def zasifruj(text, posun):
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


def desifruj(text, posun):
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


zprava = input("Zadej text: ")
posun = int(input("Zadej posun: "))
tajne = zasifruj(zprava, posun)
print("Zasifrovano:", tajne)
print("Desifrovano:", desifruj(tajne, posun))