from utils import db_connect
import pandas as pd


def main():
    engine = db_connect()

    df = pd.read_sql("ml_4geeks_airbnb_ny_2019", engine)

    print(df.head())


if __name__ == "__main__":
    main()
