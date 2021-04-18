def inputNumberCour():
    n=int(input("How many courses are there?"))
    return n

def inputCourInfo(n):
    idl=[]
    courl=[]
    with open("courses.text", "w+") as f:
        for i in range (0,n,1):
            print("Enter info of course ",i+1," and course id should be interger starting from 0,1,..")
            id=input("Id: ")
            f.write(id+"\t")
            idl+=[id]
            cour=input("Name of course: ")
            f.write(cour+"\n")
            courl+=[cour]
    return [idl,courl]

