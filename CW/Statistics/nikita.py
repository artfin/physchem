import numpy as np
import math as m
import matplotlib.pyplot as plt

def vib_int_energy(t):
    omega=2169.
    hc=6.63*10**(-34)*3*10**10
    k=1.38*10**(-23)
    alpha=hc*omega/(k*t)
#    print(str(alpha))
    E=hc*omega*m.exp(-alpha)/(1.-m.exp(-alpha))
    return E

def vib_capacity(t):
    omega=2169.
    hc=6.63*10**(-34)*3*10**10
    k=1.38*10**(-23)
    alpha=hc*omega/(k*t)
    c_v=(hc*omega)**2/(k*t**2)*m.exp(-alpha)/(1-m.exp(-alpha))**2
    return c_v

def rot_summ(t):
    B=1.93*3*6.63*10**-24
    k=1.38*10**(-23)
    Q=0.
    Q1=2.
    alpha=B/k
    for j in range(100):
        if abs(Q-Q1)>=10**-5:
            Q1=Q
            g=2*j+1
            Q+=g*m.exp(-alpha*j*(j+1)/t)
    return Q
      
    
def rot_capacity(y,y0,x,x0):
    return (y-y0)/(x-x0)
            
T=np.linspace(10,100000,500)
Uvib=list()
Cvib=list()
Summrot=list()
k=1.38*10**(-23)
for t in T:
    Uvib.append(vib_int_energy(t))
    Cvib.append(vib_capacity(t)/k)
    Summrot.append(m.log(rot_summ(t)))

Urot=list()
for i in range(len(T)):
    if i<(len(T)-1): Urot.append(k*T[i]**2*rot_capacity(Summrot[i+1],Summrot[i],T[i+1],T[i]))
    else: Urot.append(Urot[i-1])
Crot=list()
for i in range(len(T)):
    if i<(len(T)-1): Crot.append(rot_capacity(Urot[i+1],Urot[i],T[i+1],T[i])/k)
    else: Crot.append(Crot[i-1]/k)
Ctrans=list()
for t in T:
    Ctrans.append(3/2)
C=list()
for v,r,t in zip(Cvib,Crot,Ctrans):
    C.append(v+r+t)
plt.plot(T,Crot,'-',T,Cvib,'-',T,Ctrans,'-',T,C,'-')