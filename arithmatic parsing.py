def parse(call):
    def extend(operation,i):
        nonlocal base, diff
        if operation:
            base+=i
        else:
            diff+=i
    call=str(call)
    operation=False
    base=''
    diff=''
    for i in call[::-1]:
        try:
            herring=int(i)
            extend(operation,i)
        except ValueError:
            if i in {'+','-'}:
                extend(operation,i)
                if operation:
                    back=int(base[::-1])+int(diff[::-1])
                    back=str(back)
                    t=call.index(i)
                    call=call[:t]+back
                    call=parse(call)
                else:    
                    operation=True
    return call
print(parse('7-3+14-26'))

#'7-3+-12'
"""
by "extend(operation,i)" the operators I'm relying on
    python's built-in math parsing which isn't really the idea
loop and recursion don't work. we need only recursion.
"""
   