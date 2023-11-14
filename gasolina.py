# código de geração do gráfico´
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

grafico = pd.read_csv("gasolina.csv")

df = pd.DataFrame(grafico)

sns.lineplot(x='dia', y='venda', data=df, marker='o', color='b', label='Preço médio de venda de gasolina em SP')

plt.savefig('gasolina.png')

plt.show()