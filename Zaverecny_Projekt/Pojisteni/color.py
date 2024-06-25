# Třída na různé barvy textu v programu.
class Color:
    RESET = '\033[0m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    BROWN = '\033[33m'
    BLUE = '\033[34m'
    GREY = '\033[37m'
    END = '\033[0m'

    # Funkce vracejicí barvu textu s textem.
    @staticmethod
    def color_text(text, color):
        return f"{color}{text}{Color.RESET}"
