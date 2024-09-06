timur = 'ящерица'
ruslan = 'камень'

variant = ['камень', 'ящерица', 'Спок', 'ножницы', 'бумага']
ishod = ['Тимур', 'Руслан']
if timur == ruslan:
    print('ничья')
else:
    if variant.index(timur) > variant.index(ruslan) and (variant.index(timur) - variant.index(ruslan)) % 2 == 0:
        print(ishod[0])
    elif variant.index(timur) < variant.index(ruslan) and (variant.index(timur) - variant.index(ruslan)) % 2 == 0:
        print(ishod[1])
    elif variant.index(timur) > variant.index(ruslan) and (variant.index(timur) - variant.index(ruslan)) % 2 != 0:
        print(ishod[1])
    elif variant.index(timur) < variant.index(ruslan) and (variant.index(timur) - variant.index(ruslan)) % 2 != 0:
        print(ishod[0])