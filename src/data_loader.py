import pandas as pd
import os

def load_raw_data(file_path: str) -> pd.DataFrame:
    """
    Carga el dataset crudo de transacciones financieras desde la ruta especificada.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"No se encontró el archivo en la ruta: {file_path}")
    
    df = pd.read_csv(file_path)
    print(f"Dataset cargado con éxito. Dimensiones: {df.shape[0]:,} filas y {df.shape[1]} columnas.")
    return df

if __name__ == "__main__":
    # Ajusta el nombre exacto de tu archivo CSV si es necesario
    PATH = "data/raw/PS_20174392719_1491204439457_log.csv"
    try:
        df_sample = load_raw_data(PATH)
        print("\nPrimeras 3 filas del dataset:")
        print(df_sample.head(3))
    except Exception as e:
        print(f"\n[Aviso]: {e}")
        print("Asegúrate de colocar tu archivo CSV descargado de Kaggle dentro de la carpeta 'data/raw/'.")