import numpy as np
import pandas as pd

if __name__ == '__main__':
    print('strm.compound(n,r)')
    print('strm.discount(n,r)')
    print('strm.bond(n,c,p,f)')

def compound(n,r = 0):
    return (1 + r) ** pd.Series(list(range(n)))
def discount(n, r = 0):
    return 1 / compound(n,r)

def pv(series,r=0):
    return series * discount(len(series), r)

def bond(n,c, p = 0, f = 0):
    series = pd.Series(c, index = list(range(n)))
    series[0] = -p
    series.iloc[-1] += f
    return series

