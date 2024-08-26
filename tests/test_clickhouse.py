import pytest
import pandas as pd
from data_pipeline.clickhouse_client import get_client, insert_dataframe

@pytest.fixture(scope="module")
def clickhouse_client():
    return get_client()

def test_insert_dataframe(clickhouse_client):
    df = pd.DataFrame({
        'data': [pd.to_datetime('2024-08-25 10:00:00')],
        'quantidade': [100],
        'preco': [49.99]
    })

    try:
        clickhouse_client.command("""
        CREATE TABLE IF NOT EXISTS test_insert (
            data DateTime,
            quantidade Int64,
            preco Float64
        ) ENGINE = MergeTree()
        ORDER BY data;
        """)

        insert_dataframe(clickhouse_client, 'test_insert', df)
        
        result = clickhouse_client.query("SELECT * FROM test_insert").result_rows
        assert len(result) == 1, "DataFrame insertion failed."
        assert result[0][1] == 100, "Incorrect data inserted for 'quantidade'."
        assert result[0][2] == 49.99, "Incorrect data inserted for 'preco'."
    finally:
        clickhouse_client.command("DROP TABLE IF EXISTS test_insert")
