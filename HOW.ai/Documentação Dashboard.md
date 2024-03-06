# Relatório HOW.ai - DASHBOARD

### Índice:

1 - Importação e conexão ao Power BI Service;

2 - Dados
  *	Modelagem de Dados
  
      1 - Modelagem Relacional ();
  
      2 - Modelagem Dimensional (Dimenções e Fato);
  
      3 - Modelagem Entidade-Relacionamento;
  *	Medidas DAX;

___

# 1 - Importação e Conexão

A partir de uma visão geral, observemos como ficará o fluxo ao final da construção.

Fluxo de Dados Completo
![Fluxo de Dados Completo](https://github.com/fuculo/Engenharia-de-Dados/assets/138727304/e86abfb7-19fa-4456-91c4-387f8aa58307)

Após criar um novo workspace e dar as devidas autorizações de acesso seguimos este passo a passo:
* Novo -> Fluxo de Dados -> Adicionar Novas Tabelas -> API Web



Conectar à Fonte de Dados

![Conectar à Fonte de Dados](https://github.com/fuculo/Engenharia-de-Dados/assets/138727304/8c5e3fe6-6401-40f1-8463-b4ac99b06180)


Parâmetros:
* URL: endpont + índice de acesso = https://how-ai.es.sa-east-1.aws.found.io:PORTA/p_santa_casa_exemplo
* Nome da Conexão: Foi mantido o mesmo da URL
* Gateway de dados: Conexão local
* Tipo de autenticação: Anônimo
* Nível de privacidade: Organizacional

  # 2 - Dados


1 - Utilizando o Power BI Service(Online) foi criado um Fluxo de Dados com base no acesso disponibilizado ao banco de dados do Elastic Search da HOW.ai.
