import pandas as pd
import numpy as np

def filter_relevant_transactions(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filtramos únicamente los tipos de transacción donde ocurre fraude (TRANSFER y CASH_OUT),
    descartando el ruido operativo de otros canales.
    """
    print(f"Dimensiones iniciales del dataset: {df.shape[0]:,} filas.")
    filtered_df = df[df['type'].isin(['TRANSFER', 'CASH_OUT'])].copy()
    print(f"Dimensiones tras filtrar canales de riesgo: {filtered_df.shape[0]:,} filas.")
    return filtered_df

def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Creamos características sintéticas basadas en las discrepancias de los saldos bancarios.
    Los defraudadores suelen alterar cuentas alterando la coherencia entre saldos y montos.
    """
    print("Iniciando ingeniería de características (feature engineering)...")
    
    # 1. Error en el balance de la cuenta de origen: 
    # En una transacción legítima, el nuevo saldo debe ser igual al viejo saldo menos el monto.
    df['errorBalanceOrig'] = df['newbalanceOrig'] + df['amount'] - df['oldbalanceOrg']
    
    # 2. Error en el balance de la cuenta de destino:
    # El nuevo saldo del receptor debe ser igual al viejo saldo más el monto.
    df['errorBalanceDest'] = df['oldbalanceDest'] + df['amount'] - df['newbalanceDest']
    
    return df

if __name__ == "__main__":
    # Prueba rápida de ejecución del módulo independiente
    from data_loader import load_raw_data
    
    PATH = "../data/raw/PS_20174392719_1491204439457_log.csv"
    try:
        df_raw = load_raw_data(PATH)
        df_filtered = filter_relevant_transactions(df_raw)
        df_processed = engineer_features(df_filtered)
        
        print("\nPrimeras columnas procesadas con éxito:")
        print(df_processed[['step', 'type', 'amount', 'errorBalanceOrig', 'errorBalanceDest', 'isFraud']].head(3))
    except Exception as e:
        print(f"\n[Aviso]: {e}")