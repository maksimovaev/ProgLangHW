import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import uuid
m=[1, -1]
n=int(input('Введите размер матрицы '))
a=np.zeros((n,n))
h=int(input('Введите количество повторов '))
l=0 
per=int(input('Нешахматы(1) или шахматы(2)'))   #Заполнение матрицы 1/-1 или чередованием(шахматный порядок)
for i in range(n):
    for j in range(n):
        a[i, j]=random.choice(m)
print(a)                                   
c=a.copy()
fig=plt.figure(figsize=(8, 8))

frame=[]

for l in range(h):                              #цикл для заполнения матрицы
    print("Петля номер", l)
    b=a.copy()
    summ1=0
    summ2=0
    b[random.randrange(n), random.randrange(n)]*=-1 
    for i in range(n):
        for j in range(n):
            summ1+=a[i, j]*a[i, j-1]+a[i-1, j]*a[i, j]
            summ2+=b[i, j]*b[i, j-1]+b[i-1, j]*b[i, j]
    print('Сумма новой ',summ2)
    if per==1:
        dsumm=-1*(summ2-summ1)
    else:
        dsumm=summ2-summ1
    print('Разницы сумм ',dsumm)                                   
    if dsumm<=0:                                       
        a=b.copy()
    else:
        t=float(1)
        w=np.exp(-dsumm/t)
        p=round(random.uniform(0, 1), 5)
        if w>=p:
            c=a.copy()
        elif w<0:
            a=c.copy()
    frame.append(a)
im=plt.imshow(frame[0], animated=True)
def updatefig(*args):
    global i
    if i<h-1:
        i += 1
    else:
        i=0
    im.set_array(frame[i])
    return im
ani = animation.FuncAnimation(fig, updatefig, frames=h+round(h/10), interval=20,  blit=False)
filename=str(uuid.uuid4())
ani.save('matrix_'+filename+'.gif')
plt.show()
    