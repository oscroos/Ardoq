def highest_product(x):
    c = x.copy() # For å unngå å endre listen 
    result = 1
    n = min(3, len(x)) # Antar her at dersom listen har mindre enn 3 elementer så tar vi produktet av alle elementene, og dersom listen er tom returnerer vi 1
    for _ in range(n):
        m = max(c)
        res *= m
        c.remove(m)
    return result

