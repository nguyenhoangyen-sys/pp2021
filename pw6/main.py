import zipfile
import pickle

with zipfile.ZipFile('students.dat', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
     my_zip.write("students.text")
     my_zip.write("courses.text")
     my_zip.write("marks.text")

with zipfile.ZipFile('students.dat', 'r') as my_zip1:
    #print(my_zip.namelist())
    my_zip1.extractall("Files")
    my_zip1.extract("marks.text")

with open("Files/students.text","r") as f1:
    students=f1.read()
    print(f"The information of students is: \n{students}")
    pickledStudent=pickle.dumps(students)
    print(f"The information of pickled student is: \n{pickledStudent}")

#with open("Files/courses.text","r") as f2:
    #courses=f2.read()
    #print(f"The information of course is: \n{courses}")
    #pickledCourse=pickle.dumps(courses)
    #print(f"The information of pickled course is: \n{pickledCourse}")

#with open("Files/marks.text","r") as f3:
    #marks=f3.read()
    #print(f"The information of mark is: \n{marks}")
    #pickledMark=pickle.dumps(courses)
    #print(f"The information of pickled course is: \n{pickledMark})

with open("Files/students.text","w") as f4:
    f4.write("Hung \t B2\t 23")
    f4.write("Tam \t B3\t 09")
    f4.write("Tien \t B4\t 19")
with open("Files/students.text","r") as f5:
    students=f5.read()
    print(f"The information of students is: \n{students}")
    UnpickledStudent=pickle.loads(pickledStudent)
    print(f"The information of pickled student is: \n{UnpickledStudent}")



