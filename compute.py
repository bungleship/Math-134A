import numpy as np
import stream as strm

if __name__ == '__main__':
    print('cmpt.annu_A(P,r,n)')
    print('cmpt.annu_P(A,r,n)')
    print('cmpt.bond_P(P,r,n,F')
    print('cmpt.macaulay(cf,r,year)')
    print('cmpt.npv(series,r)')
    print('cmpt.irr(series)')

def annu_A(P, r, n):
    return P * r * (1 + r)**n / ((1 + r)**n - 1)

def annu_P(A, r, n):
    remaining_balance = (A/r)*(1-1/(1+r)**n)
    return remaining_balance

def bond_P(P,r,n,F):
    return annu_P(A,r,n) + (F / (1+r) ** n)

def macaulay(series, r, year):
    pv = strm.pv(series,r)
    weight = pv / np.sum(pv)
    return np.sum(weight * year)

def npv(series, r = 0):
    return np.sum(strm.pv(series,r))

def irr(series):
    if (series[0] < 0):
        series = np.flip(series)
    # find roots of polynomial
    roots = np.roots(series)
    # choose real, positive root
    c = np.real(roots[(roots >= 0) & (np.iscomplex(roots) == False)])[0]
    # solve for C = 1 / (1+r)
    return (1/c) - 1
