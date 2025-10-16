#  Coffee Sales Forecast (Prophet Baseline)

Este repositório demonstra um **modelo de previsão simples com Prophet** aplicado à série temporal de vendas de café.

## Estrutura:
simple_prophet_forecast/
    data/         -> dados brutos
    notebooks/    -> notebook principal com o passo a passo
    src/          -> scripts modulares (pré-processamento e métricas)



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
