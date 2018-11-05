from stackimpl import Stack

"""
Program to check if parenthesis are balanced
"""
def checkBalanceParen(tmpstr):
    stackobj = Stack()
    openparens = set('([{')
    closeparens = set(')]}')

    matches = set([('(', ')'), ('[', ']'), ('{', '}')])

    for paren in tmpstr:
        if (paren not in openparens) and (paren not in closeparens):
            continue

        if paren in openparens:
            stackobj.push(paren)
        else:
            if stackobj.isEmpty():
                return False

            if (stackobj.pop(), paren) not in matches:
                print("NO match")
                return False


    return True



print(checkBalanceParen('(ab(cd))'))
