def dobra(lst):
    for i, v in enumerate(lst):
        lst[i] = v * 2
    print(lst)


# Programa Principal
dobra([7, 2, 5, 0, 4])
dobra(['oi'])
