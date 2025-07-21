import os
import sys
from cryptography.fernet import Fernet

# Lê a chave do arquivo 'chave.key'
def carregar_chave():
    caminho_chave = os.path.join(os.path.dirname(__file__), "chave.key")
    with open(caminho_chave, "rb") as f:
        return f.read()

# Descriptografa todos os arquivos na pasta indicada
def descriptografar_arquivos(pasta_alvo, chave):
    fernet = Fernet(chave)
    arquivos_descriptografados = 0

    for raiz, _, arquivos in os.walk(pasta_alvo):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome == "chave.key" or not os.path.isfile(caminho):
                continue
            try:
                with open(caminho, "rb") as f:
                    dados = f.read()
                original = fernet.decrypt(dados)
                with open(caminho, "wb") as f:
                    f.write(original)
                print(f"[✔] Descriptografado: {caminho}")
                arquivos_descriptografados += 1
            except Exception as e:
                print(f"[✘] ERRO em {caminho}: {e}")

    if arquivos_descriptografados == 0:
        print("[!] Nenhum arquivo foi descriptografado.")
    else:
        print(f"[i] Total de arquivos descriptografados: {arquivos_descriptografados}")

# Execução via terminal
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python decrypter.py <pasta_alvo>")
        sys.exit(1)

    pasta = os.path.abspath(sys.argv[1])

    if not os.path.isdir(pasta):
        print(f"[X] A pasta '{pasta}' não existe.")
        sys.exit(1)

    chave = carregar_chave()
    descriptografar_arquivos(pasta, chave)
