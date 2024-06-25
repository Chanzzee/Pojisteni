from color import Color
class Pojistenec:

    # Zpracovává pojištěnce se Jménem, Příjmením, Věkem a Telefonním číslem.
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    # Vrací textovou reprezentaci pojištěnce.
    def __str__(self):
        return Color.color_text(f"Jméno a Příjmení: {self.jmeno} {self.prijmeni}, Věk: {self.vek} "
                                f"Telefon: {self.telefon}", Color.BLUE)