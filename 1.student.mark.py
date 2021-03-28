#!/usr/bin/env python
# coding: utf-8

# In[15]:


def inputNumberStd():
    n=int(input("How many students are there?"))
    return n

def inputStdInfo(n):
    namel=[]
    idl=[]
    dobl=[]
    for i in range (0,n,1):
        print("Enter info of student ",i+1)
        name=input("Name")
        namel+=[name]
        id=input("Id")
        idl+=[id]
        dob=input("Date of bird")
        dobl+=[dob]
    return [namel,idl,dobl]

def listStd(n,a):
    print("\n\n\nThe list of student info is: ")
    for i in range (n):
        print(a[0][i]+"\t"+a[1][i]+"\t"+a[2][1])

def inputNumberCour():
    n=int(input("How many courses are there?"))
    return n

def inputCourInfo(n):
    idl=[]
    courl=[]
    for i in range (0,n,1):
        print("Enter info of course ",i+1)
        id=input("Id")
        idl+=[id]
        cour=input("Name of cours")
        courl+=[cour]
    return [idl,courl]

def listCour(m,b):
    print("\n\n\nThe list of courses' info is:")
    for i in range (m):
        print(b[0][i]+"\t"+b[1][i])
    

def inputMark(n,m,a,b):
    markl=[]
    print("\n\n\nPlease select a course Id:")
    listCour(m,b)
    cidx=int(input())
    cid=b[0][cidx-1]
    
    print("Enter all student marks:")
    for i in range (n):
        sid=a[0][i]
        mark=int(input("mark of student \t"+sid+a[1][i]+"\t"))
        markl+=[cid,sid,mark]
    print("\n\n\n The marks of students in course "+b[1][cidx-1]+" is:")
    return markl  

i=inputNumberStd()
a=inputStdInfo(i)
listStd(i,a)


j=inputNumberCour()
b=inputCourInfo(j)
listCour(j,b)


c=inputMark(i,j,a,b)
print(c)


# In[ ]:




