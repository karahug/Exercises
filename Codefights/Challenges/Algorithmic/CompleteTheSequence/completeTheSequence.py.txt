def CompletetheSequence(s):
    s=list(map(lambda x: float(x), s.split(',')))
    d,r,g,a=(None,None,True,True)
    for i in range(1,4):
        t=s[i]/s[i-1] if s[i-1] != 0 else 0
        z=s[i]-s[i-1]
        r=r or t
        d=d or z
        if g:
            g=(r==t and t!=0)
            r=t
        if a:
            a=(d==z)
            d=z 
    if a:
        x=s[-1]+d
    elif g:
        x=s[-1]*r
    else:
        x=s[-1]+s[-2]
    return x