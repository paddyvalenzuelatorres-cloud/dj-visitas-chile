import pandas as pd
from pathlib import Path   # Para manejar rutas de forma segura
from transform_dj import transform

def predict_next_visit():
    df = transform()

    # Última fecha de visita por DJ
    last_visits = df.groupby("dj_name")["event_date"].max().reset_index()

    # Obtener mediana de días entre visitas
    median_days = df[["dj_name", "median_days_between_visits"]].drop_duplicates()
    median_days["median_days_between_visits"] = median_days["median_days_between_visits"].astype(int)

    # Unir medianas al dataframe de última visita
    last_visits = last_visits.merge(median_days, on="dj_name")

    # Calcular próxima visita usando enteros
    last_visits["predicted_next_visit"] = last_visits["event_date"] + pd.to_timedelta(last_visits["median_days_between_visits"], unit="D")

    return last_visits[["dj_name", "event_date", "predicted_next_visit"]]

if __name__ == "__main__":
    predictions = predict_next_visit()
    print(predictions)

    # Guardar CSV con predicciones
    output_path = Path(__file__).parent.parent / "data/predictions.csv"
    predictions.to_csv(output_path, index=False)
    print(f"Predictions saved to {output_path}")