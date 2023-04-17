import numpy as np
import pandas as pd
import stream as strm
import compute as cmpt
if __name__ == '__main__':
    print("welcome")

df = pd.DataFrame()
def push(series, header = len(df.columns), DataFrame = df):
    df[header] = pd.Series(series)

# push([100, 110, 120, 130, 140])
# push([120, 115, 110, 105, 100])
# npv()
