def contador (* num):
    list_num = []
    for i in num:
        list_num.append(i)
    list_num.sort()
    print(f'Os números recebidos foram {list_num} e são ao todo {len(num)} número(s).')
    list_num.sort(reverse=True)
    print(f'Os números recebidos foram {list_num} e são ao todo {len(num)} número(s).')


contador(2, 1, 5, 8)
contador(9)
