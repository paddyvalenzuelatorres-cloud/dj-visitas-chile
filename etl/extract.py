import pandas as pd
from pathlib import Path

RAW_PATH = Path(__file__).parent.parent / "data/raw/dj_visits_chile_raw.csv"

def extract():
    df = pd.read_csv(RAW_PATH, parse_dates=["event_date"])
    return df

if __name__ == "__main__":
    df = extract()
    print(df)

    # Guardar CSV
    output_path = Path(__file__).parent.parent / "data/extracted.csv"
    df.to_csv(output_path, index=False)
    print(f"Extracted data saved to {output_path}")

