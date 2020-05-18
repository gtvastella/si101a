# -*- coding: utf-8 -*-
"""final.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Byrtcsg9NlqO6tb8Qlw30Mc5rkX22sNO
"""

#AULA 1

import pandas as pd
import seaborn as sns

n = pd.read_csv("brazil_covid19novo.csv", index_col=2)
#lendo o banco de dados

n.head(27)
#apresentação do banco de dados, mostrando os casos em cada estado, por região, do Brasil por dia.
#o head(27) foi devido aos 26 estados brasileiros mais o distrito federal.
#o banco foi editado para mostrar apenas de 1 de abril até 10 de maio, para maior relevância.

n.loc[n.date == "5/1/2020"].cases.sum()
#aqui é exibido o número total de casos de covid-19 no Brasil até a data de 01/05/2020.

n.loc[n.date == "5/1/2020"].deaths.sum()
#aqui é exibido o número total de mortes por covid-19 no Brasil até a data de 01/05/2020.

n.loc[n.date == "5/10/2020"].deaths.plot.bar()

#aqui é exibido um gráfico de barra que mostra o número de mortes por estado até a data de 10/05/2020.

n.loc[n.date == "5/10/2020"].cases.plot.pie()
#aqui é exibido um gráfico de barras que mostra o número de casos por estado até a data de 10/05/2020.

n.loc[n.date == "5/10/2020"].deaths>=500
#aqui é exibido estados que possuiam 500 mortes ou mais por covid-19 no dia 10/05/2020, sinalizados como true.

n.loc[n.date == "4/22/2020"].plot.scatter(x='region', y='cases')
n.reset_index("state", inplace=True)
#aqui é exibido um gráfico do tipo scatter mostrando os casos totais por região exatamente do dia 22 de abril
#de 2020.

n.loc[n.state=="Amazonas"].loc[n.date=="4/22/2020"].plot.hist()
#aqui é exibido um gráfico do tipo histograma mostrando os casos e mortes amazonenses exatamente no dia 22/04/2020.

#AULA 2

from google.colab import files
n.loc[n.date=="5/10/2020"].loc[:,['deaths','region']].to_csv('teste.csv', index = True)
files.download('teste.csv')
#aqui é filtrado o banco de dados e criado um novo a partir desse, guardando apenas as colunas
#deaths e region (mortes e região) do dia 10/05/2020. Em seguida p arquivo é salvo e baixado para o computador que
#executou o código

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt
tm= tt.groupby(['region']).sum()
tm.head()
#aqui é montado, a partir do método groupby, um novo dataset que soma a morte por regiões com o banco de dados criado anteriormente. Assim, é possível obter o número total de mortes, ainda
#no dia 10/05/2020, porém por região e não por estado.

#AULA 3

lista = n.loc[n.region == "Sudeste"]
lista.head(12)

#aqui mostramos uma lista com os casos de todos os estados da região sudeste nos 3 primeiros dias de abril. note que, como a região é constituída por 3 estados
#então, para cada estado seria necessario exibir 4 linhas e totalizando 12 linhas para 3 dias.

X_lista = lista.loc[: ,  ["cases",	"deaths"] ]
X_lista.head(4)


#aqui fazemos nosso banco restringindo apenas os casos e mortes, sem determinar o estado, já que esse é nosso alvo.

y_lista = lista.state
y_lista.head(4)

#aqui fazemos um banco restringindo apenas os estados, sem determinar mortes e casos, já que isso servirá para  determinar o alvo(estado)

from sklearn.ensemble import ExtraTreesClassifier
from sklearn.model_selection import train_test_split

ETC = ExtraTreesClassifier()
#escolhemos o modelo ExtraTreesClassifier

Xtrain, Xtest, ytrain, ytest = train_test_split(X_lista, y_lista, random_state=74)
#fazemos nosso "treino" baseado nos bancos criados anteriormentes

ETC.fit(Xtrain, ytrain)
y_ETC = ETC.predict(Xtest)
#utilizamos o método de predição

rom sklearn.metrics import accuracy_score

accuracy_score(ytest, y_ETC)*100

#determinamos a precisão final em porcentagem do modelo ETC

y_ETC
#o que foi inferido

ytest
#o "gabarito" do teste