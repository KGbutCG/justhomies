# для нахождения пароля для всех чисел
# for n in range(3, 21):
#     result_number = []
#     for a in range(1,21):
#         if a == n :
#             continue
#         for b in range(a + 1,21):
#             if b == n :
#                 continue
#             summa = a + b
#             # print(a, '+', b, '=', a + b)
#             if n % summa == 0:
#                 result_number.append(a)
#                 result_number.append(b)
#             else:
#                 continue
#     print(result_number)


# для нахождения пароля введенного числа
norm = int(input('первая вставка:'))
result_ = []
for a in range(1,21):
    if a == norm :
        continue
    for b in range(a + 1,21):
        if b == norm :
            continue
        summa = a + b
        if norm % summa == 0 :
            result_.append(a)
            result_.append(b)

print(f'Для числа {norm} пароль: {result_}')