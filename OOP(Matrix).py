import numpy as np
import random
import matplotlib.pyplot as plt
import random
import matplotlib.animation as animation
import uuid

class matrix():
    def __init__(self, size, loop):
        self.size = size
        self.loop = loop
        
        m = [1,-1]
        global n
        n=int(self.size)
        global a
        a=np.zeros((n,n))
        for i in range(n):
            for j in range(n):
                a[i,j]=random.choice(m)
        global c
        c=a.copy()
        global d
        d=a.copy()
        print(a)
    
    def summ(self):
        v=0
        for i in range(n):
            for j in range(n):
                v+=a[i,j]*a[i,j-1]
                v+=a[i-1,j]*a[i,j]        
        print(v)
        
    def reset(self):
        global a
        a = d.copy()
        print(a)
    
    def save(self):
        global d
        d = a.copy()
        print(a)
    
    def plot(self):
        plt.clf()
        plt.imshow(a)
        plt.draw()
        plt.show()
    
    def change(self):
        global a
        a[random.randrange(n), random.randrange(n)]*=-1
        print(a)
        
    def chess(self):
        global a
        global c
        for l in range(self.loop):
            print("Петля номер", l)                             
            b=a.copy()
            summ1=0
            summ2=0
            b[random.randrange(n), random.randrange(n)]*=-1 
            for i in range(n):
                for j in range(n):
                    summ1+=a[i, j]*a[i, j-1]+a[i-1, j]*a[i, j]
                    summ2+=b[i, j]*b[i, j-1]+b[i-1, j]*b[i, j]
            dsumm=summ2-summ1
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
        print(a)
        
    def fill(self):
        global a
        global c
        for l in range(self.loop):
            print("Петля номер", l)                             
            b=a.copy()
            summ1=0
            summ2=0
            b[random.randrange(n), random.randrange(n)]*=-1 
            for i in range(n):
                for j in range(n):
                    summ1+=a[i, j]*a[i, j-1]+a[i-1, j]*a[i, j]
                    summ2+=b[i, j]*b[i, j-1]+b[i-1, j]*b[i, j]
            dsumm=-1*(summ2-summ1)
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
        print(a)

class matrixanim(matrix):
    def __init__(self, size, loop, picsize):
        super().__init__( size, loop)
        self.picsize = picsize
        global p
        p=0

    def anichess(self):
        global a
        global c
        h=self.loop
        l=0 
        fig=plt.figure(figsize=(self.picsize, self.picsize))
        frame=[]
        for l in range(h):
            print("Петля номер", l)
            b=a.copy()
            summ1=0
            summ2=0
            b[random.randrange(n), random.randrange(n)]*=-1 
            for i in range(n):
                for j in range(n):
                    summ1+=a[i, j]*a[i, j-1]+a[i-1, j]*a[i, j]
                    summ2+=b[i, j]*b[i, j-1]+b[i-1, j]*b[i, j]
            dsumm=summ2-summ1
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
            global p
            if p<h-1:
                p += 1
            else:
                p=0
            im.set_array(frame[p])
            return im
        ani = animation.FuncAnimation(fig, updatefig, frames=h+round(h/10), interval=20,  blit=False)
        filename=str(uuid.uuid4())
        ani.save('matrix_'+filename+'.gif')
        plt.show()
            
            
        
    def anifill(self):
        global a
        global c
        h=self.loop
        l=0 
        fig=plt.figure(figsize=(self.picsize, self.picsize))
        frame=[]
        for l in range(h):
            print("Петля номер", l)
            b=a.copy()
            summ1=0
            summ2=0
            b[random.randrange(n), random.randrange(n)]*=-1 
            for i in range(n):
                for j in range(n):
                    summ1+=a[i, j]*a[i, j-1]+a[i-1, j]*a[i, j]
                    summ2+=b[i, j]*b[i, j-1]+b[i-1, j]*b[i, j]
            dsumm=-1*(summ2-summ1)
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
            global p
            if p<h-1:
                p += 1
            else:
                p=0
            im.set_array(frame[p])
            return im
        ani = animation.FuncAnimation(fig, updatefig, frames=h+round(h/10), interval=20,  blit=False)
        filename=str(uuid.uuid4())
        ani.save('matrix_'+filename+'.gif')
        plt.show()    