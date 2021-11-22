surname = 'maxym'
max_count = 0



for symbol in surname:
    count1 = surname.count(symbol)
    if count1 > max_count:
        max_count = count1

if max_count == 1:
    print('У прізвищі всі літери унікальні')
else: print(max_count)