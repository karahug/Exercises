def SumSquareRoot(l):
    r=0
    u=set(l)
    for c in u:
        o=pow(c, .5)
        f=[x for x in l if x==o]
        r+=sum(f)
    return r