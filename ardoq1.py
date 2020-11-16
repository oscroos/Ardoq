def highest_product(x):
    result = 1
    ints = len(x)

    # dersom vi har mindre enn 3 tall returnerer vi produktet av alle, eventuelt 1 dersom listen er tom
    if ints <= 3:
        for i in x:
            result *= i
        return result

    # ellers fordeler vi elementene på to lister; en med positive heltall og en med negative
    negative = []
    positive = []
    for i in x:
        if i < 0:
            negative.append(i)
        else:
            positive.append(i)
    
    # dersom vi ikke har noen negative tall
    if len(negative) == 0:
        for _ in range(3):
            m = max(positive)
            result *= m
            positive.remove(m)
        return result
    
    # dersom vi ikke har noen positive tall
    if len(positive) == 0:
        for _ in range(3):
            m = max(negative)
            result *= m
            negative.remove(m)
        return result

    # kommer vi hit har vi to muligheter: Det største produktet kan komme av enten
    # 1) to negative tall og et positivt, eller
    # 2) tre positive tall
    opt1 = 1
    if len(negative) == 1:
        opt1 = float('-inf')
    else:
        opt1 *= max(positive)
        opt1 *= min(negative)
        negative.remove(min(negative))
        opt1 *= min(negative)
    
    opt2 = 1
    if len(positive) < 3:
        opt2 = float('-inf')
    else:
        for _ in range(3):
            m = max(positive)
            opt2 *= m
            positive.remove(m)

    return max(opt1, opt2)
