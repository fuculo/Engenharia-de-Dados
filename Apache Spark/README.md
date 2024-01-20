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
 
## Conclusão

## Anexos e referências

Os conhecimentos aplicados neste projetos tiveram a colaboração da Data Science Academy através do curso de Machine Learning e Inteligência Artificial em Ambientes Distribuídos e também à recente publicação da databricks com o eBook "The Data Engineers Guide to Apache Spark".
