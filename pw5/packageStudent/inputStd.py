def inputNumberStd():
    n=int(input("How many students are there?"))
    return n

def inputStdInfo(n):
    namel=[]
    idl=[]
    dobl=[]
    with open("students.text", "w+") as f:
        for i in range (0,n,1):
            print("Enter info of student ",i+1)
            name=input("Name: ")
            f.write(name+"\t")
            namel+=[name]
            id=input("Id: ")
            f.write(id+"\t")
            idl+=[id]
            dob=input("Date of bird: ")
            f.write(dob+"\n")
            dobl+=[dob]
    return [namel,idl,dobl]
