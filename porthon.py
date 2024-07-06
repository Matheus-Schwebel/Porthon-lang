import re
import sys
import subprocess
import os

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
    '_principal_' : '__init__',
    'imprimir': 'print',
    'entrada': 'input'
}

libraries = {}

def carregar_libraries():
    try:
        with open('libraries.DATAPTPY', 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    library, version = line.split('>')
                    libraries[library.strip()] = version.strip()
            
    except FileNotFoundError:
        print("Arquivo libraries.DATAPTPY não encontrado. As bibliotecas serão traduzidas por padrão.")

def traduzir_codigo(codigo):
    carregar_libraries()
    # Traduzindo palavras-chave
    for palavra_pt, palavra_en in traducao_palavras_chave.items():
        codigo = re.sub(r'\b' + palavra_pt + r'\b', palavra_en, codigo)
    
    # Traduzindo importações de bibliotecas
    for library, version in libraries.items():
        codigo = re.sub(r'\b' + library + r'\b', f'libraries.{library}', codigo)
    
    return codigo

def executar_codigo(codigo, nome_traducao):
    codigo_traduzido = traduzir_codigo(codigo)
    codigo_traduzido_path = nome_traducao.replace(".ptpy", ".py")
    
    with open(codigo_traduzido_path, "w", encoding="utf-8") as f:
        f.write(codigo_traduzido)
        subprocess.Popen(['start', 'cmd', '/k', f'python {codigo_traduzido_path}'], shell=True)

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

    executar_codigo(codigo_portugues, nome_traducao=name_file)

if __name__ == "__main__":
    main()
