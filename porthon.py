import re
import sys
import subprocess

# Dicionário de tradução
traducao_palavras_chave = {
    'importar': 'import',
    'retornar': 'return',
    'se': 'if',
    'senao': 'else',
    'sense': 'elif',
    'para': 'for',
    'enquanto': 'while',
    'verdadeiro': 'True',
    'falso': 'False',
    'nenhum': 'None',
    'func': 'def',
    'classe': 'class',
    'tente': 'try',
    'exceto': 'except',
    'finalmente': 'finally',
    'passar': 'pass',
    'quebrar': 'break',
    'continuar': 'continue',
    'como': 'as',
    'com': 'with',
    'levantar': 'raise',
    'assegurar': 'assert',
    'de': 'from',
    'imprimir': 'print',
    'entrada': 'input',
    'janelas': 'tkinter',
    'principal': 'mainloop',
    'titulo': 'title',
    '#:' : '#'
}

def traduzir_codigo(codigo):
    for palavra_pt, palavra_en in traducao_palavras_chave.items():
        codigo = re.sub(r'\b' + palavra_pt + r'\b', palavra_en, codigo)
    return codigo

def executar_codigo(codigo):
    codigo_traduzido = traduzir_codigo(codigo)
    with open("codigo_traduzido.py", "w", encoding="utf-8") as f:
        f.write(codigo_traduzido)
    
    if 'janelas' in codigo:
        subprocess.run(['python', 'codigo_traduzido.py'], shell=True)
    else:
        subprocess.run(['start', 'cmd', '/k', 'python codigo_traduzido.py'], shell=True)

def main():
    if len(sys.argv) < 2:
        print("Uso: py main.py <nome_do_arquivo.ptpy>")
        sys.exit(1)

    name_file = sys.argv[1]

    try:
        with open(name_file, "r", encoding="utf-8") as file:
            codigo_portugues = file.read()
    except FileNotFoundError:
        print(f"Arquivo {name_file} não encontrado.")
        sys.exit(1)

    codigo_traduzido = traduzir_codigo(codigo_portugues)

    with open("codigo_traduzido.py", "w", encoding="utf-8") as f:
        f.write(codigo_traduzido)

    subprocess.Popen(['start', 'cmd', '/k', 'python codigo_traduzido.py'], shell=True)

if __name__ == "__main__":
    main()
