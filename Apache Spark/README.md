# PROJETO APACHE SPARK



Este projeto consiste na construção de um fluxo de dados com Apache Spark através da orquestração de containers Docker e arquivos armazenados localmente. 



## Objetivo
O objetivo é demonstrar o funcionamento do fluxo de dados para uma aplicação de Machine Learning.

![image](https://github.com/fuculo/Engenharia-de-Dados/assets/138727304/eec6663e-061c-4f43-a95e-7d2477145fb8)


## Aplicação

Os dados a serem processados estão armazenados localmente em meu computador. 

Utilizando a orquestração de containers Docker, as aplicações do Spark foram encapsuladas em um ambiente isolado. Nesse contexto, um cluster Docker foi configurado através do docker-compose, composto por 1 Driver, 3 Workers e 1 componente History, este último fundamental para monitorar os registros de execução do processo.

- [docker-compose](https://github.com/fuculo/Engenharia-de-Dados/blob/main/Apache%20Spark/Arquivos%20do%20Projeto/docker-compose.yml)

O seguinte dockerfile foi configurado para atender as demandas do projeto. Nele temos a configuração da imagem Docker com a instalção de um Sistema Operacional e seus pacotes, juntamente com variáveis de ambiente, arquivos binários do Spark, preparação do ambiente Python e ajuste de permissões e privilégios.

- [dockerfile](https://github.com/fuculo/Engenharia-de-Dados/blob/main/Apache%20Spark/Arquivos%20do%20Projeto/dockerfile)

Este Dockerfile ainda faz referência a outros 3 arquivos:

1- requeriments.txt
 
2- spark-defaults.conf
 
3- entrypoint.sh 
 

Ao ler o requirements.txt  que consiste em um arquivo de especificação de dependências em Python, listamos os pacotes e suas versões necessárias para executar o código do projeto.


 - [requeriments.txt](https://github.com/fuculo/Engenharia-de-Dados/blob/main/Apache%20Spark/Arquivos%20do%20Projeto/requirements.txt)


Quando o Spark é iniciado, ele procura automaticamente por esse arquivo e aplica as configurações nele contidas. Essas configurações são úteis para personalizar o comportamento do Spark de acordo com os requisitos do projeto.

  - [spark-defaults.conf](https://github.com/fuculo/Engenharia-de-Dados/blob/main/Apache%20Spark/Arquivos%20do%20Projeto/spark-defaults.conf)

Por fim, ainda temos a indicação ao arquivo entrypoint.sh, que por sua vez é utilizado como ponto de entrada para iniciar diferentes componentes do Apache Spark.

   - [entrypoint.sh](https://github.com/fuculo/Engenharia-de-Dados/blob/main/Apache%20Spark/Arquivos%20do%20Projeto/entrypoint.sh)

___
O Apache Spark disnobiliza uma User Interface (UI) para acompanhar o desempenho do cluster, bem como aplicações que estão em andamento ou que já foram concluídas.

 - [User Interface Sem Aplicação](https://private-user-images.githubusercontent.com/138727304/298301065-c96b6bc4-4100-45a0-8f5c-aaff6e4b4ac3.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDU3Nzc3NDQsIm5iZiI6MTcwNTc3NzQ0NCwicGF0aCI6Ii8xMzg3MjczMDQvMjk4MzAxMDY1LWM5NmI2YmM0LTQxMDAtNDVhMC04ZjVjLWFhZmY2ZTRiNGFjMy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMTIwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDEyMFQxOTA0MDRaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1lZGZhOTZhMzUyZWJmNzZjZDYxN2E3N2ZkZjk1OWU0OGZmZDk2MjFlNzdlOGY0ZDA4MDk0ZDBjYmU0MjYzNmU0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.7mB4QqA5Wa69Z7gZ-R6xtp_cq9bwce2Tp5LZqz67GGk)
 
## Conclusão

A conclusão bem-sucedida deste projeto reforça não apenas as habilidades técnicas do engenheiro de dados, mas também a capacidade de integrar múltiplos conhecimentos para alcançar soluções robustas em ambientes complexos de processamento de dados.

## Anexos e referências

Os conhecimentos aplicados neste projetos tiveram a colaboração da [Data Science Academy](https://www.datascienceacademy.com.br/start) através do curso de Machine Learning e Inteligência Artificial em Ambientes Distribuídos e também à recente publicação da databricks com o eBook "The Data Engineers Guide to Apache Spark".
