import pandas as pd
from pathlib import Path   # <--- Agregar esta línea
from transform_dj import transform

def predict_next_visit():
    df = transform()

    last_visits = df.groupby("dj_name")["event_date"].max().reset_index()
    last_visits = last_visits.merge(
        df[["dj_name","median_days_between_visits"]].drop_duplicates(), on="dj_name"
    )

    last_visits["median_days_between_visits"] = last_visits["median_days_between_visits"].astype(int)
    last_visits["predicted_next_visit"] = last_visits["event_date"] + pd.to_timedelta(last_visits["median_days_between_visits"], unit="D")

    return last_visits[["dj_name","event_date","predicted_next_visit"]]

if __name__ == "__main__":
    predictions = predict_next_visit()
    print(predictions)

    # Guardar CSV
    output_path = Path(__file__).parent.parent / "data/predictions.csv"
    predictions.to_csv(output_path, index=False)
    print(f"Predictions saved to {output_path}")
