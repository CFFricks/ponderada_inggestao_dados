CREATE TABLE IF NOT EXISTS vendas_2018 (
    data DateTime,
    cod_vendedor Int64,
    cod_loja String,
    cod_transacao String,
    quantidade Int64,
    cod_prod Int64,
    preco Float64
) ENGINE = MergeTree()
ORDER BY data;
