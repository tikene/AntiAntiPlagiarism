from random import randint
from colorama import init, Fore, Style
import time
import os

init(convert=True)
init(autoreset=True)

bright = Style.BRIGHT
dim = Style.DIM
red = Fore.RED + bright + dim
green = Fore.GREEN + bright + dim
cyan = Fore.CYAN + bright + dim
yellow = Fore.LIGHTYELLOW_EX + bright + dim
blue = Fore.BLUE + bright + dim
white = Fore.WHITE + bright + dim
magenta = Fore.MAGENTA + bright + dim

FILE_IN = "aap_in.txt"
FILE_OUT = "aap_out.txt"
SINGLE_CHAR = False # Enable if you have a word limit and don't want aap to use many chars

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def main():
    cls()
    mod_str = ""
    input_text = input("\n\n > Introduce a text or press enter: ")

    if input_text == "":
        if not os.path.exists(FILE_IN):
            print(red + "{} could not be found, creating\n".format(FILE_IN))
            open(FILE_IN, "w+", encoding="utf-8").close()
            input()
            main()

        input_file = open(FILE_IN, "r", encoding="utf-8")
        input_text = input_file.read()
        input_file.close()

        if input_text == "":
            print(red + "{} file cannot be empty\n".format(FILE_IN))
            input()
            main()


    for word in input_text.split():

        if SINGLE_CHAR:
            middle = int(len(word)/2)
            mod_str += word[:middle] + "‎" + word[middle:] + " "
            continue

        for char in word:
            mod_str += char + "‎"
        mod_str += " "

    f = open(FILE_OUT, "w", encoding="utf-8")
    f.write(mod_str)
    f.close()
    print(green + "\nResult saved into: {}".format(FILE_OUT))
    print(cyan + "\n{}".format(mod_str))


    input()
    main()

main()
