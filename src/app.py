from utils import db_connect
import pandas as pd


def main():
    engine = db_connect()

    df = pd.read_sql("ml_4geeks_airbnb_ny_2019", engine)

    df_clean = df[df.availability_365 > 0]
    print(df_clean.head())


if __name__ == "__main__":
    main()
