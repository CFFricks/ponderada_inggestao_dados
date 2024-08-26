import pytest
import pandas as pd
from data_pipeline.data_processing import process_csv_to_parquet

def test_process_csv_to_parquet(monkeypatch, tmp_path):
    csv_content = """data,cod_vendedor,cod_loja,cod_transacao,quantidade,cod_prod,preco
2021-08-01,1234,LOJ001,TRX001,10,5678,99.99
2021-08-02,1235,LOJ002,TRX002,20,5679,199.99
"""
    csv_path = tmp_path / "test.csv"
    with open(csv_path, 'w') as f:
        f.write(csv_content)

    parquet_file = process_csv_to_parquet(csv_path)
    assert parquet_file.endswith('.parquet')

    df = pd.read_parquet(parquet_file)
    assert len(df) == 2
    assert df['cod_vendedor'].iloc[0] == 1234
    assert df['preco'].iloc[1] == 199.99
