g def parse(call):
    call=str(call)
    operation=False
    base=''
    diff=''
    for i in call[::-1]:
        try:
            herring=int(i)
            if operation:
                base+=i
            else:
                diff+=i
        except ValueError:
            if operation:
                back=int(base[::-1])+int(diff[::-1])
                back=str(back)
                if int(back)>0:
                    back='+'+back
                t=call.index(i)
                call=call[:t+1]+back
                #print(i, call)
                parse(call)
            else:
                if i in {'+','-'}:
                    operation=True
                    if i=='-':
                        diff+='-'
    return call

print(parse('7-3+14-26'))

#'7-3+-12'