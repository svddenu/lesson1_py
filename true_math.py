from math import inf

def true_divide(first__, second__):
    if second__ == 0:
        return inf
    elif first__ % second__ == 0:
        answer_ = first__ / second__
        return round(answer_)
    else:
        answer_ = first__ / second__
        return answer_
