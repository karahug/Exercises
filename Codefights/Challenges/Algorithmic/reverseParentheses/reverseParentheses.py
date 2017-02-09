def g(s):
    if'('not in s:return s
    l,r=re.search(r'\([^()]*\)',s).span();return g(s[:l]+s[r-2:l:-1]+s[r:])
def reverseParentheses(s):return g(s)