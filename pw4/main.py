from packageStudent import inputStd, listStd
i=inputStd.inputNumberStd()
a=inputStd.inputStdInfo(i)
listStd.listStd(i, a)

from packageCourse import inputCour, listCour
j=inputCour.inputNumberCour()
b=inputCour.inputCourInfo(j)
listCour.listCour(j, b)

from packageMark import inputMark, listMark
c=inputMark.inputMark(i, j, a, b)
print(c)
listMark.listMark(j, b, c)

#from packageCurses import outPut
