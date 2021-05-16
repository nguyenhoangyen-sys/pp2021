import threading
import time
import zipfile
import pickle


class ThreadingExample(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, interval=1):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        while True:
            # Do something
            with open("Files/students.text","r") as f1:
                students=f1.read()
                print(f"The information of students is: \n{students}")
                pickledStudent=pickle.dumps(students)
                print(f"The information of pickled student is: \n{pickledStudent}")

            with open("Files/courses.text","r") as f2:
                courses=f2.read()
                print(f"The information of course is: \n{courses}")
                pickledCourse=pickle.dumps(courses)
                print(f"The information of pickled course is: \n{pickledCourse}")

            with open("Files/marks.text","r") as f3:
                marks=f3.read()
                print(f"The information of mark is: \n{marks}")
                pickledMark=pickle.dumps(marks)
                print(f"The information of pickled marks is: \n{pickledMark}")

            time.sleep(self.interval)

example = ThreadingExample()
with zipfile.ZipFile('students.dat', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
     my_zip.write("students.text")
     my_zip.write("courses.text")
     my_zip.write("marks.text")

with zipfile.ZipFile('students.dat', 'r') as my_zip1:
    my_zip1.extractall("Files")
    my_zip1.extract("marks.text")

#time.sleep(3)
#print('Checkpoint)
#time.sleep(2)
#print('Bye')
