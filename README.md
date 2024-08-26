# Projeto de Ingestão de Dados - Data Pipeline

Este projeto foi desenvolvido como parte de um autoestudo para criar um pacote em Python que realiza a ingestão de dados em um banco de dados ou data lake. O sistema é responsável por processar um arquivo CSV, armazenar o arquivo no MinIO, e inserir os dados processados em uma tabela no banco de dados ClickHouse. O projeto também inclui testes automatizados usando `pytest` para garantir que o sistema funcione corretamente.
## Funcionalidades

- **Ingestão de Dados**: O sistema processa um arquivo CSV, salva o arquivo processado no MinIO, e insere os dados na tabela `vendas_2018` no ClickHouse.
- **Armazenamento em MinIO**: O CSV é convertido em formato Parquet e armazenado no MinIO.
- **Inserção no ClickHouse**: Os dados são inseridos na tabela `vendas_2018` após o processamento.
- **API Flask**: Um endpoint `/upload` é exposto para receber uploads de arquivos CSV.
- **Testes Automatizados**: O projeto inclui testes para verificar a funcionalidade de cada componente do sistema.

## Pré-requisitos

- **Python 3.12+**
- **Poetry** (para gerenciamento de dependências)
- **Docker e Docker Compose** (para subir os serviços MinIO e ClickHouse)


## Configuração

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/CFFricks/ponderada_inggestao_dados
   cd ponderada_inggestao_dados 
   ```
2. **Instale as dependencias:**
   ```bash
    poetry install
    ```
3. **Configure as variáveis de ambiente:**
- Crie um arquivo .env na raiz do projeto.
- Suba os serviços no Docker
   ```bash
    docker-compose up --build
    ```

## Executando a aplicação
1. Inicie o servidor:
   ```bash
    poetry run python app.py

    ```
2. **Faça o upload da base de dados**
O upload tem que ser da tabela de transações de 2018, caso queira subir outra tem que mudar o file_path no arquivo `upload_csv.py`

## Rodar o projeto:
- Inicialize o docker com `docker-compose up --build`
    - se você acessar ao localhost:9000 devera ver a interface do minIO.

- Suba a base de dados que vai utilizar com 
`python upload_csv.py`

- Depois rode o codigo em si com o comando `poetry run python .\app.py`

- Rode os testes com `poetry run pytest` 

