
# RLS (segurança em nível de linha) com o Power BI

O que significa Row Level Security?

Também conhecido como RLS, abreviação do termo em inglês, a Row Level Security (segurança em nível de linha) no Power BI, em resumo é uma opção de segurança para quando se deseja restringir o acesso a visualização de dados, definindo filtros por determinados usuários.

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

## Antes de iniciar as etapas de aplicação da RLS, vamos analisar um ponto importante:
Se o relatório do Power BI Desktop for publicado em um Workspace no serviço do Power BI, as funções de RLS serão aplicadas aos usuários a quem foi atribuída a função de *VISUALIZADOR* no workspace. Os usuários do workspace com atribuição de Administrador, Membro ou Colaborador têm permissão de edição para o conjunto de dados. Portanto, a RLS não se aplica a eles. Se desejar que a RLS se aplique às pessoas de um workspace, atribua a todas a função de visualizador.

___
## Etapas de Aplicação: 
#### OBSERVAÇÃO: Todos os dados apresentados são fictícios com a única finalidade de instrução.


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





### Apache Spark



_________________________________________________________________________________________________________________________________________________________________________________
#### Eu estou na caminhada para me tornar um Engenheiro de Dados, caso haja algo incorreto ou se você tiver alguma consideração, como elogios ou críticas, por favor me avise!
