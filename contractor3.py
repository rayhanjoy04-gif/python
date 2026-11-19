class Student:
    college_name = "Apna College"

    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    def welcome(self):
        print("Welcome student", self.name)

    def get_marks(self):
        return self.mark


s1 = Student("Rayhan", 97)

s1.welcome()
print(s1.get_marks())