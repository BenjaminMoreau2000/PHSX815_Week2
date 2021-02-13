#Edited by Ben Moreau

import math
import numpy as np
from matplotlib import pyplot as plt

''' I used this to get my plot
seedO=302
time =1
N=100#how many times to run the function and get ten numbers back

def randomBinary(seed):
    time=1
    i=0
    n=0
    x=[]
    while(i<10):
        
        n+=1

        a=((seed)**552*(n+1)**233)
        ba=bin(a)
        #print(ba)
        #print(int(ba[2:2+time]))
        if(int(ba[3:3+time])==0):
            time+=1
            #print(bin(a))
            x.append((int(str(a)[6])))
            #print(a)
            #print((int(str(a)[6])))
            i+=1
    return(x)


tot=[]
ww=[]
for i in range(N):
    ww=randomBinary(seedO+(i+1))
    for k in range(len(ww)):
        tot.append(ww[k])

plt.title("Show where each number occurs from the function")
plt.scatter((range(len(tot))),tot)



aa=0
bb=0
cc=0
dd=0
ee=0
ff=0
gg=0
hh=0
ii=0
jj=0
kk=0
for i in range(len(tot)):
    if(tot[i]==0):
        aa+=1
    if(tot[i]==1):
        bb+=1
    if(tot[i]==2):
        cc+=1
    if(tot[i]==3):
        dd+=1
    if(tot[i]==4):
        ee+=1
    if(tot[i]==5):
        ff+=1
    if(tot[i]==6):
        hh+=1
    if(tot[i]==7):
        ii+=1
    if(tot[i]==8):
        jj+=1
    if(tot[i]==9):
        kk+=1
print("amounts of each number after",N*10,"numbers:")
print("0: 1: 2  3: 4: 5: 6: 7  8: 9:")
print(aa,bb,cc,dd,ee,ff,hh,ii,jj,kk)    
'''

plt.show()
#################
# Random class
#################
# class that can generate random numbers
class Random:
    """A random number generator class"""

    # initialization method for Random class
    def __init__(self, seed = 5555):
        self.seed = seed
        self.m_v = np.uint64(4101842887655102017)
        self.m_w = np.uint64(1)
        self.m_u = np.uint64(1)
        
        self.m_u = np.uint64(self.seed) ^ self.m_v
        self.int64()
        self.m_v = self.m_u
        self.int64()
        self.m_w = self.m_v
        self.int64()

    # function returns a random 64 bit integer
    def int64(self):
        with np.errstate(over='ignore'):
            self.m_u = np.uint64(self.m_u * np.uint64(2862933555777941757) + np.uint64(7046029254386353087))
        self.m_v ^= self.m_v >> np.uint64(17)
        self.m_v ^= self.m_v << np.uint64(31)
        self.m_v ^= self.m_v >> np.uint64(8)
        self.m_w = np.uint64(np.uint64(4294957665)*(self.m_w & np.uint64(0xffffffff))) + np.uint64((self.m_w >> np.uint64(32)))
        x = np.uint64(self.m_u ^ (self.m_u << np.uint64(21)))
        x ^= x >> np.uint64(35)
        x ^= x << np.uint64(4)
        with np.errstate(over='ignore'):
            return (x + self.m_v)^self.m_w

    # function returns a random floating point number between (0, 1) (uniform)
    def rand(self):
        return 5.42101086242752217E-20 * self.int64()

    # function returns a random integer (0 or 1) according to a Bernoulli distr.
    def Bernoulli(self, p=0.5):
        if p < 0. or p > 1.:
            return 1
        
        R = self.rand()

        if R < p:
            return 1
        else:
            return 0

    # function returns a random double (0 to infty) according to an exponential distribution
    def Exponential(self, beta=1.):
      # make sure beta is consistent with an exponential
      if beta <= 0.:
        beta = 1.

      R = self.rand();

      while R <= 0.:
        R = self.rand()

      X = -math.log(R)/beta

      return X


    #Return ten random numbers ased on the seed
    
    
    def randomBinary(seed):
        time=1
        i=0
        n=0
        x=[]
        while(i<10):
            
            n+=1

            a=((seed)**552*(n+1)**233)
            ba=bin(a)
            #print(ba)
            #print(int(ba[2:2+time]))
            if(int(ba[3:3+time])==0):
                time+=1
                #print(bin(a))
                x.append((int(str(a)[6])))
                #print(a)
                #print((int(str(a)[6])))
                i+=1
        return(x)
