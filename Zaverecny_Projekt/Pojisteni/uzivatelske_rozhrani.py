from validace import Validace
from pojistenec import Pojistenec
from color import Color

# Inicializuje uživatelské rozhraní s danou evidencí pojištěnců.
class UzivatelskeRozhrani:
    def __init__(self, evidence):
        self.evidence = evidence

    # Získá a validuje vstup od uživatele.
    def ziskej_vstup(self, vyzva, validacni_funkce):
        while True:
            vstup = input(vyzva)
            if validacni_funkce(vstup):
                return vstup
            print(Color.color_text("===================================", Color.BROWN))
            print(Color.color_text("️ ❗️Neplatné údaje. Opakujte.❗️", Color.RED))
            print(Color.color_text("===================================", Color.BROWN))

    # Přidá nového pojištěnce na základě vstupu od uživatele.
    def pridat_pojistence(self):
        jmeno = self.ziskej_vstup("Zadejte jméno: ", Validace.validuj_jmeno)
        prijmeni = self.ziskej_vstup("Zadejte příjmení: ", Validace.validuj_jmeno)
        vek = self.ziskej_vstup("Zadejte věk: ", Validace.validuj_vek)
        telefon = self.ziskej_vstup("Zadejte telefonní číslo: ", Validace.validuj_telefon)
        pojistenec = Pojistenec(jmeno, prijmeni, int(vek), telefon)
        self.evidence.pridat_pojistence(pojistenec)
        print(Color.color_text("===================================", Color.BROWN))
        print(Color.color_text(" ✅Pojištěná osoba byla přidána.✅", Color.GREEN))
        print(Color.color_text("===================================", Color.BROWN))

    # Zobrazí seznam všech pojištěnců.
    def zobraz_vsechny_pojistence(self):
        pojisteni = self.evidence.zobraz_vsechny()
        if pojisteni:
            for pojistenec in pojisteni:
                print(pojistenec)
        else:
            print(Color.color_text("===================================", Color.BROWN))
            print(Color.color_text("    📌Žádná osoba v evidenci.📌", Color.RED))
            print(Color.color_text("===================================", Color.BROWN))

    # Vyhledá a zobrazí pojištěnce podle Jména a Příjmení.
    def najdi_pojistence(self):
        jmeno = self.ziskej_vstup("Zadejte jméno: ", Validace.validuj_jmeno)
        prijmeni = self.ziskej_vstup("Zadejte příjmení: ", Validace.validuj_jmeno)
        pojistenec = self.evidence.najdi_pojistence(jmeno, prijmeni)
        if pojistenec:
            print(pojistenec)
        else:
            print(Color.color_text("===================================", Color.BROWN))
            print(Color.color_text("❓Pojištěná osoba nebyla nalezena.❓", Color.RED))
            print(Color.color_text("===================================", Color.BROWN))
