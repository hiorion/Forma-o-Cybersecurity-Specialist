import os
import sys
from cryptography.fernet import Fernet

# Gera a chave e salva no arquivo chave.key
def gerar_chave():
    caminho_chave = os.path.join(os.path.dirname(__file__), "chave.key")
    chave = Fernet.generate_key()
    with open(caminho_chave, "wb") as f:
        f.write(chave)
    return chave

# Lê a chave de chave.key
def carregar_chave():
    caminho_chave = os.path.join(os.path.dirname(__file__), "chave.key")
    with open(caminho_chave, "rb") as f:
        return f.read()

# Criptografa todos os arquivos da pasta
def criptografar_arquivos(pasta_alvo, chave):
    fernet = Fernet(chave)
    arquivos_criptografados = 0

    for raiz, _, arquivos in os.walk(pasta_alvo):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)

            if nome == "chave.key" or not os.path.isfile(caminho):
                continue

            with open(caminho, "rb") as f:
                dados = f.read()

            criptografado = fernet.encrypt(dados)

            with open(caminho, "wb") as f:
                f.write(criptografado)

            print(f"[✔] Criptografado: {caminho}")
            arquivos_criptografados += 1

    if arquivos_criptografados == 0:
        print("[!] Nenhum arquivo foi criptografado.")
    else:
        print(f"[i] Total de arquivos criptografados: {arquivos_criptografados}")

# Execução principal
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python encrypt.py <pasta_alvo>")
        sys.exit(1)

    # Caminho absoluto da pasta passada
    pasta = os.path.abspath(sys.argv[1])

    if not os.path.isdir(pasta):
        print(f"[X] A pasta '{pasta}' não existe.")
        sys.exit(1)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    chave_path = os.path.join(script_dir, "chave.key")

    if os.path.exists(chave_path):
        chave = carregar_chave()
        print("[i] Usando chave existente.")
    else:
        chave = gerar_chave()
        print("[i] Nova chave gerada e salva como chave.key.")

    criptografar_arquivos(pasta, chave)

