import pyfiglet
import sys

def main():
    txt_to_art()

def txt_to_art():
    # check to make sure there is either 2 or zero arguments
    if arg_checker(3) == False and arg_checker(1) == False:
        sys.exit("Please pass either Zero or 2 arguments.")
    if arg_checker(3):
        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            sys.exit("Unkown option: " + sys.argv[1])

    txt = input("Insert Text: ")

    # Try to print provided with 2 arguments, if 0 arguments are given then "exept" is run
    try:
        print(pyfiglet.figlet_format(txt, font=sys.argv[2]))
    except IndexError:
        print(pyfiglet.figlet_format(txt))
    except pyfiglet.FontNotFound:
        print("Font invalid. ")


# check that proper amounts of args are given
def arg_checker(n):
    if len(sys.argv) == n:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
    