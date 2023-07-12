# WEB SCRAPING DA NBA TEMPORADA 2022-2023

Notebook: [NBA 22_23](https://tinyurl.com/bdz6mzv4)

## Objetivo
O objetivo do projeto é demonstrar a técnica de web scraping (raspagem) que apliquei no site https://www.basketball-reference.com/, o qual possui dados estatísticos detalhados sobre a NBA (National Basketball Association), e em seguida, realizar uma análise breve utilizando os dados extraídos.

## Resumo
**Extração de Dados e Análise Exploratória de Dados com PYTHON**

É indiscutível que python é uma das linguagens mais podersas devido à sua simplicidade e à disponibilidade de bibliotecas especializadas.
Realizar a extração dos dados 

Primeiramente, utilizei o módulo requests para realizar uma solicitação HTTP GET à página de interesse.

Para verificar se a requisição foi bem-sucedida, foi feita a impressão (print) do resultado, que mostra o código de status HTTP, como o código 200 para uma resposta bem-sucedida.

Com o objetivo de visualizar os dados de forma organizada e com indentação, utilizei o parseamento do módulo BeautifulSoup.

As buscas no conteúdo da página foram feitam através do método soup.find(), mas também poderíamos ter usado soup.head() ou soup.body() se estivéssemos buscando algo específico dentro das tags <head> e <body>, respectivamente.

Após as buscas, foram selecionadas todas as tags ""div", {"class": "table_container"}".

Para só então, selecionar os cabeçalhos das tabelas e extrair os elementos de cada linha.

## Conclusão

Juntar dois assuntos de interesse torna mais fácil o processo de aprendizagem. Ambos temas tem peso no meu cotidiano, um de modo profissional e outro como hobby. 
Ser capaz de extrair os dados e dar relevância a eles é importante para obter insights significativos e tomar decisões informadas. Isso permite utilizar informações valiosas para identificar padrões, tendências e aplicar conhecimentos de forma estratégica, maximizando o valor dos dados disponíveis.
