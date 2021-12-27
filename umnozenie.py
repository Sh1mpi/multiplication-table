import time
from random import randint
count = 0
a = []
i= 1
time.perf_counter()
while i <=40:
    st = True
    eror = 0
    m1 = randint(1,9)
    m2 = randint(1,9)
    for j in range(0,len(a),2):
        if (a[j] == m1 and a[j+1] == m2) or (a[j] == m2 and a[j+1] == m1):
            st = False
            break
    if st == False:
        continue
    a.append(m1)
    a.append(m2)
    print('Сколько будет ',m1,'*',m2,' ?')
    ans = int(input())
    if ans == m1*m2:
        count +=1
        print('Правильно, идем дальше (^_^)')
        i+=1
        if time.perf_counter() >120:
            print('у вас осталось:',180-(time.perf_counter()//1),'секунд')
    else:
        print('неверно, правильный ответ',m1*m2,' (>_<)')
        i+=1
        if time.perf_counter() >120:
            print('у вас осталось:',180-(time.perf_counter()//1),'секунд')
    if time.perf_counter() >180:
        print('Вы не успели (>_<)')
        break
if count >= 38:
    print('количество правильных ответов: ',count,'оценка: 5')
if count >= 35 and count < 38:
    print('количество правильных ответов: ',count,'оценка: 4')
if count >= 30 and count < 35:
    print('количество правильных ответов: ',count,'оценка: 3')
if count < 30:
    print('количество правильных ответов: ',count,'оценка: 2')
