
# RLS (Segurança em Nível de Linha) com o Power BI

O que significa Row Level Security?

Também conhecido como RLS, abreviação do termo em inglês, a Row Level Security (Segurança em Nível de Linha) no Power BI, em resumo é uma opção de segurança para quando se deseja restringir o acesso a visualização de dados, definindo filtros por determinados usuários.

Os filtros restringem o acesso a dados no nível de linha. A definição dos filtros é feito através de funções DAX.

Para melhor entender, vamos analisar cada etapa para implantação RLS em um relatório do Power BI através de um estudo de caso aplicado à organização de um hospital.

Supondo o cenário em que alguém foi contratado para ser Analista Business Inteligence em um hopistal para a tarefa de construção de um relatório de quantidade de cirurgias realizadas. 

Uma das premissas é que este relatório deverá ser acessado pelos diretores, gestores e médicos, e os dados sejam restringidos conforme organograma abaixo:


| Diretor Geral  |     Gestor      |      Médicos      |
|----------------|-----------------|-------------------|
| Filipe Fúculo  | Wagner Dorneles | Sophia Evans      |
| Filipe Fúculo  | Livia Silva     | Silvane Gonçalves |
| Filipe Fúculo  | Livia Silva     | Cristiano Ribeiro |


* O Diretor pode visualizar tudo referente aos gestores e os médicos;
* Os Gestores podem visualizar tudo a respeito dos seus médicos e não de outros gestores;
* Os médicos podem visulizar tudo a respeito de sí próprio e não de outros médicos.

___

## Antes de iniciar as etapas de aplicação da RLS, vamos analisar dois pontos importantes:
Se o relatório do Power BI Desktop for publicado em um Workspace no serviço do Power BI, as funções de RLS serão aplicadas aos usuários a quem foi atribuída a função de *VISUALIZADOR* no workspace. Os usuários do workspace com atribuição de Administrador, Membro ou Colaborador têm permissão de edição para o conjunto de dados. Portanto, a RLS não se aplica a eles. Se desejar que a RLS se aplique às pessoas de um workspace, atribua a todas a função de visualizador.

Duas etapas são necessárias para configuração de Segurança em Nível de Linha. A primeira aplicada ao Power BI Desktop e a segunda aplicada ao Power BI Online

___
## Conhecendo os dados: 
* Antes de iniciar, analisemos a relação entre as tabelas.
![Print 4 - DER - Dimensão Entidade e Relacionamento](https://github.com/fuculo/Engenharia-de-Dados/assets/138727304/6204afcb-5db5-4010-9d81-cef5f329facd)

* Para o filtro de linha ter coerência e funcionar, a hierarquia deve estar presente na tabela fato.
![Print 5 - Tabela Fato](https://github.com/fuculo/Engenharia-de-Dados/assets/138727304/10b1a1df-c7ae-4299-be4e-792d6d1767f4)
___

## Etapas de Aplicação: 
#### OBSERVAÇÃO: Todos os dados apresentados são fictícios com a única finalidade de instrução e prática.
## Etapa 1:
1. Na guia Modelagem, selecione Gerenciar funções.
   ![Print 1 - Modelagem -_ Gerenciar Funções](https://github.com/fuculo/Engenharia-de-Dados/assets/138727304/ac801e52-1ce7-4161-88f9-3b53b3f04c06)

2. Na janela Gerenciar funções, selecione Criar e forneça um nome para a função.
   ![Print 2 - Gerenciar Funções -_ Criar](https://github.com/fuculo/Engenharia-de-Dados/assets/138727304/44a18329-4519-4e63-bece-c7eae623f244)

3. Em tabelas, selecione a tabela à qual irá aplicar as regras de filtros. O filtro deve ser aplicado na tabela fato.
   ![Print 3 - Criar -_ Funções RLS](https://github.com/fuculo/Engenharia-de-Dados/assets/138727304/4c0e9124-817c-495f-bc90-5b572daf0ce3)


``` dax
'Cirurgias'[id_diretor] IN 
SELECTCOLUMNS(
    FILTER(
        'Direção', 
        'Direção'[email] = USERPRINCIPALNAME()
    ), 
    "id_diretor", 'Direção'[id_diretor]
)
```

### Vamos analisar o código de dentro para fora:
* **FILTER('Direção', 'Direção'[email] = USERPRINCIPALNAME())**: Esta parte da expressão filtra a tabela 'Direção' para encontrar a linha onde o email ('email') é igual ao usuário atualmente autenticado (USERPRINCIPALNAME()). O filtro está sendo aplicado para encontrar o diretor que corresponde ao usuário atual.

* **SELECTCOLUMNS(FILTER(...), "id_diretor", 'Direção'[id_diretor])**: Depois que a filtragem é aplicada, a função SELECTCOLUMNS é usada para selecionar a coluna 'id_diretor' da tabela filtrada. Isso resulta em uma tabela com apenas uma coluna chamada "id_diretor", contendo os IDs dos diretores que correspondem ao usuário atual.

* **'Cirurgias'[id_diretor] IN ...**: Verifica se o ID do diretor associado ao usuário atual está presente na coluna 'id_diretor' da tabela 'Cirurgias' e esta expressão está filtrando as cirurgias para mostrar apenas aquelas associadas ao diretor que corresponde ao usuário atual.
  
* Em resumo, a expressão DAX está filtrando as cirurgias com base no diretor que corresponde ao usuário atualmente autenticado, garantindo que apenas as cirurgias relacionadas a esse diretor sejam exibidas.

* O mesmo foi replicado para os demais níveis hierarquicos, gestores e médicos, sendo alterado somente os parâmetros de tabelas e colunas.

## Etapa 2:
Após a etapa 1 estar devidamente configurada o dashboard deverá ser publicado em um Workspace do Power BI.
Ao publicar dois arquivos são exibidos, relatório e modelo semântico. Clique nos 3 pontos (...) do *MODELO SEMÂNTICO* e selecione *SEGURANÇA*

* Como pode ser observado, as regras foram criadas e o que resta é designar os acessos de acordo com cada uma destas regras.  
![Print 9 - Designando Acessos](https://github.com/fuculo/Engenharia-de-Dados/assets/138727304/3a012cff-8dc3-45e2-b0ba-241a71b7dbaa)

* Finalizada a etapa de designação de acesso conforme imagem abaixo.
![Print 10 - Designando Acessos](https://github.com/fuculo/Engenharia-de-Dados/assets/138727304/a8dffa87-805a-4e0b-bc50-4cf078fc2d47)

* Por fim, o relatório deverá ser compartilhado com os usuários ou com o grupo de usuários para os mesmos terem acesso, pois só configurar a Segurança em Nível de Linha não é o suficiente para visualizar o painel. 
___

## Analisando os Resultados:
1- Visão do Diretor: Consegue visualizar tudo a respeito dos seu gestores e dos seus médicos.
![Print 6 - Visão do Diretor](https://github.com/fuculo/Engenharia-de-Dados/assets/138727304/7a9f2169-15f1-4c9c-a7f6-75adbe747dd3)

2- Visão do Gestor: Consegue visualizar tudo a respeito de sí próprio e dos seus médicos, mas não dos demais gestores.
![Print 7 - Visão do Gestor](https://github.com/fuculo/Engenharia-de-Dados/assets/138727304/1b44832c-02da-412d-976e-9aa7f54a27bf)

3- Visão do Médico: Consegue visualizar tudo a respeito de sí próprio, mas não dos demais médicos 
![Print 8 - Visão do Médico](https://github.com/fuculo/Engenharia-de-Dados/assets/138727304/2b4d11c3-6ca2-4de8-8eba-c38ede37cd69)

___

## Conclusão:
O dataset apresentado contém poucos registros, porém, isso não se torna impeditivo para escalar a mesma solução para um grande conjunto de dados. 

A aplicação de RLS às organizações permite controlar com precisão quem pode ver quais dados, garantindo conformidade com regulamentos de privacidade e protegendo informações confidenciais contra acesso não autorizado.

Essa funcionalidade é fundamental para criar relatórios e painéis confiáveis que oferecem insights relevantes sem comprometer a segurança dos dados.
