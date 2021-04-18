from packageCourse import listCour
def inputMark(n, m, a, b):
    markl=[]
    print("\n\n\nFor inputing mark, please select a course Id:")
    listCour.listCour(m, b)
    cidx=int(input())
    cid=b[0][cidx-1]
    print("Enter all student marks:")
    with open("marks.text", "w+") as f:
        for i in range (n):
            sid=a[0][i]
            mark=int(input("mark of student \t"+sid+a[1][i]+"\t: "))
            f.write(str(mark)+"\n")
            markl+=[int(cid),sid,mark]
    print("\n\n\n The marks of students in course "+b[1][cidx-1]+" \t is: ")
    return markl
