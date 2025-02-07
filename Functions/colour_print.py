# Some ANSI escape codes for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


def colour_print(text: str, effect: str) -> None:
    """
    Print `text` using the ANSI sequence to change colour, etc.

    :param text: The text to print.
    :param effect: The effect to apply to the text.    
    """
    output_string = "{0}{1}{2}".format(effect, text, RESET)
    print(output_string)


print(RED, "this will be in red")
print("and so is this")
print(GREEN, "this will be in green")
print(BLUE, "this will be in blue")
print(BOLD, "this will be in bold")
print(UNDERLINE, "this will be underlined")
print(REVERSE, "this will be reversed")
print(RESET, "this will be reset")

colour_print("Hello in red", RED)
colour_print("Hello in green", GREEN)
colour_print("Hello in blue", BLUE)
colour_print("Hello in bold", BOLD)
colour_print("Hello in underline", UNDERLINE)
colour_print("Hello in reverse", REVERSE)
