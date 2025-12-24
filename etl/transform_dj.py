import pandas as pd
from pathlib import Path   # Para manejar rutas de forma segura
from extract import extract

def transform():
    df = extract()
    df = df.sort_values(["dj_name", "event_date"])

    # Calcular días desde la visita anterior
    df["days_since_last_visit"] = df.groupby("dj_name")["event_date"].diff().dt.days

    # Calcular mediana de días entre visitas por DJ
    median_days = df.groupby("dj_name")["days_since_last_visit"].median().reset_index()
    median_days.rename(columns={"days_since_last_visit": "median_days_between_visits"}, inplace=True)

    # Reemplazar NaN por 365 días si hay solo una visita
    median_days["median_days_between_visits"] = median_days["median_days_between_visits"].fillna(365)

    # Unir mediana al dataframe principal
    df = df.merge(median_days, on="dj_name", how="left")

    # Convertir columnas de días a enteros
    df["days_since_last_visit"] = df["days_since_last_visit"].fillna(0).astype(int)
    df["median_days_between_visits"] = df["median_days_between_visits"].astype(int)

    return df

if __name__ == "__main__":
    df_transformed = transform()
    print(df_transformed)

    # Guardar CSV en data/
    output_path = Path(__file__).parent.parent / "data/transformed.csv"
    df_transformed.to_csv(output_path, index=False)
    print(f"Transformed data saved to {output_path}")
