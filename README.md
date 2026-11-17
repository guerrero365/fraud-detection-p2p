# 🛡️ P2P Financial Fraud Detection Pipeline

## 📌 Overview (Resumen Ejecutivo)
* **Problema:** Las transacciones financieras digitales P2P son altamente vulnerables al fraude, el cual suele camuflarse entre millones de operaciones legítimas (<0.2% de incidencia real).
* **Objetivo:** Diseñar y desplegar un pipeline de Machine Learning de grado de producción capaz de identificar operaciones fraudulentas en tiempo real con alta precisión y mínima fricción operativa.
* **Tecnologías:** Python, Pandas, Scikit-Learn, XGBoost, Jupyter, Git, PowerShell.
* **Principal Resultado:** Un modelo XGBoost optimizado que alcanzó un **Recall del 99.63%** y una **Precision del 91.15%**, garantizando un blindaje financiero efectivo.

---

## 🏗️ Arquitectura del Proyecto
```text
El repositorio implementa una separación limpia entre la lógica de producción modular y la exploración analítica:
fraud-detection-p2p/
├── data/data/raw/       # Dataset sintético PaySim (excluido del control de versiones)
├── docs/                # Documentación técnica de preprocesamiento
├── notebooks/           # Cuadernos interactivos (EDA y Modelado)
├── src/                 # Código modular de producción (data_loader, preprocessing, train)
├── .gitignore           # Configuración de exclusión de archivos pesados
├── requirements.txt     # Dependencias del proyecto
└── README.md            # Documentación principal
```
### 📊 Metodología y Hallazgos del EDA
```text
Auditoría de Calidad: Verificación de integridad estructural sobre más de 6 millones de
registros del dataset PaySim.

Filtrado Operativo: Se aisló el análisis exclusivamente en los canales de riesgo real
(TRANSFER y CASH_OUT), descartando canales sin incidencia de fraude (PAYMENT, CASH_IN, DEBIT).

Ingeniería de Características: Creación de variables de discrepancia financiera para
delatar inconsistencias en los saldos de origen y destino:

errorBalanceOrig = newbalanceOrig + amount - oldbalanceOrig

errorBalanceDest = oldbalanceDest + amount - newbalanceDest
```
### 🎯 Resultados del Modelo y Justificación de Métricas
```text
En problemas de fraude financiero con desbalanceo extremo, la métrica de Accuracy (Exactitud)
resulta totalmente engañosa (un modelo ingenuo que prediga "todo legítimo" tendría 99.8% de
accuracy pero cero utilidad). Por ello, evaluamos el desempeño bajo estrictas métricas
orientadas a negocio:

Recall (99.63%): De cada 1,000 fraudes reales, el modelo atrapa a 996. Esto mitiga
drásticamente el riesgo de pérdidas financieras por estafas no detectadas.

Precision (91.15%): De cada 100 alertas generadas por el sistema, más de 91 son fraudes
reales. Esto evita inundar al equipo de operaciones con falsas alarmas masivas.

F1-Score (0.9520): Confirma un balance excepcional entre la sensibilidad del modelo y su
precisión predictiva.
```
### 💼 Impacto en el Negocio (Fintech)
```text
Mitigación de Pérdidas Directas: Un alto Recall previene que transacciones maliciosas salgan
de la plataforma, evitando costos de devolución y sanciones regulatorias.

Experiencia de Usuario (UX) Protegida: Una alta Precision evita bloquear las cuentas o
transacciones de clientes legítimos por error, reduciendo la fricción y la frustración del
usuario final en la pasarela de pagos.


Eficiencia Operativa: Minimiza los costos de revisión manual por parte de los analistas
humanos de fraude al reducir el volumen de falsos positivos.
```
