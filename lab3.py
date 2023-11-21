#!/usr/bin/env python
# coding: utf-8

# In[5]:


a=0
for a in range(0,100):
    a+=1
    if a%3 ==0 and a%5==0:
        print(a,":3'e ve 5'e bölünebilir")
    elif a%3 ==0 and a%5!=0:
        print(a,":3'e bölünebilir ama 5'e bölünemez")
    elif a%3!=0 and a%5 ==0:
        print(a,":5'e bölünebilir ama 3'e bölünemez")
    else:
        print(a,":5'e ve 3'e bölünemez")


# In[2]:


N =int(input("Sayı giriniz :"))
tektoplam =0
cifttoplam =0
for i in range(1,N+1):
    if i%2==0:
        cifttoplam+=i
    else:
        tektoplam+=i
    
print(N,"'e kadar olan tek sayıların toplamı:",tektoplam)
print(N,"'e kadar olan çift sayıların toplamı:",cifttoplam)   
    
                     


# In[75]:


for a in range(21):
    if a<10:
        print(a,":10'dan küçük")
    elif a>10:
        print(a,":10'dan büyük")


# In[29]:


#Sayı 
import random
a=random.randint(1,63)
x=int(input("Sayıyı tahmin ediniz :"))

if x==a:
    print("Sayıyı doğru bildiniz")
while x!=a:
    while x<a:
        print("Sayı tahmininizden daha büyük")
        x=int(input("Yeni bir tahminde bulununuz:"))
    while x>a:
        print("Sayı tahmininzden daha küçük")
        x=int(input("Yeni bir tahminde bulununuz:"))
    if x==a:
        print("Sayıyı doğru bildiniz")


# In[15]:


minimum = int(input("Sayı giriniz :"))
for x in range(2,6):
    y=int(input("Bir sayı giriniz :"))
    if minimum>y:
        minimum=y
        
print("En küçük sayı :",minimum)
        
    
        


# In[16]:


#Sayı tahmin oyunu
import random
a= random.randrange(100)
x=int(input("Sayıyı tahmin ediniz :"))
if int(x) == a:
    print("Sayıyı doğru bildiniz")
while int(x) !=a:
    while int(x) < a:
        print("Sayı tahmininizden daha büyük")
        x=int(input("Yeni bir tahminde bulununuz:"))
    while int(x) > a:
        print("Sayı tahmininzden daha küçük")
        x= int(input("Yeni bir tahminde bulununuz:"))
    if int(x)== a:
        print("Sayıyı doğru bildiniz")


# In[23]:


#Fibonacci ilk yirmi terim
a,b=0,1

print("Fibonacci dizisinin ilk yirmi terimi")
for i in range(20):
    a,b=b,a+b
    print(a)



# In[26]:


#10'dan 1'e
print("10'dan 1'e:")
for a in range(10,0,-1):
    print(a)


# In[ ]:




