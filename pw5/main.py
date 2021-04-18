

import zipfile

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

with zipfile.ZipFile('students.dat', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
     my_zip.write("students.text")
     my_zip.write("courses.text")
     my_zip.write("marks.text")

with zipfile.ZipFile('students.dat', 'r') as my_zip1:
    #print(my_zip.namelist())
    my_zip1.extractall("Files")
    my_zip1.extract("marks.text")

