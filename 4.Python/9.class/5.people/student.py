from person import Person

class Student(Person):
    #상속: student가 person이 가진 모든 속성,메서드을 갖는다


    def __int__(self, age, name,student_id):
        super().__int__(age, name)
        self._student_id = student_id

    def study(self):
        print(f"{self.name}은 고통에 시달립니다. 학번 : {self._student_id}")