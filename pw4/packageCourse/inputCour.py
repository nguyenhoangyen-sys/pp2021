def inputNumberCour():
    n=int(input("How many courses are there?"))
    return n

def inputCourInfo(n):
    idl=[]
    courl=[]
    for i in range (0,n,1):
        print("Enter info of course ",i+1," and course id should be interger starting from 0,1,..")
        id=input("Id")
        idl+=[id]
        cour=input("Name of cours")
        courl+=[cour]
    return [idl,courl]

