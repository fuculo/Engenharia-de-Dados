# Imports
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.clustering import KMeans
from pyspark.ml import Pipeline
from pyspark.sql.functions import col
from pyspark.sql.types import FloatType

# Inicializa o Spark Session
spark = SparkSession.builder.appName("PipelineFCL").getOrCreate()

# Carrega os dados
# Indica que o formato do arquivo é CSV e indica também que a primeira linha é um cabeçalho 
df = spark.read.format("csv").option("header", "true").load("/opt/spark/data/dataset.csv") # Este é o caminho para o Docker

# Converte as colunas 'idade', 'renda_anual' e 'pontuação_gastos' para FloatType
df = df.withColumn("idade", col("idade").cast(FloatType()))
df = df.withColumn("renda_anual", col("renda_anual").cast(FloatType()))
df = df.withColumn("pontuação_gastos", col("pontuação_gastos").cast(FloatType()))

# Assembla(junta, reune) as colunas 'idade', 'renda_anual' e 'pontuação_gastos' em um único vetor (features)
assembler = VectorAssembler(inputCols = ["idade", "renda_anual", "pontuação_gastos"], outputCol = "features")

# Define o modelo K-means
kmeans = KMeans(featuresCol = "features", k = 3)

# Define o pipeline
# Junção das duas etapas anteriores. Indica que o kmeans será agrupado a feature da etapa assembler
pipeline = Pipeline(stages = [assembler, kmeans])

# Treina o modelo
model = pipeline.fit(df)

# Faz as previsões (atribui os dados a clusters)
predictions = model.transform(df)

# Salva as previsões em um arquivo CSV
predictions.select("prediction").coalesce(1).write.format('com.databricks.spark.csv').mode("overwrite").option('header', 'true').save('/opt/spark/data/resultadop3')

# Para fechar a Spark Session quando a aplicação terminar
spark.stop()
