import subprocess
import sys
from pathlib import Path

# Función para ejecutar un script Python y mostrar salida en consola
def run_script(script_name):
    script_path = Path(__file__).parent / script_name
    print(f"\n=== Ejecutando {script_name} ===\n")
    result = subprocess.run([sys.executable, str(script_path)], capture_output=False)
    if result.returncode != 0:
        print(f"Error al ejecutar {script_name}")
        sys.exit(1)

if __name__ == "__main__":
    # Ejecutar extract, transform y predict en orden
    run_script("extract.py")
    run_script("transform_dj.py")
    run_script("predict.py")

    print("\n✅ ETL completo, todos los CSVs generados en data/")
