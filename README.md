#  Coffee Sales Forecast (Prophet Baseline)

O modelo foi treinado utilizando o Facebook Prophet para previsão de séries temporais.

Métricas de desempenho no conjunto de teste:

MAE: 255.65

RMSE: 286.11

R²: 0.242

Esses valores indicam que o modelo possui um erro médio de aproximadamente 255 unidades e explica cerca de 24% da variabilidade dos dados observados.
Futuros ajustes de hiperparâmetros e tratamento de outliers podem melhorar o desempenho.


##  Como Rodar

```bash
# Instale as dependências
pip install -r requirements.txt

# Acesse a pasta do notebook
cd notebooks

# Execute o notebook
jupyter notebook coffee_forecast.ipynb

Principais etapas:
1.Limpeza e agregação diária/semanal.
2.Suavização da série (rolling mean).
3.Treinamento Prophet.
4.Avaliação (MAE, RMSE, R²).
