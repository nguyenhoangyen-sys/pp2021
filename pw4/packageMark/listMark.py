from packageCourse import listCour
def listMark(m, coursel, markl):
    print("\n please select a course Id that you want to list its mark:")
    listCour.listCour(m, coursel)
    cid=int(input())
    print("\n\n\nThe list of mark of this course is:")
    if cid==markl[0]:
        for i in range(len(markl)):
            print (markl[i])
    else:
        print("please try again with another mark list agurement!")

