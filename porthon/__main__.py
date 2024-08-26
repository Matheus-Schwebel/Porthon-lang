"""
Main
----

Command line interface.
"""
import argparse
import tempfile
import os
from . import __version__ as version, interpreter
import keyboard
import sys

try:
    input = raw_input
except NameError:
    pass

def print_centered(text):
    # Calcula o espaço necessário para centralizar o texto
    padding = 10

    # Imprime o texto com o padding
    print(' ' * padding + text)

def parse_args():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-v', '--verbose', action='store_true')
    argparser.add_argument('file', nargs='?')
    return argparser.parse_args()

def interpret_file(path, verbose=False):
    with open(path) as f:
        print(interpreter.evaluate(f.read(), verbose=verbose))

def repl():
    print_centered("\033[34m\033[1mA B R V A L G\033[0m")    # Azul
    print("\033[33mAbrvalg {}.\033[0m \033[32mPress \033[1mCtrl+C\033[0m\033[32m to exit.\033[0m".format(version)) # Amarelo
    continurepl()

def continurepl():
    env = interpreter.create_global_env()
    buf = ''
    try:
        while True:
            inp = input('>>> ' if not buf else '')
            if inp == '':
                if buf:
                    # Cria um arquivo temporário
                    with tempfile.NamedTemporaryFile(delete=False, suffix='.abr') as tmpfile:
                        tmpfile.write(buf.encode())
                        tmpfile_path = tmpfile.name
                    
                    # Executa o arquivo temporário
                    interpret_file(tmpfile_path)

                    buf = ''
            elif inp == 'sair':
                keyboard.press_and_release('ctrl+c')
            else:
                buf += '\n' + inp
                with tempfile.NamedTemporaryFile(delete=False, suffix='.abr') as tmpfile:
                        tmpfile.write(buf.encode())
                        tmpfile_path = tmpfile.name
                    
                    # Executa o arquivo temporário
                        interpret_file(tmpfile_path)

                                        
                        buf = ''
    except KeyboardInterrupt:
        print("\nExiting ABRVALG INTERACTIVE. Goodbye!")

def main():
    args = parse_args()
    if args.file:
        interpret_file(args.file, args.verbose)
    else:
        repl()

if __name__ == '__main__':
    main()
