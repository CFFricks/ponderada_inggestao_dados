from flask import Flask, request, jsonify
from datetime import datetime
from data_pipeline.minio_client import create_bucket_if_not_exists, upload_file, download_file
from data_pipeline.clickhouse_client import execute_sql_script, get_client, insert_dataframe
from data_pipeline.data_processing import process_csv_to_parquet, prepare_dataframe_for_insert
import pandas as pd
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

# Criar bucket se não existir
create_bucket_if_not_exists("vendas-data")

# Executar o script SQL para criar a tabela
execute_sql_script('sql/create_table.sql')

@app.route('/upload', methods=['POST'])
def upload_csv():
    file = request.files['file']
    if not file or not file.filename.endswith('.csv'):
        return jsonify({"error": "Formato de arquivo inválido, por favor envie um arquivo CSV"}), 400

    try:
        # Processar e salvar CSV como Parquet
        filename = process_csv_to_parquet(file)
        upload_file("vendas-data", filename)

        # Ler arquivo Parquet do MinIO
        download_file("vendas-data", filename, f"downloaded_{filename}")
        df_parquet = pd.read_parquet(f"downloaded_{filename}")

        # Preparar e inserir dados no ClickHouse
        df_prepared = prepare_dataframe_for_insert(df_parquet)
        client = get_client()  # Obter o cliente ClickHouse
        insert_dataframe(client, 'vendas_2018', df_prepared)

        return jsonify({"message": "Arquivo CSV recebido, armazenado e processado com sucesso"}), 200
    except Exception as e:
        logging.error(f"Erro ao processar arquivo: {e}")
        return jsonify({"error": "Erro ao processar o arquivo"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
