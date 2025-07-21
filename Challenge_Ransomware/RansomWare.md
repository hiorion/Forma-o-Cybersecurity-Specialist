# Challenge Ransomware - Projeto de Criptografia de Arquivos

Este projeto simula o comportamento de um ransomware didático, com foco em criptografia e descriptografia de arquivos em uma pasta alvo, utilizando a biblioteca `cryptography` do Python.

---

## Estrutura do Projeto
````
Desafio_Cyber_security/
│
├── Challenge_Ransomware/
│ ├── encrypt.py # Script de criptografia
│ ├── decrypter.py # Script de descriptografia
│ ├── chave.key # Arquivo com a chave secreta (gerado automaticamente)
│ └── pasta_alvo/ # Pasta onde os arquivos serão criptografados/descriptografados
└── README.md

`````

----

## Requisitos

- Python 3.6 ou superior
- Biblioteca `cryptography`

Instale a biblioteca com:

```bash
pip install cryptography
```

Funcionamento da Criptografia

Este projeto utiliza criptografia simétrica, ou seja, a mesma chave é utilizada tanto para criptografar quanto para descriptografar os arquivos.
Sobre a biblioteca cryptography

A biblioteca cryptography fornece implementações modernas e seguras de algoritmos criptográficos. Neste projeto, usamos o módulo Fernet, que oferece:

    Geração e uso de chave segura

    Criptografia baseada em AES 128 CBC com HMAC SHA256

    Autenticação dos dados criptografados

    Proteção contra alterações e verificações de integridade

Exemplo básico de uso:

from cryptography.fernet import Fernet

# Geração da chave
chave = Fernet.generate_key()

# Instância do Fernet
fernet = Fernet(chave)

# Criptografando
mensagem = b"texto confidencial"
criptografado = fernet.encrypt(mensagem)

# Descriptografando
original = fernet.decrypt(criptografado)

Executando a Criptografia

```python

python Challenge_Ransomware/encrypt.py Challenge_Ransomware/pasta_alvo

```
![Encrypt](/Challenge_Ransomware/prints/encrypt.jpg)


![Encript](/Challenge_Ransomware/prints/encrypted.jpg)

O que o script faz:

    Gera o arquivo chave.key se ainda não existir.

    Criptografa todos os arquivos na pasta indicada (exceto a própria chave).

Executando a Descriptografia

```
python Challenge_Ransomware/decrypter.py Challenge_Ransomware/pasta_alvo

```
![Encrypt](/Challenge_Ransomware/prints/decrypt.jpg)


![Encript](/Challenge_Ransomware/prints/decrypted.jpg)

O que o script faz:

    Lê a chave existente de chave.key.

    Descriptografa todos os arquivos que foram criptografados anteriormente.

Aviso Legal

Este projeto é apenas para fins educacionais. O uso indevido pode ter implicações legais e éticas sérias. Não é recomendado aplicar este código em ambientes reais sem pleno conhecimento dos riscos.
Referências
