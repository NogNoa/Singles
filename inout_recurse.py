def sumin(L:list)->int:
    return L[0] + sumin(L[1:]) if L else 0
    
def sumout(L:list, sum=0)->int:
    if not L:
        return sum
    else:
        return sumout(L[1:],sum+L[0])
