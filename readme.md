# DJ Visitas Chile - ETL y Predicción

Proyecto en Python para construir un dataset histórico de visitas de DJs (house / techno) a Chile, calcular frecuencia de visitas y predecir la próxima fecha de evento.  

---

## **Objetivo**

- Crear un dataset histórico de visitas de DJs a Chile.  
- Calcular cada cuánto tiempo regresan los DJs al país.  
- Predecir la próxima visita de cada DJ.  

---

## **Estructura del proyecto**

dj-visitas-chile/
│
├─ etl/
│ ├─ extract.py # Extracción de datos desde CSV histórico
│ ├─ transform_dj.py # Transformaciones y cálculo de métricas
│ ├─ predict.py # Predicción de próxima visita
│ └─ init.py # Inicializa el paquete
│
├─ data/
│ ├─ raw/
│ │ └─ dj_visits_chile_raw.csv
│ └─ processed/
│ └─ dj_visits_chile_processed.csv
├─ README.md
└─ .gitignore

---

## **Tecnologías**

- Python 3.14  
- Pandas  
- Git / GitHub  

---

## **Instalación y uso**

1. Clonar el repositorio:

```bash
git clone https://github.com/paddyvalenzuelatorres-cloud/dj-visitas-chile.git
cd dj-visitas-chile
Crear y activar entorno virtual:

bash
Copiar código
python -m venv venv
.\venv\Scripts\Activate.ps1   # Windows PowerShell
Instalar dependencias:

bash
Copiar código
pip install pandas
Ejecutar ETL y predicciones:

bash
Copiar código
# Extraer
python etl/extract.py

# Transformar
python etl/transform_dj.py

# Predecir
python etl/predict.py
Resultados
Dataset procesado: data/processed/dj_visits_chile_processed.csv

Predicciones de próxima visita: tabla generada por predict.py

Métricas calculadas: días entre visitas, mediana de días entre visitas

Contribuciones
Proyecto individual para demostración de habilidades de ETL, análisis y predicción.

Cualquier mejora es bienvenida mediante Pull Requests.
