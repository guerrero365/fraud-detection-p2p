# 🛡️ P2P Financial Fraud Detection Pipeline

Pipeline modular de Machine Learning de grado de producción diseñado para la detección de fraude en transacciones de pagos peer-to-peer (P2P), utilizando el dataset sintético **PaySim**. El proyecto prioriza la arquitectura de código limpio, la reproducibilidad y métricas de rendimiento orientadas al negocio financiero.

---

## 🏗️ Arquitectura del Proyecto

El repositorio está estructurado siguiendo las mejores prácticas de ingeniería de software para Ciencia de Datos, separando la lógica de producción (`src/`) de la exploración interactiva (`notebooks/`):

```text
fraud-detection-p2p/
│
├── data/
│   └── raw/                   # Dataset original (PaySim)
│
├── docs/                      # Documentación técnica y guías detalladas
│   └── preprocessing_guide.md # Documentación del preprocesamiento
│
├── notebooks/                 # Cuadernos Jupyter interactivos
│   ├── 01_eda_and_insights.ipynb         # Análisis Exploratorio y Auditoría
│   └── 02_modeling_and_pipeline.ipynb    # Pipeline de Modelado y Evaluación
│
├── src/                       # Código modular de producción
│   ├── data_loader.py         # Módulo de ingesta y carga de datos
│   ├── preprocessing.py       # Modificación, filtrado e ingeniería de features
│   └── train.py               # Estructuras de preparación de datos para ML
│
├── .gitignore                 # Archivos excluidos del control de versiones
├── requirements.txt           # Dependencias del entorno de desarrollo
└── README.md                  # Documentación principal del proyecto