import numpy as np
import pandas as pd
import stream as strm
import compute as cmpt
if __name__ == '__main__':
    print("welcome")

df = pd.DataFrame()
def push(series, header = len(df.columns), DF = df):
    if len(DF) == 0:
        df.index = list(range(len(series)))
    DF[header] = pd.Series(series, index = list(range(len(DF))))

