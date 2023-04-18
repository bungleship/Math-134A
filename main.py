import numpy as np
import pandas as pd
import stream as strm
import compute as cmpt
if __name__ == '__main__':
    print("push(series, header, DF)")

df = pd.DataFrame()
def push(series, header = len(df.columns), DF = df):
    if len(DF) == 0:
        DF.index = list(range(len(series)))
    DF[header] = pd.Series(series, index = DF.index)

