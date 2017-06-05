# L-15 MCS 260 : eval()
"""
With eval() we can turn expressions into functions.
"""

def make_fun():
    "user given expression becomes a function"
    expr = input('give an expression in x : ')
    return lambda x : eval(expr)

FUN = make_fun()
ARG = float(input('give a value : '))
VAL = FUN(ARG)
print('the expression evaluated at %f' % ARG)
print('gives %f ' % VAL)

