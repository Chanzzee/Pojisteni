class Validace:
    @staticmethod
    def validuj_jmeno(jmeno):

        #Validuje, zda je jméno a přijmení není neprázdné.

        return jmeno.strip() != ""

    @staticmethod
    def validuj_vek(vek):

        #Validuje, zda je věk kladné celé číslo.

        return vek.isdigit() and int(vek) > 0

    @staticmethod
    def validuj_telefon(telefon):

        #Validuje, zda je telefonní číslo dostatečně dlouhé a obsahuje pouze číslice.

        return telefon.isdigit() and len(telefon) == 9