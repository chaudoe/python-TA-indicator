def pivot(pivot_high, pivot_low, pivot_close):
    pp = ((pivot_high + pivot_low + pivot_close) / 3)
    r1 = (2 * pp) - pivot_low
    r2 = (pp + pivot_high - pivot_low)
    r3 = (pivot_high + 2*(pp - pivot_low))
    s1 = (2*pp) - pivot_high
    s2 = pp - pivot_high + pivot_low
    s3 = pivot_low - 2*(pivot_high - pp)
    return pp, r1, r2, r3, s1, s2, s3
    #fc_values = [pp, r1, r2, r3, s1, s2, s3]
    #return fc_values

def pivotC(pivot_high, pivot_low, pivot_close):
    r3 = pivot_close + (pivot_high - pivot_low) * 1.1/4
    r2 = pivot_close + (pivot_high - pivot_low) * 1.1/6
    r1 = pivot_close + (pivot_high - pivot_low) * 1.1/12
    s1 = pivot_close - (pivot_high - pivot_low) * 1.1/12
    s2 = pivot_close - (pivot_high - pivot_low) * 1.1/6
    s3 = pivot_close - (pivot_high - pivot_low) * 1.1/4
    return r1, r2, r3, s1, s2, s3
