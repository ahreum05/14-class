import sys

class Student :
    def set_list(self) :
        self.students = []
    
    def input_score(self) :
        student = {}
        student['name'] = input("이름 : ")
        student['kor'] = int(input("국어 : "))
        student['eng'] = int(input("영어 : "))
        student['mat'] = int(input("수학 : "))
        student['tot'] = student['kor'] + student['eng'] + student['mat']
        student['avg'] = student['tot'] / 3
        
        if student['avg'] >= 90 :
            student['grade'] = 'A'
        elif student['avg'] >= 80 and student['avg'] < 90 : 
            student['grade'] = 'B'
        elif student['avg'] >= 70 and student['avg'] < 80 : 
             student['grade'] = 'C'
        elif student['avg'] >= 60 and student['avg'] < 70 : 
             student['grade'] = 'D'
        elif student['avg'] < 60 : 
             student['grade'] = 'F'
        # 리스트에 저장
        self.students.append(student)
    
    def output_score(self) :
        print('{:<4s}\t {:<5s}\t {:<5s}\t {:<5s}\t {:<6s} {:<3s} {:<2s}'
         .format('이름', '국어', '영어', "수학", '총점', '평균','학점'))
        print('-----------------------------------------------------------')
        for s in self.students :
            str1 = '{name:<4s}\t {kor:<5d}\t {eng:<5d}\t {mat:<5d}\t {tot:<8d} {avg:<5.1f} {grade:<2s}'.format(**s)
            print(str1)
        print('-----------------------------------------------------------')
    
    def end_pgm(self) :
        print("종료")
        sys.exit(0)


# 객체 생성
student = Student()
student.set_list()

while True :
    print('성적 관리 프로그램')
    print('**************************')
    print('1. 성적 입력')
    print('2. 성적 출력')
    print('3. 종료')
    print('**************************')
    num = int(input("메뉴 번호 : "))
    print() 
    
    if num == 1 :
        student.input_score()
    elif num == 2 :
        student.output_score()
    elif num == 3 :
        student.end_pgm()
    
    print()
