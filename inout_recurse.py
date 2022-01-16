def sumin(L:list)->int:
    return sumin(L[1:]) + L[0] if L else 0
    
def sumout(L:list, sum=0)->int:
    return sumout(L[1:],sum+L[0]) if L else sum