# GitHub Followers Data

Este projeto coleta dados dos seguidores de um usuário específico do GitHub, processa e salva os dados em um arquivo CSV.

## Requisitos

- Python 3.7+
- PySpark
- Requests

## Configuração

### Variáveis de Ambiente

Defina as seguintes variáveis de ambiente:

- `GITHUB_TOKEN`: Seu token de acesso pessoal do GitHub.
- `USER`: Nome de usuário do GitHub para coletar os seguidores.
- `CSV_OUTPUT`: Caminho para o arquivo de saída CSV.

### Instalação

Instale as dependências necessárias:

```bash
pip install -r requirements.txt
