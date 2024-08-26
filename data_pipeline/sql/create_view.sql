CREATE VIEW IF NOT EXISTS resumo_vendas_diarias AS
SELECT
    toDate(data) AS dia,
    SUM(quantidade) AS total_quantidade,
    SUM(preco * quantidade) AS valor_total_vendas,
    COUNT(DISTINCT cod_vendedor) AS total_vendedores,
    COUNT(DISTINCT cod_loja) AS total_lojas
FROM vendas_2018
GROUP BY dia
ORDER BY dia
