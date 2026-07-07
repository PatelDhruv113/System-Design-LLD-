class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self):
        print(f"{self.name} is teaching")


class Student:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher   # Association

    def study(self):
        print(f"{self.name} is studying with {self.teacher.name}")


teacher = Teacher("Rahul")
student = Student("Dhruv", teacher)

student.study()
teacher.teach()


# Association ka matlab hai do classes ka ek dusre se relationship hona, lekin dono independently exist kar sakti hain.





class Teacher:
    def __init__(self, name: str) -> None:
        self.__name: str = name  # Private

    def get_name(self) -> str:
        return self.__name

    def teach(self, s: "Student") -> None:
        print(f"{self.__name} is teaching {s.get_name()}")


class Student:
    def __init__(self, name: str) -> None:
        self.__name: str = name  # Private

    def get_name(self) -> str:
        return self.__name


teacher1 = Teacher("Sharma Sir")
student1 = Student("Rahul")

teacher1.teach(student1)  # teach() takes Student type as parameter