import numpy as np
import stream as strm

if __name__ == '__main__':
    print('annu_A, annu_P')

def annu_A(P, r, n):
    return P * r * (1 + r)**n / ((1 + r)**n - 1)

def annu_P(A, r, n):
    remaining_balance = (A/r)*(1-1/(1+r)**n)
    return remaining_balance

def bond_P(P,r,n,F):
    return annu_P(A,r,n) + (F / (1+r) ** n)

def macaulay(cf, r, year):
    pv = cf * strm.discount(r, length = len(cf))
    price = pv.sum()
    weight = pv / price
    return (weight * year).sum()
