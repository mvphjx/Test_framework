class Student(object):

    def __init__(self):
        self._birth = 1990
#如何使用@property
    @property
    def birth(self):
        return self._birth

#是否允许赋值
    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2018 - self._birth


# idea快捷輸入 main
if __name__ == '__main__':
    student = Student()
    print(student.birth)
    student.birth=1989
    print(student.birth)
