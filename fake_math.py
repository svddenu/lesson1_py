def fake_divide(first_, second_):
    zero_ = 'Ошибка, на ноль делить нельзя'
    if second_ == 0:
        return zero_
    elif first_ % second_ == 0:
        answer_ = first_ / second_
        return round(answer_)
    else:
        answer_ = first_ / second_
        return answer_
