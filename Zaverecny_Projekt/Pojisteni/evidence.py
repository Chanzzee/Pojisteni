from color import Color


# Inicializuje prázdnou evidenci pojištěných osob.
class Evidence:
    def __init__(self, pojisteni=[]):
        self.pojisteni = pojisteni

    # Přidá pojištěnce do evidence.
    def pridat_pojistence(self, pojistenec):
        self.pojisteni.append(pojistenec)

    # Vrací seznam všech pojištěnců v evidenci.
    def zobraz_vsechny(self):
        print(Color.color_text("===================================", Color.BROWN))
        print(Color.color_text("   📑Seznam pojištěných osob📑", Color.RED))
        print(Color.color_text("===================================", Color.BROWN))
        return self.pojisteni

    # Vyhledá pojištěnce podle jména a příjmení.
    def najdi_pojistence(self, jmeno, prijmeni):
        for pojistenec in self.pojisteni:
            if pojistenec.jmeno == jmeno and pojistenec.prijmeni == prijmeni:
                return pojistenec
        return None
