# JOBS

Embora não seja o real foco do projeto, me sinto obrigado a comentar a respeito da aplicação de Machine Learning.

No arquivo [pipeline.py](https://github.com/fuculo/Engenharia-de-Dados/blob/main/Apache%20Spark/Jobs/pipeline.py) defini o arquivo [dataset.csv](https://github.com/fuculo/Engenharia-de-Dados/blob/main/Apache%20Spark/Jobs/dataset.csv) como parâmetro de entrada,o qual contém dados dos clientes, tais como idade, renda anual e pontuação de gasto.

Durante a execução do pipeline o modelo K-means foi utilizado para segmentar aqueles 10 clientes em 3 grupos distintos.

Como resultado desse processo, o arquivo de saída, [resultado.csv](https://github.com/fuculo/Engenharia-de-Dados/blob/main/Apache%20Spark/Jobs/resultado.csv), contém os índices 0, 1 e 2, representando os grupos aos quais os clientes foram atribuídos.

