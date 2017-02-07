s = re.search

def algebraHomework(problem, answer):
    a = answer.replace(' ', '').split('=')
    v = a[0]
    #substitute to remove ? from problem, substitute for x if necessary
    if '?' in problem:
        problem = problem.replace(v, a[-1]).replace('?', v).replace(' ', '')
    
    #solve for x
    left, right = problem.split( '=')
    while True:
        print('{0} = {1}'.format(left,right))
        result = solver(left, right)
        if not type(result) is tuple:
            return int(result)
        left, right = result

    
def solver(left, right):
    if(s('[A-Za-z]', right)):
        return eval(left)
    elif not s('[+*/-]', left):
        return float(right)  
    a,x,c = (s('\((\(*.*\)*)([+*/-])(.*)\)$', left) or s('(\(*.*\)*)([+*/-])(.*)$', left)).groups()
    inverse = '-' if x == '+' else '+' if x == '-' else '*' if x== '/' else '/'  
    if(s('[A-Za-z]', c)):
        if(s('[/-]', x)):
            return eval(a+x+right)
        return eval(right + inverse + a)
    return a.rstrip(), str(eval(right + inverse + c))
            