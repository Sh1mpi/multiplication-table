import threading
from random import randint
count = 0
a = []
i= 1
x = True
y = False
n = 0
def gl():
    global x
    if y == False:
        x = False
t = threading.Timer(180.0,gl)
t.start()
def p():
    global y
    if y == False:
        print('у вас осталась 1 минута (^.^)/ ')
tp = threading.Timer(120.0,p)
tp.start()
while i <40:
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
    ans = input()
    if ans.isnumeric() == True:
        if int(ans) == m1*m2:
            count +=1
            print('Правильно (^_^)')
            i+=1
            if x == False:
                print('Вы не успели (>_<)')
                break
        else:
            print('неверно, правильный ответ',m1*m2,' (>_<)')
            i+=1
            if x == False:
                print('Вы не успели (>_<)')
                break
    else:
        print('Вы ввели не число (╯°□°)╯')
        n+=1
        if n >=2:
            i+=1
        continue
if count >= 38:
    print('количество правильных ответов: ',count,'оценка: 5')
    y = True
if count >= 35 and count < 38:
    print('количество правильных ответов: ',count,'оценка: 4')
    y = True
if count >= 30 and count < 35:
    print('количество правильных ответов: ',count,'оценка: 3')
    y = True
if count < 30:
    print('количество правильных ответов: ',count,'оценка: 2')
    y = True
