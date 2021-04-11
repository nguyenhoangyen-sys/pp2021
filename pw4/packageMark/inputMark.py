from packageCourse import listCour
def inputMark(n, m, a, b):
    markl=[]
    print("\n\n\nFor inputing mark, please select a course Id:")
    listCour.listCour(m, b)
    cidx=int(input())
    cid=b[0][cidx-1]
    print("Enter all student marks:")
    for i in range (n):
        sid=a[0][i]
        mark=int(input("mark of student \t"+sid+a[1][i]+"\t"))
        markl+=[cid,sid,mark]
    print("\n\n\n The marks of students in course "+b[1][cidx-1]+" is:")
    return markl
