# Resumo dos Desafios de Segurança da Informação

Este documento apresenta um resumo técnico de dois desafios práticos realizados em laboratório, com foco em **segurança ofensiva**. Ambos os projetos têm finalidade didática, voltados para o estudo de técnicas comuns em ambientes controlados.

---

## Desafio 1 – Phishing com SEToolkit

### Objetivo

Simular um ataque de coleta de credenciais por meio de clonagem de site, utilizando o **SEToolkit** em ambiente virtual.

### Ambiente

- Kali Linux 2024.1 (atacante)
- Windows 10 (vítima)
- VirtualBox com rede Host-Only + NAT

### Etapas Realizadas

- Configuração de rede entre as VMs
- Execução do SEToolkit para clonar a página de login do Google
- Coleta de credenciais via terminal após acesso da vítima à página falsa

### Resultados

- Clonagem da página do Google foi bem-sucedida
- Sites como Facebook e Instagram não funcionaram devido a HSTS/HTTPS
- Windows Defender impediu varreduras com ICMP quando ativo

### Limitações e Alternativas

- SEToolkit é limitado frente a tecnologias de segurança modernas
- Ferramentas recomendadas: **Evilginx2**, **Gophish**, **BeEF**

---

## Desafio 2 – Ransomware Didático com Python

### Objetivo

Simular o funcionamento básico de um ransomware, utilizando **criptografia simétrica** com a biblioteca `cryptography`.

### Estrutura

- Script `encrypt.py` para criptografar arquivos em uma pasta
- Script `decrypter.py` para reverter a criptografia
- Chave única gerada com `Fernet`

### Funcionalidade

- Criptografa arquivos da pasta alvo com AES-128 + HMAC-SHA256
- Garante integridade e autenticidade dos dados
- Scripts ignoram o arquivo de chave durante a operação

### Requisitos

- Python 3.6+
- Instalação da lib:
  ```bash
  pip install cryptography
