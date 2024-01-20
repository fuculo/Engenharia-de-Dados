# ARQUIVOS DO PROJETO

Todos os arquivos necessários para a criação da imagem e dos contêineres Docker estão presentes neste repositório.

Segue o comando essencial para iniciar o cluster. Após abrir o Prompt de Comando como administrador e navegar até o diretório que contém os arquivos, execute o seguinte comando:

    docker-compose up -d --scale spark-worker=3

Este comando garantirá a inicialização do cluster, com a escala de três instâncias do Spark Worker para um desempenho otimizado.

[Print da execução acima](https://private-user-images.githubusercontent.com/138727304/298300963-834a04d4-d98b-4e60-bc9b-0363d1aedbef.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDU3NzU5OTAsIm5iZiI6MTcwNTc3NTY5MCwicGF0aCI6Ii8xMzg3MjczMDQvMjk4MzAwOTYzLTgzNGEwNGQ0LWQ5OGItNGU2MC1iYzliLTAzNjNkMWFlZGJlZi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMTIwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDEyMFQxODM0NTBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1mMDJjNmM4YzZhYThlMjVkYjU0MWYzMjRjNzdmNWViM2JmYmE4MGNkNDQ2ZWM1MWQyZDhiOWVmMjY5OTVlZDcyJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.PabwMQ6XNMksKZCUKCVrZts-scRlwFaAcosV5ag0zkY{:target="_blank"})


Especificações do meu dispositivo:

  - Processador	Intel(R) Core(TM) i5-8265U CPU @ 1.60GHz   1.80 GHz
  
  - RAM instalada	8,00 GB (utilizável: 7,88 GB)
  
  - Tipo de sistema	Sistema operacional de 64 bits, processador baseado em x64

  - Edição	Windows 11 Home Single Language

___
## OBSERVAÇÃO
Caso a capacidade computacional não fosse o suficiente para executar o projeto, a solução viável seria reduzir a quantidade de Workers para 2 ou até mesmo 1.
