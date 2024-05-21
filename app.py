import random
import ply.lex as lex
import ply.yacc as yacc
from colorama import Fore, Style, init

tokens = ('CAT', 'SPACE', 'DOG', 'COW', 'THEDOG', 'NAME')


def t_CAT(t):
    r'cat'
    return t


def t_COW(t):
    r'cow'
    return t


def t_DOG(t):
    r'dog'
    return t


def t_THEDOG(t):
    r'thedog'
    return t


def t_SPACE(t):
    r'\s+'
    pass


def t_NAME(t):
    r'\w+'
    t.value = t.value.strip()
    return t


def t_error(t):
    print("Invalid token:", t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


def p_program(p):
    '''program : CAT
               | program CAT'''
    pass


def p_error(p):
    global syntax_error
    syntax_error = True


parser = yacc.yacc()


def interpret(code):
    global syntax_error
    syntax_error = False
    parser.parse(code)
    return not syntax_error


def handle_output(token, value):
    if token == 'cat':
        options = [
            Fore.LIGHTRED_EX + "Hello, World!" + Style.RESET_ALL,
            Fore.GREEN + "Hello, Kitty!" + Style.RESET_ALL,
            Fore.YELLOW + "Hello, Kitten!" + Style.RESET_ALL,
            Fore.BLUE + "JUST A CCCCCCAAAAATTTTTTT!!" + Style.RESET_ALL
        ]
        statement = random.choice(options)
        print(statement, end="")
    elif token == 'dog':
        print(Fore.LIGHTCYAN_EX + "Hello, user!" + Style.RESET_ALL, end="")
    elif token == 'cow':
        print(Fore.LIGHTMAGENTA_EX + "Hello, MoO!" + Style.RESET_ALL, end="")
    elif token == 'thedog':
        print(Fore.LIGHTBLACK_EX + f"Hello, {value}!" + Style.RESET_ALL, end="")


def main():
    # Initialize colorama
    init()

    while True:
        input_lines = []
        while True:
            line = input(
                Fore.LIGHTBLUE_EX + "Enter code (or press 'Enter' to output, or enter '!exit' to exit): " + Style.RESET_ALL)
            if line == "!exit":
                print(Fore.RED + "Exit ..." + Style.RESET_ALL, end="")
                exit(0)
            if line == "":
                break
            input_lines.append(line)

        output = ""
        for line in input_lines:
            words = line.split()
            for i, word in enumerate(words):
                if word == 'thedog' and i < len(words) - 1:
                    handle_output(word, words[i + 1])
                else:
                    handle_output(word, None)
                if i < len(words) - 1:
                    output += " "

        print(output)


if __name__ == "__main__":
    main()
