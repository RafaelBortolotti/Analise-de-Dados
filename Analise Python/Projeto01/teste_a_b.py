# -*- coding: utf-8 -*-
"""Teste A/B.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o5BpKXBOZnIyMTMZH1cCjbG3zBTVkl5e
"""

# numpy ajuda a calcular o desvio padrão
# scipy ajuda a calcular o teste t
# matplotlib ajuda a calcular os gráficos

import pandas as pd
import numpy as np
from scipy.stats import t
import matplotlib.pyplot as plt

# Carrega os dados
df = pd.read_excel('/content/Testes de Hipóteses - Média de uma população.xlsx', sheet_name='Teste-t')
df.shape

# Filtro da base de dados onde incia pela linha 14 e matém até coluna 2 onde estão as variaveis
df = df.iloc[14: , 0:2]
df.shape

# Renomeia as colunas
df = df.rename(columns={'Unnamed: 0': 'Nº Amostra', 'Unnamed: 1': 'pH Billings'})
df.shape

df.dtypes

df.info()

df['Nº Amostra'] = df['Nº Amostra'].astype(int)
df['pH Billings'] = df['pH Billings'].astype(float).round(2)
df.shape

# Calculo das distribuições que será usada para o teste de Hipóteses
N = df['Nº Amostra'].count()
Media_PH = df['pH Billings'].mean().round(1)
Desvio_PH = np.std(df['pH Billings']).round(1)

print('Nº de Amostras:', N),
print('Media_PH:', Media_PH),
print('Desvio_PH:', Desvio_PH)

# Distribuição dos dados.
# A amostra de dados precisa estar ao menos próxima a uma distribuição normal.

plt.hist(df['pH Billings'], bins=8,  density=True, color='skyblue', edgecolor='black');

"""# Média de uma população
### Teste-t
-------------------------------------------
### 1º Passo: Definir as hipóteses
### H0: O pH das águas da represa Billings é igual a 6, ou: pH=6
### H1: O pH das águas da represa Billings é inferior a 6, ou: pH<6

-------------------------------------------

### 2º Passo: Calcular a estatística do teste
"""

# Realizar o teste t para a média de uma população

amostra = df['pH Billings']
resultado_t_teste = ttest_1samp(amostra, Media_PH)
resultado_t_teste

"""- A estatística do teste t é próxima de zero, indicando uma diferença muito pequena entre a média da amostra e a média.
- O valor do teste t indica o quanto H0 é plausivel. O valor p é alto, indicando que NÃO há evidências suficientes para rejeitar a hipótese nula de que a média da amostra é igual à média informada.
- Os graus de liberdade são 99, o que é importante para calcular o valor crítico e interpretar a estatística do teste t.

## Recomendação: Não suspender o abastecimento de água
"""