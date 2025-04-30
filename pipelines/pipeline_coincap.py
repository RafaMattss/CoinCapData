import sys
import json
import requests
from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, when, countDistinct, stddev,
    lit
)
from pyspark.sql.types import DoubleType, IntegerType

# Lê o token da API via argumento
if len(sys.argv) < 2:
    raise ValueError("Token da API Coincap não fornecido.")
token = sys.argv[1]

# Cria sessão Spark
spark = SparkSession.builder.appName("CoinCap ETL").getOrCreate()

# Headers da requisição
headers = {"Authorization": f"Bearer {token}"}

# Função de coleta
def coletar_dados(url: str) -> dict:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro na requisição: {response.status_code} - {response.text}")

# URLs da API
url_assets = "https://rest.coincap.io/v3/assets/"
url_mercados = "https://rest.coincap.io/v3/markets/"

# Coleta
dados_assets = coletar_dados(url_assets)
dados_mercados = coletar_dados(url_mercados)

# Criação dos DataFrames
rdd_assets_json = spark.sparkContext.parallelize([json.dumps(row) for row in dados_assets['data']])
rdd_mercados_json = spark.sparkContext.parallelize([json.dumps(row) for row in dados_mercados['data']])

df_assets = spark.read.json(rdd_assets_json)
df_mercados = spark.read.json(rdd_mercados_json)

# Renomeia colunas
df_assets = (df_assets
    .withColumnRenamed("rank", "posicao")
    .withColumnRenamed("symbol", "simbolo")
    .withColumnRenamed("name", "nome")
    .withColumnRenamed("supply", "suprimento")
    .withColumnRenamed("maxSupply", "suprimento_maximo")
    .withColumnRenamed("marketCapUsd", "capitalizacao_mercado_usd")
    .withColumnRenamed("volumeUsd24Hr", "volume_usd_24h")
    .withColumnRenamed("priceUsd", "preco_usd")
    .withColumnRenamed("changePercent24Hr", "variacao_percentual_24h")
    .withColumnRenamed("vwap24Hr", "vwap_24h")
    .withColumnRenamed("explorer", "explorador"))

df_mercados = (df_mercados
    .withColumnRenamed("exchangeId", "id_exchange")
    .withColumnRenamed("baseId", "id_base")
    .withColumnRenamed("quoteId", "id_cotacao")
    .withColumnRenamed("baseSymbol", "simbolo_base")
    .withColumnRenamed("quoteSymbol", "simbolo_cotacao")
    .withColumnRenamed("priceUsd", "preco_usd")
    .withColumnRenamed("volumeUsd24Hr", "volume_usd_24h"))

# Conversão de tipos
df_assets = (df_assets
    .withColumn("preco_usd", col("preco_usd").cast(DoubleType()))
    .withColumn("variacao_percentual_24h", col("variacao_percentual_24h").cast(DoubleType()))
    .withColumn("capitalizacao_mercado_usd", col("capitalizacao_mercado_usd").cast(DoubleType()))
    .withColumn("volume_usd_24h", col("volume_usd_24h").cast(DoubleType()))
    .withColumn("suprimento", col("suprimento").cast(DoubleType()))
    .withColumn("suprimento_maximo", col("suprimento_maximo").cast(DoubleType()))
    .withColumn("posicao", col("posicao").cast(IntegerType()))
)

df_mercados = (df_mercados
    .withColumn("preco_usd", col("preco_usd").cast(DoubleType()))
    .withColumn("volume_usd_24h", col("volume_usd_24h").cast(DoubleType()))
)

# Razão de suprimento
df_assets = df_assets.withColumn(
    "razao_suprimento", col("suprimento") / col("suprimento_maximo")
)

# Categoria por capitalização
df_categorias_capitalizacao = (
    df_assets.select("id", "capitalizacao_mercado_usd")
    .withColumn(
        "categoria_capitalizacao",
        when(col("capitalizacao_mercado_usd") > 1e10, "Grande Capitalizacao")
        .when((col("capitalizacao_mercado_usd") > 1e9), "Media Capitalizacao")
        .otherwise("Pequena Capitalizacao")
    )
)

# Número de exchanges
df_exchanges_por_ativo = (
    df_mercados.groupBy("id_base")
    .agg(countDistinct("id_exchange").alias("numero_exchanges"))
)

# Volatilidade
df_volatilidade_precos = (
    df_mercados.groupBy("id_base")
    .agg(stddev("preco_usd").alias("desvio_padrao_preco"))
)

# Joins finais
df_assets_final = (
    df_assets.alias("assets")
    .join(df_categorias_capitalizacao.alias("categoria"), col("assets.id") == col("categoria.id"), "left")
    .join(df_exchanges_por_ativo.alias("exchanges"), col("assets.id") == col("exchanges.id_base"), "left")
    .join(df_volatilidade_precos.alias("volatilidade"), col("assets.id") == col("volatilidade.id_base"), "left")
)

df_assets_final = df_assets_final.select(
    col("assets.id").alias("id"),
    col("assets.nome").alias("nome"),
    col("assets.simbolo").alias("simbolo"),
    col("assets.posicao").alias("ranking"),
    col("assets.preco_usd").alias("preco_usd"),
    col("assets.variacao_percentual_24h").alias("variacao_percentual_24h"),
    col("assets.capitalizacao_mercado_usd").alias("capitalizacao_mercado_usd"),
    col("assets.volume_usd_24h").alias("volume_24h_usd"),
    col("assets.suprimento").alias("suprimento"),
    col("assets.suprimento_maximo").alias("suprimento_maximo"),
    col("assets.razao_suprimento").alias("razao_suprimento"),
    col("categoria.categoria_capitalizacao").alias("categoria_capitalizacao"),
    col("exchanges.numero_exchanges").alias("numero_exchanges"),
    col("volatilidade.desvio_padrao_preco").alias("desvio_padrao_preco")
)

# Salvamento final
df_assets_final.write.mode("overwrite").format("parquet").saveAsTable("ativos_coincap")
df_mercados.write.mode("overwrite").format("parquet").saveAsTable("mercados_coincap")
