data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calc_all():
    int_sum = 0
    for i in data_structure:
        if isinstance(i, dict):
            for k, v in i.items():
                int_sum += len(k)
                int_sum += v
        elif isinstance(i, list):
            for j in i:
                if isinstance(i, dict):
                    for k, v in i.items():
                        int_sum += len(k)
                        int_sum += v
                int_sum += j
        elif isinstance(i, tuple):
            for a in i:
                if isinstance(a, dict):
                    for k, v in a.items():
                        int_sum += len(k)
                        int_sum += v
                elif isinstance(a, list):
                    for j in a:
                        if isinstance(j, dict):
                            for k, v in j.items():
                                int_sum += len(k)
                                int_sum += v
                        elif isinstance(j, set):
                            for l in j:
                                for s in l:
                                    if isinstance(s, str):
                                        int_sum += len(s)
                                    elif isinstance(s, tuple):
                                        for d in s:
                                            if isinstance(d, str):
                                                int_sum += len(d)
                                            else:
                                                int_sum += d
                                    else:
                                        int_sum += s
                elif isinstance(a, int):
                    int_sum += a
                elif isinstance(a, str):
                    int_sum += len(a)
                elif isinstance(a, tuple):
                    if isinstance(a, str):
                        int_sum += len(a)
                    elif isinstance(a, int):
                        int_sum += a
                    else:
                        continue

        else:
            int_sum += len(i)
    return int_sum

result = calc_all()
print(result)