import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)

def process_csv_to_parquet(file_path):
    """
    Processa um arquivo CSV e salva os dados em um arquivo Parquet.
    """
    try:
        df = pd.read_csv(file_path, parse_dates=['data'])
        filename = f"vendas_{datetime.now().strftime('%Y%m%d%H%M%S')}.parquet"
        table = pa.Table.from_pandas(df)
        pq.write_table(table, filename)
        logging.info(f"Dados do CSV processados e salvos no arquivo '{filename}'.")
        return filename
    except Exception as e:
        logging.error(f"Erro ao processar arquivo CSV: {e}")
        raise

def prepare_dataframe_for_insert(df):
    """
    Prepara o DataFrame para inserção no banco de dados.
    """
    try:
        logging.info("DataFrame preparado para inserção no banco de dados.")
        return df
    except Exception as e:
        logging.error(f"Erro ao preparar DataFrame: {e}")
        raise
