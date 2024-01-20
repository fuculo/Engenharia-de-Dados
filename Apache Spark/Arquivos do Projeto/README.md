# ARQUIVOS DO PROJETO

Todos os arquivos necessários para a criação da imagem e dos contêineres Docker estão presentes neste repositório.

Segue o comando essencial para iniciar o cluster. Após abrir o Prompt de Comando como administrador e navegar até o diretório que contém os arquivos, execute o seguinte comando:

    docker-compose up -d --scale spark-worker=3

Este comando garantirá a inicialização do cluster, com a escala de três instâncias do Spark Worker para um desempenho otimizado.

Especificações do meu dispositivo:

  - Processador	Intel(R) Core(TM) i5-8265U CPU @ 1.60GHz   1.80 GHz
  
  - RAM instalada	8,00 GB (utilizável: 7,88 GB)
  
  - Tipo de sistema	Sistema operacional de 64 bits, processador baseado em x64

  - Edição	Windows 11 Home Single Language

___
## OBSERVAÇÃO
Caso a capacidade computacional não fosse o suficiente para executar o projeto, a solução viável seria reduzir a quantidade de Workers para 2 ou até mesmo 1.
