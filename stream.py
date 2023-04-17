import numpy as np
import pandas as pd

if __name__ == '__main__':
    print('irr(series) # decreasing degree')
    print("npv(series, r > 0)")

def compound(r, length):
    return (1 + r) ** pd.Series(list(range(length)))
def discount(r, length):
    return 1 / compound(r, length)

def npv(series, r = 0):
    discount_factor = discount(r, len(series))
    return (series * discount_factor).sum()

def irr(series):
    if (series[0] < 0):
        series = np.flip(series)
    # get the roots of the polynomial
    roots = np.roots(series)
    # get the real positive root
    c = np.real(roots[(roots >= 0)  & (np.iscomplex(roots) == False)])[0]
    # solve for C=1/(1+r)
    return (1/c) - 1
