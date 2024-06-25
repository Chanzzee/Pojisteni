from evidence import Evidence
from uzivatelske_rozhrani import UzivatelskeRozhrani
from color import Color


def main():

    """Hlavní menu programu. Uživatel si vybere 1-4 možnost. Pokud zadá jinou možnost funkce else ho upozorní.
    Cykl se opakuje dokud nezadá jednu ze správných možností."""

    evidence = Evidence()
    rozhrani = UzivatelskeRozhrani(evidence)

    # Seznam možností které číselně vybírá uživatel.
    while True:
        print(Color.color_text("===================================", Color.BROWN))
        print(Color.color_text(" 💼EVIDENCE POJISTNÝCH UDÁLOSTÍ💼", Color.RED))
        print(Color.color_text("===================================", Color.BROWN))
        print("💾 1. Přidat pojištěnou osobu")
        print("📄 2. Zobrazit pojištěné osoby")
        print("🔍 3. Vyhledat pojištěnou osobu")
        print("🚪 4. Ukončit program")
        print(Color.color_text("===================================", Color.BROWN))
        print(Color.color_text("       ➡️Zadejte volbu:⬅️         ", Color.BLUE))
        print(Color.color_text("===================================", Color.BROWN))
        print(Color.color_text("   Programmed by Jan Kotas 2024      ", Color.GREY))
        volba = input()


        # Podmínky pro volbu v menu.
        if volba == "1":
            rozhrani.pridat_pojistence()
        elif volba == "2":
            rozhrani.zobraz_vsechny_pojistence()
        elif volba == "3":
            rozhrani.najdi_pojistence()
        elif volba == "4":
            print(Color.color_text("===================================", Color.BROWN))
            print(Color.color_text("       ⏏️Konec programu.⏏️         ", Color.BLUE))
            print(Color.color_text("===================================", Color.BROWN))
            break
        else:
            print(Color.color_text("===================================", Color.BROWN))
            print(Color.color_text("⛔️Neplatná volba! Zkuste to znovu.⛔️", Color.RED))
            print(Color.color_text("===================================", Color.BROWN))


# Zavedení programu z main.
if __name__ == "__main__":
    main()