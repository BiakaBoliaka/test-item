#Вариант 1
#Деление на группы с помощью функций
def test_A():
    print('Это тест А')
    
def test_B():
    print('Это тест В')
    
def division_into_groups(group):
    g = group
    for x in group:
    #num = x
        sum = 0
        while (x != 0):
            sum = sum + x % 10
            x = x // 10        
        if sum > 0:
            print ("Сумма цифр числа равна: ", sum)
            if sum > 25:
                test_A()
            elif sum < 25:
                test_B()
        else:
            continue

id_group = [1234567, 2345678, 12345, 234567]
division_into_groups(id_group)
print()

#Вариант 1.2
#Пользователь может ввести свой ID
while True:
    answer = input('Вы желаете ввести свой ID? (Да/Нет)\n')
    if answer == 'да':
        my_id = input('Введите свой ID: \n')
        if len(my_id)== 5 or len(my_id)== 7:
            try:
                my_id = int(my_id)
                id_group.append(my_id)
                division_into_groups(id_group)
            except:
                print('ID должен состоять только из чисел')
                continue

        else:
            print('Введен неверный размет ID')
            continue
    else:
        break
    

#Вариант 2
#Использование Pandas для структурированных и полуструктурированных данных
import pandas as pd
import numpy as np

#получить данные из csv-файла
table = pd.read_csv('test1.csv')

#устраняем пустые значения в данных
table['id_5'] = table['id_5'].replace(np.nan, 0)
table['id_7'] = table['id_7'].replace(np.nan, 0)

#замена дробных значений на целочисленные
new_table = table.astype({'id_5':'int64', 'id_7': 'int64'})
#print(new_table)
print(new_table['id_5'])
division_into_groups(new_table['id_5'])
print()
division_into_groups(new_table['id_7'])


