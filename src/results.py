import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def evaluate_predictions(y_true, y_pred):
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    return {"MAE": mae, "RMSE": rmse, "R2": r2}

def plot_forecast(df_weekly, forecast):
    plt.figure(figsize=(10, 5))
    plt.plot(df_weekly['ds'], df_weekly['y'], label='Original', alpha=0.4)
    plt.plot(df_weekly['ds'], df_weekly['y_smooth'], label='Suavizada (3 sem)', color='red')
    plt.plot(forecast['ds'], forecast['yhat'], label='Prevista', color='blue')
    plt.legend()
    plt.grid()
    plt.show()
