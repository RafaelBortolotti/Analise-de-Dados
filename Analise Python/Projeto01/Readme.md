# Teste de hipóteses (Sendo Finalizado)

# Estudo
Este é um case da escola Predicta Analytics onde foi criado esse caso hipotético com objetivo de transmitir o conhecimento aos alunos
regularmente matriculados no curso de análise de dados para negócios

# Cenário
Uma empresa responsável por realizar testes de qualidade nas águas das represas que abastecem a região
metropolitana da cidade de São Paulo coletou 100 amostras de água da represa Billings. Após realizar a
análise de pH, a empresa obteve os seguintes dados:

- Represa: Billings
- Nº de Amostra: 100
- Média do pH: 5,8
- Desvio do pH: 1,4

Como a Legislação Brasileira define que apenas águas com o pH entre 6 e 9 sejam utilizadas no abastecimento.
surgiu a seguinte pergunta:

**Deve-se suspender o fornecimento de água das regiões abastecidas pela represa Billings?**

# Hipóteses

Para responder a pergunta se deve-se ou não suspender o abastecimento de água, precisamos saber se a média do pH medido a partir das 100 amostras é
estatisticamente igual a 6 ou inferior a 6. A Hipótese Nula sempre apresentará uma igualdade, pois é sob essa condição que calculamos a estatística do 
teste. Já a Hipótese Alternativa sempre apresentará uma desigualdade.

Dessa forma, teremos as seguintes hipóteses nula e alternativa:
- 𝐻0: O pH das águas da represa Billings é igual a 6, ou: pH = 6
- 𝐻1: O pH das águas da represa Billings é inferior a 6, ou: pH < 6


# Conclusão:
- A estatística do teste t é próxima de zero, indicando uma diferença muito pequena entre a média da amostra e a média.
- O valor p é alto, indicando que NÃO há evidências suficientes para rejeitar a hipótese nula de que a média da amostra é igual à média informada.
- Os graus de liberdade são 99, o que é importante para calcular o valor crítico e interpretar a estatística do teste t.

Escala de significância de Fisher:
![image](https://github.com/RafaelBortolotti/Analise-de-Dados/blob/main/Analise%20Python/Projeto01/imagens/Captura%20de%20tela%202024-03-20%20224524.png)

- **Recomendação: Não suspender o abastecimento de água**

# Preparação dos Dados

- Bliblioteca utilizadas
![image](https://github.com/RafaelBortolotti/Analise-de-Dados/assets/48927975/7362f92b-5fba-4dde-a476-6bfa8f74ba39)

- Carrega os dados e conta o número de linhas e colunas
![image](https://github.com/RafaelBortolotti/Analise-de-Dados/assets/48927975/fa89f767-9d0e-49bc-92cc-078bfcd4b8b5)

- Filtragem de linhas e colunas e ao final conta o número de linhas e colunas
![image](https://github.com/RafaelBortolotti/Analise-de-Dados/assets/48927975/753ce19e-e785-4a98-9530-c2e0923de6cb)

- Renomeia as colunas com os nomes corretos
![image](https://github.com/RafaelBortolotti/Analise-de-Dados/assets/48927975/4cd02790-7fed-4620-b5e2-62f635663764)

- Mostra o tipo dos dados
![image](https://github.com/RafaelBortolotti/Analise-de-Dados/assets/48927975/2825bc79-2a91-4954-a789-0052ebf21261)

- Fornece informações mais detalhadas
![image](https://github.com/RafaelBortolotti/Analise-de-Dados/assets/48927975/5ddef273-a33f-4e2b-94da-8346ec7b8d49)

- Altera o formato dos dados 
![image](https://github.com/RafaelBortolotti/Analise-de-Dados/assets/48927975/02482d4e-670d-4827-b817-e31640b36532)

- Calculo da distribuição dos dados que serão utilizadas no teste A/B
![image](https://github.com/RafaelBortolotti/Analise-de-Dados/assets/48927975/9440cd4f-b19d-430f-bacd-01f78b831d76)

- Análise da distribuição dos dados
![image](https://github.com/RafaelBortolotti/Analise-de-Dados/assets/48927975/b85033e6-9ef5-43ba-a683-dcd07858e1ae)

# Teste de Hipóteses

![image](https://github.com/RafaelBortolotti/Analise-de-Dados/assets/48927975/a9b5c747-1efc-48ed-abf1-2bcb0063714d)






