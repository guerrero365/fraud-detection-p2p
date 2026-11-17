import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, precision_recall_curve, auc

def prepare_modeling_data(df: pd.DataFrame):
    """
    Prepara la matriz de características (X) y la variable objetivo (y)
    excluyendo columnas irrelevantes o de identificación directa.
    """
    # Variables a excluir que no aportan al patrón matemático o son identificadores
    drop_cols = ['step', 'type', 'nameOrig', 'nameDest', 'isFraud', 'isFlaggedFraud']
    
    X = df.drop(columns=[col for col in drop_cols if col in df.columns])
    y = df['isFraud']
    
    return X, y

if __name__ == "__main__":
    print("Módulo de entrenamiento listo para integrarse con el pipeline.")