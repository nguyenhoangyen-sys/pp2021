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
